import configparser

from ROVMessaging.MessageChannel import MessageChannel
from ROVMessaging.MessageType import MessageType
from ROVMessaging.Subscriber import Subscriber
from ROVMessaging.SystemStatus import *

from ROVConnections.SocketWriter import *
from ROVConnections.SocketReader import *
from ROVConnections.SubWriter import *
from ROVConnections.PubListener import *
from ROVConnections.SocketServer import *

from commands.CommandProcessor import CommandProcessor
from commands.CommandFactory import CommandFactory

from ROV import ROV
from DataSender import DataSender

#Represents the ROV program
class ROVApp(Subscriber):
    __config = None                             #The config data
    __isRunning:bool = False                    #Whether or not the program is running
    __clientConnection: SocketConnection = None #The connection to the client program
    __pubListener: PubListener = None           #Listens for messages from the client program
    __dataSender: DataSender = None             #Sends the sensor data to the client

    #The setup used for initializing all of the resources that will be needed
    def __setup(self) -> None:
        #Reads in the configuration file
        config = configparser.ConfigParser()
        config.read('..\config.ini')

        #The message channels for sending and recieving messages. Incoming can also
        #be used for sending internal messages
        incomingMessageChannel = MessageChannel()
        outgoingMessageChannel = MessageChannel()

        #The representation of the ROV and its sub systems
        rov = ROV()

        #Used to decode and process commands
        commandFactory = CommandFactory(rov, outgoingMessageChannel) #message channel temp for testing
        commandProcessor = CommandProcessor(commandFactory)

        #Sets up the sever to listen at the provided port
        port = int(config['Server']['Port'])
        server = SocketServer('', port)

        print("Waiting for client connection")

        #Wait for the client program to connect
        self.__clientConnection = server.getClientConnection()

        #Reads messages from the client and rebroadcasts them internally using the
        #incoming message channel
        socketReader = SocketReader(self.__clientConnection)
        self.__pubListener = PubListener(socketReader, incomingMessageChannel)

        #Listens for messages that it is registered to and sends them over the
        #socekt to the client program
        socketWriter = SocketWriter(self.__clientConnection)
        subWriter = SubWriter(socketWriter)

        self.__dataSender = DataSender(outgoingMessageChannel)
        self.__dataSender.start()

        #Registers the command processor to listen for actions (correspond to comands)
        #and registers the ROV App to listen for system status changes
        incomingMessageChannel.subscribe(MessageType.ACTION, commandProcessor)
        incomingMessageChannel.subscribe(MessageType.SYSTEM_STATUS, self)

        #Listens for sensor data updates and sends it to the client program
        outgoingMessageChannel.subscribe(MessageType.SENSOR_DATA, subWriter)

        #Start listening for messages from the client program
        self.__pubListener.listen()

    #Starts the ROV if it is not already running
    def start(self) -> None:
        if not self.__isRunning:
            self.__isRunning = True
            self.__run()

    #The main loop for the program
    def __run(self) -> None:
        self.__setup()

        while self.__isRunning:
            pass

        self.__cleanup()

    #Tells the ROV to stop running
    def stop(self) -> None:
        self.__isRunning = False

    #Used to close resources as part of the shutdown process
    def __cleanup(self) -> None:
        self.__pubListener.stop()
        self.__clientConnection.close()
        self.__dataSender.stop()

    #TODO
    def recieveMessage(self, message:Message) -> None:
        print("message")
        #Checks if the message is a shutdown message
        if (message.getType()     == MessageType.SYSTEM_STATUS and
            message.getContents() == SystemStatus.SHUT_DOWN):

            print("Shutodnw")

            self.stop()
