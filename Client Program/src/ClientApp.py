import sys
import socket
import configparser
from tkinter import *

from ROVConnections.SocketWriter import SocketWriter
from ROVConnections.SocketReader import SocketReader
from ROVConnections.SocketConnection import SocketConnection
from ROVConnections.PubListener import PubListener
from ROVConnections.SubWriter import SubWriter

from ROVMessaging.MessageChannel import *
from ROVMessaging.MessageType import *
from ROVMessaging.Subscriber import *
from ROVMessaging.SystemStatus import *

from inputs.KeyboardInput import KeyboardInput
from inputs.ControllerInput import ControllerInput
from loggers.DataLogger import DataLogger
from gui.Window import Window
from gui.ImageFrame import ImageFrame

#Represents the ROV Client program
class ClientApp(Subscriber):
    __config = None                                #The config data
    __serverConnection:SocketConnection = None     #The connection to the ROV
    __dataLogger:DataLogger = None                 #The sensor data logger
    __window:Window = None                         #The GUI window
    __pubListener:PubListener = None               #Listens for messages from the ROV program
    __isRunning:bool = False                       #Whether or not the program is running
    __outgoingMessageChannel:MessageChannel = None #The message channel to the ROV program
    __controllerInput:ControllerInput = None       #The xbox controller
    __subWriter:SubWriter = None

    #The setup used for initializing all of the resources that will be needed
    def __setup(self) -> None:
        #Opens the config file
        self.__config = configparser.ConfigParser()
        self.__config.read('..\config.ini')

        #Connection info for connecting to the ROV
        host = str(self.__config['ROV_CONNECTION']['Host'])
        port = int(self.__config['ROV_CONNECTION']['Port'])
        print("PORT: " + str(port) + " Host: " + str(host))
        #The connection to the ROV
        self.__serverConnection = SocketConnection(host=host, port=port)

        #Attempts to connect to the ROV
        try:
            self.__serverConnection.connect()
        except:
            print("Failed to connect to ROV")
            sys.exit()

        #The sending and receiving message channels
        incomingMessageChannel = MessageChannel()
        self.__outgoingMessageChannel = MessageChannel()

        #Sets up ability to send messages to the ROV
        socketWriter = SocketWriter(self.__serverConnection)
        self.__subWriter = SubWriter(socketWriter)

        #Sets up the abilty to recieve messages from the ROV
        socketReader = SocketReader(self.__serverConnection)
        self.__pubListener = PubListener(socketReader, incomingMessageChannel)

        #The input method that utilizes a keyboard
        keyboardInput = KeyboardInput(self.__outgoingMessageChannel)

        #Sets up the xbox controller
        self.__controllerInput = ControllerInput(self.__outgoingMessageChannel)
        self.__controllerInput.listen()

        #Start listening for messages from the ROV
        self.__pubListener.listen()

        #Sets up the data logger and creates a new log file
        self.__dataLogger = DataLogger()
        self.__dataLogger.openFile("..\logs\data\data_log");

        #Setups the GUI window
        self.__window = Window()
        self.__window.create()

        #Create a frame to show the camera feed and sets it to be the current one
        imageFrame = ImageFrame(self.__window)
        self.__window.switchFrame(imageFrame)

        #Allows the client to send action and system status messages to the ROV
        self.__outgoingMessageChannel.subscribe(MessageType.ACTION, self.__subWriter)
        self.__outgoingMessageChannel.subscribe(MessageType.SYSTEM_STATUS, self.__subWriter)

        #Allows the client to recieve sensor data from the ROV
        incomingMessageChannel.subscribe(MessageType.SENSOR_DATA, self.__dataLogger)

        #Listens for any system status changes from either this program or the ROV
        incomingMessageChannel.subscribe(MessageType.SYSTEM_STATUS, self)

        #Listens for new camera images from the ROV
        incomingMessageChannel.subscribe(MessageType.VISION_DATA, imageFrame)

    #Starts the ROV client if it is not already running
    def start(self) -> None:
        if not self.__isRunning:
            self.__isRunning = True

            self.__run()

    #The main loop for the program
    def __run(self) -> None:
        self.__setup()

        # while self.__isRunning:
        self.__window.mainloop()

        self.__cleanup()

    #Tells the ROV client to stop running
    def stop(self) -> None:
        self.__isRunning = False

    #Used to close resources as part of the shutdown process
    def __cleanup(self) -> None:
        print("shutting down...")

        #Stops the xbox controller listener thread
        self.__controllerInput.stop()

        #Stops the data logger
        self.__dataLogger.close()

        print("send shutdown mssage")

        #Tells the server that it is shutting down
        message = Message(MessageType.SYSTEM_STATUS, SystemStatus.SHUT_DOWN)
        self.__outgoingMessageChannel.broadcast(message)

        self.__subWriter.stop()

        #Sends EOF to the server, so that its socket reader stops blocking
        self.__serverConnection.shutdown(socket.SHUT_WR)

        #Waits for pub listener to stop blocking (occurs once the server sends EOF
        #by shutting down its side of the socekt)
        self.__pubListener.stop()

        #Finally closes the socket, since the server is disconnected
        self.__serverConnection.close()

    def recieveMessage(self, message:Message) -> None:
        #Checks if the message is a shutdown message
        if (message.getType()     == MessageType.SYSTEM_STATUS and
            message.getContents() == SystemStatus.SHUT_DOWN):

            self.stop()
