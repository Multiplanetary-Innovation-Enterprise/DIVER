import configparser
import sys

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
from loggers.DataLogger import DataLogger
from gui.Window import Window

#Represents the ROV Client program
class ClientApp(Subscriber):
    __config = None                            #The config data
    __serverConnection:SocketConnection = None #The connection to the ROV
    __dataLogger:DataLogger = None             #The sensor data logger
    __window:Window = None                     #The GUI window
    __pubListener: PubListener = None          #Listens for messages from the ROV program
    __isRunning:bool = False                   #Whether or not the program is running

    #The setup used for initializing all of the resources that will be needed
    def __setup(self) -> None:
        #Opens the config file
        self.__config = configparser.ConfigParser()
        self.__config.read('..\config.ini')

        #Connection info for connecting to the ROV
        host = str(self.__config['ROV_CONNECTION']['Host'])
        port = int(self.__config['ROV_CONNECTION']['Port'])

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
        outgoingMessageChannel = MessageChannel()

        #Sets up ability to send messages to the ROV
        socketWriter = SocketWriter(self.__serverConnection)
        subWriter = SubWriter(socketWriter)

        #Sets up the abilty to recieve messages from the ROV
        socketReader = SocketReader(self.__serverConnection)
        self.__pubListener = PubListener(socketReader, incomingMessageChannel)

        #The input method that utilizes a keyboard
        keyboardInput = KeyboardInput(outgoingMessageChannel)

        #Start listening for messages from the ROV
        self.__pubListener.listen()

        #Sets up the data logger and creates a new log file
        self.__dataLogger = DataLogger()
        self.__dataLogger.openFile("..\logs\data\data_log");

        #Allows the client to send action and system status messages to the ROV
        outgoingMessageChannel.subscribe(MessageType.ACTION, subWriter)
        outgoingMessageChannel.subscribe(MessageType.SYSTEM_STATUS, subWriter)

        #Allows the client to recieve sensor data from the ROV
        incomingMessageChannel.subscribe(MessageType.SENSOR_DATA, self.__dataLogger)

        #Listens for any system status changes from either this program or the ROV
        outgoingMessageChannel.subscribe(MessageType.SYSTEM_STATUS, self)
        incomingMessageChannel.subscribe(MessageType.SYSTEM_STATUS, self)

        #Setups the GUI window
        self.__window = Window(outgoingMessageChannel)
        self.__window.create()

    #Starts the ROV client if it is not already running
    def start(self) -> None:
        if not self.__isRunning:
            self.__isRunning = True

            self.__run()

    #The main loop for the program
    def __run(self) -> None:
        self.__setup()

        while self.__isRunning:
            self.__window.mainloop()

        self.__cleanup()

    #Tells the ROV client to stop running
    def stop(self) -> None:
        self.__isRunning = False

    #Used to close resources as part of the shutdown process
    def __cleanup(self) -> None:
        self.__dataLogger.close()
        self.__serverConnection.close()
        self.__pubListener.stop()

        #This is causing the socket errors on close, need to wait until PubListener is done
        #before calling this line

        print("Exiting...")

    def recieveMessage(self, message:Message) -> None:
        #Checks if the message is a shutdown message
        if (message.getType()     == MessageType.SYSTEM_STATUS and
            message.getContents() == SystemStatus.SHUT_DOWN):

            self.stop()