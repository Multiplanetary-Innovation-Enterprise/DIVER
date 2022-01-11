import socket
import configparser

from ROVMessaging.MessageChannel import MessageChannel
from ROVMessaging.MessageType import MessageType
from ROVMessaging.Subscriber import Subscriber
from ROVMessaging.SystemStatus import *
from ROVMessaging.Message import Message

from ROVConnections.SocketWriter import *
from ROVConnections.SocketReader import *
from ROVConnections.SubWriter import *
from ROVConnections.PubListener import *
from ROVConnections.SocketServer import *

from commands.CommandProcessor import CommandProcessor
from commands.CommandFactory import CommandFactory

from ROV import ROV
from collectors.SensorDataCollector import SensorDataCollector

#Represents the ROV program
class ROVApp(Subscriber):
    __config = None                                  #The config data
    __isRunning:bool = False                         #Whether or not the program is running
    __clientConnection:SocketConnection = None       #The connection to the client program
    __pubListener:PubListener = None                 #Listens for messages from the client program
    __sensorDataCollector:SensorDataCollector = None #Sends the sensor data to the client
    __outgoingMessageChannel:MessageChannel  = None  #The message channel to the client program
    __server:SocketServer  = None                    #The server that listens for client connection requests
    __shutdownEvent = None                           #The event the main thread waits for before shutdown

    #The setup used for initializing all of the resources that will be needed
    def __setup(self) -> None:
        #Reads in the configuration file
        config = configparser.ConfigParser()
        config.read('..\config.ini')

        #The message channels for sending and recieving messages. Incoming can also
        #be used for sending internal messages
        incomingMessageChannel = MessageChannel()
        self.__outgoingMessageChannel = MessageChannel()

        #The representation of the ROV and its sub systems
        rov = ROV()

        #Used to decode and process commands
        commandFactory = CommandFactory(rov, self.__outgoingMessageChannel) #message channel temp for testing
        commandProcessor = CommandProcessor(commandFactory)

        #Sets up the sever to listen at the provided port
        port = int(config['Server']['Port'])
        self.__server = SocketServer('', port)

        print("Waiting for client connection")

        #Wait for the client program to connect
        self.__clientConnection = self.__server.getClientConnection()

        #Reads messages from the client and rebroadcasts them internally using the
        #incoming message channel
        socketReader = SocketReader(self.__clientConnection)
        self.__pubListener = PubListener(socketReader, incomingMessageChannel)

        #Listens for messages that it is registered to and sends them over the
        #socekt to the client program
        socketWriter = SocketWriter(self.__clientConnection)
        subWriter = SubWriter(socketWriter)

        #Retrieves and sends the sensor data to the client
        self.__sensorDataCollector = SensorDataCollector(rov, self.__outgoingMessageChannel)
        self.__sensorDataCollector.setSampleFrequency(1)
        self.__sensorDataCollector.start()

        #Registers the command processor to listen for actions (correspond to comands)
        #and registers the ROV App to listen for system status changes
        incomingMessageChannel.subscribe(MessageType.ACTION, commandProcessor)
        incomingMessageChannel.subscribe(MessageType.SYSTEM_STATUS, self)

        #Listens for sensor data and system status updates and sends it to the client program
        self.__outgoingMessageChannel.subscribe(MessageType.SENSOR_DATA, subWriter)
        self.__outgoingMessageChannel.subscribe(MessageType.SYSTEM_STATUS, subWriter)

        #Start listening for messages from the client program
        self.__pubListener.listen()

        #The shutdown event that the main thread will wait for
        self.__shutdownEvent = threading.Event()

    #Starts the ROV if it is not already running
    def start(self) -> None:
        if not self.__isRunning:
            self.__isRunning = True
            self.__run()

    #The main loop for the program
    def __run(self) -> None:
        self.__setup()

        #Put something here instead of infinite loop (wastes cpu time)
        while self.__isRunning:
            #Waits for the shutdown event, since the main thread isn't currently
            #used for anything
            self.__shutdownEvent.wait()

        self.__cleanup()

    #Tells the ROV to stop running
    def stop(self) -> None:
        self.__isRunning = False

    #Used to close resources as part of the shutdown process
    def __cleanup(self) -> None:
        print("shuting down...")
        self.__sensorDataCollector.stop()
        self.__server.stop()

        #Tells the client that it is shutting down
        message = Message(MessageType.SYSTEM_STATUS, SystemStatus.SHUT_DOWN)
        self.__outgoingMessageChannel.broadcast(message)

        #Sends EOF to the client, so that its socket reader stops blocking
        self.__clientConnection.shutdown(socket.SHUT_WR)

        #Waits for pub listener to stop blocking (occurs once the client sends EOF
        #by shutting down its side of the socekt)
        self.__pubListener.stop()

        #Finally closes the socket, since the client is disconnected
        self.__clientConnection.close()

    def recieveMessage(self, message:Message) -> None:
        #Checks if the message is a shutdown message
        if (message.getType()     == MessageType.SYSTEM_STATUS and
            message.getContents() == SystemStatus.SHUT_DOWN):
            self.stop()

            #Wakes the main thread up, so that it can proceed with shutdown
            self.__shutdownEvent.set()
