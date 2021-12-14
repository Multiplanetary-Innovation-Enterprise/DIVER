
import configparser
import time

from ROVMessaging.MessageChannel import MessageChannel
from ROVMessaging.MessageType import MessageType
from ROVMessaging.Message import Message
from ROVMessaging.Action import Action
from ROVMessaging.Publisher import Publisher

from ROVConnections.SocketWriter import *
from ROVConnections.SocketReader import *
from ROVConnections.SubWriter import *
from ROVConnections.PubListener import *
from ROVConnections.SocketServer import *

from commands.CommandProcessor import CommandProcessor
from commands.CommandFactory import CommandFactory

from ROV import ROV

class ShutdownHandler(Subscriber):
    def recieveMessage(self, message:Message) -> None:
        if message.getContents() != SystemStatus.SHUT_DOWN:
            return

        print("Shuting down...")

        pubListener.stop()
        clientConnection.close()

#Temporary until integrated into command system
class DataSender(Publisher):
    __messageChannel:MessageChannel = None
    __isRunning = False
    __thread = None

    def __init__(self, messageChannel:MessageChannel):
        self.__messageChannel = messageChannel

    def start(self):
        print("Sending data start")
        if not self.__isRunning:
            self.__thread = threading.Thread(target=self.__run)
            self.__thread.start()

            self.__isRunning = True

    def __run(self):
        print("Doesn't run without this print statement because python")
        while self.__isRunning:
            print("data sending")

            #Get temperature
            sensorSystem = rov.getSensorSystem()
            #tempSensor = sensorSystem.getInternalTempSensor()

            #Convert time to seconds
            elapsedTime = round((time.time_ns() - startTime) / 1000000000, 2)

            #Only sensor data is temp data so far
            sensorData = {
                'internalTemp': 12, #tempSensor.getTemperature(),
                'time': elapsedTime
            }

            message = Message(MessageType.SENSOR_DATA, sensorData)

            self.sendMessage(message, self.__messageChannel)

            time.sleep(1)

    def stop(self):
        __isRunning = False


    #Creates the action message and sends it over the message channel
    def sendMessage(self, message:Message, messageChannel:MessageChannel):
        print(message)
        messageChannel.broadcast(message)

startTime = time.time_ns()

incomingMessageChannel = MessageChannel()
outgoingMessageChannel = MessageChannel()

rov = ROV()
prop = rov.getPropSystem();

commandFactory = CommandFactory(rov, outgoingMessageChannel)

commandProcessor = CommandProcessor(commandFactory)

config = configparser.ConfigParser()
config.read('config.ini')

port = int(config['Server']['Port'])

server = SocketServer('', port)

print("Waiting for client connection")

#Wait for the client program to connect
clientConnection = server.getClientConnection()

socketReader = SocketReader(clientConnection)
pubListener = PubListener(socketReader, incomingMessageChannel)

socketWriter = SocketWriter(clientConnection)
subWriter = SubWriter(socketWriter)

dataSender = DataSender(outgoingMessageChannel)
dataSender.start()

incomingMessageChannel.subscribe(MessageType.ACTION, commandProcessor)
incomingMessageChannel.subscribe(MessageType.SYSTEM_STATUS, ShutdownHandler())

outgoingMessageChannel.subscribe(MessageType.SENSOR_DATA, subWriter)

#Start listening for messages from the client program
pubListener.listen()
dataSender.stop()
