
import configparser
import time

from ROVMessaging.MessageChannel import MessageChannel
from ROVMessaging.MessageType import MessageType
from ROVMessaging.Message import Message
from ROVMessaging.Action import Action
from ROVMessaging.Publisher import Publisher

from ROVConnections.SocketWriter import *
from ROVConnections.SocketReader import *
from ROVConnections.ClientConnection import *
from ROVConnections.SubWriter import *
from ROVConnections.PubListener import *

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
            tempSensor = sensorSystem.getInternalTempSensor()

            #Convert time to seconds
            elapsedTime = round((time.time_ns() - startTime) / 1000000000, 2)

            #Only sensor data is temp data so far
            sensorData = {
                'internalTemp': tempSensor.getTemperature(),
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

clientConnection = ClientConnection('', port)

print("Waiting for client connection")
#Wait for the client program to connect
clientConnection.listenAndAccept(10)

socketReader = SocketReader(clientConnection.getClient())
pubListener = PubListener(socketReader, incomingMessageChannel)

socketWriter = SocketWriter(clientConnection.getClient())
subWriter = SubWriter(socketWriter)

dataSender = DataSender(outgoingMessageChannel)
dataSender.start()

incomingMessageChannel.subscribe(MessageType.ACTION, commandProcessor)
incomingMessageChannel.subscribe(MessageType.SYSTEM_STATUS, ShutdownHandler())

outgoingMessageChannel.subscribe(MessageType.SENSOR_DATA, subWriter)

#Start listening for messages from the client program
pubListener.listen()
dataSender.stop()

# #----------------------------testing purpose only below-----------------------------------
# import keyboard
# import tkinter as tk
#
# class KeyboardInput(Publisher):
#     __messageChannel = None
#     def __init__(self, messageChannel:MessageChannel):
#         self.__messageChannel = messageChannel
#
#         keyboard.on_press_key('space', self.arm, True)
#
#         keyboard.on_press_key('w', self.forward, True)
#         keyboard.on_release_key('w', self.stopXY, True)
#
#         keyboard.on_press_key('s', self.backward, True)
#         keyboard.on_release_key('s', self.stopXY, True)
#
#         keyboard.on_press_key('a', self.left, True)
#         keyboard.on_release_key('a', self.stopXY, True)
#
#         keyboard.on_press_key('d', self.right, True)
#         keyboard.on_release_key('d', self.stopXY, True)
#
#         keyboard.on_press_key('up', self.up, True)
#         keyboard.on_release_key('up', self.stopZ, True)
#
#         keyboard.on_press_key('down', self.down, True)
#         keyboard.on_release_key('down', self.stopZ, True)
#
#         keyboard.on_press_key('right', self.increaseSpeed, True)
#         keyboard.on_press_key('left', self.decreaseSpeed, True)
#
#         keyboard.on_release_key('l', self.toggleLight, True)
#
#         keyboard.on_press_key(']', self.increaseBrightness, True)
#         keyboard.on_press_key('[', self.decreaseBrightness, True)
#
#         keyboard.on_press_key('o', self.increaseClawAngle, True)
#         keyboard.on_release_key('o', self.deactivateClaw, True)
#         keyboard.on_press_key('p', self.decreaseClawAngle, True)
#         keyboard.on_release_key('p', self.deactivateClaw, True)
#
#     #Sends move forward action
#     def forward(self, event):
#         message = Message(MessageType.ACTION, Action.MOVE_XY_FORWARD)
#         self.sendMessage(message, self.__messageChannel)
#
#     #Send move backward action
#     def backward(self, event):
#         message = Message(MessageType.ACTION, Action.MOVE_XY_BACKWARD)
#         self.sendMessage(message, self.__messageChannel)
#
#     def stopXY(self, event):
#         message = Message(MessageType.ACTION, Action.MOVE_XY_STOP)
#         self.sendMessage(message, self.__messageChannel)
#
#     #Send move up action
#     def up(self, event):
#         message = Message(MessageType.ACTION, Action.MOVE_Z_POS)
#         self.sendMessage(message, self.__messageChannel)
#
#     #Send move down action
#     def down(self, event):
#         message = Message(MessageType.ACTION, Action.MOVE_Z_NEG)
#         self.sendMessage(message, self.__messageChannel)
#
#     def stopZ(self, event):
#         message = Message(MessageType.ACTION, Action.MOVE_Z_STOP)
#         self.sendMessage(message, self.__messageChannel)
#
#     #Sends a move right command
#     def right(self, event):
#         message = Message(MessageType.ACTION, Action.MOVE_XY_LEFT)
#         self.sendMessage(message, self.__messageChannel)
#
#     #Sends a move left command
#     def left(self, event):
#         message = Message(MessageType.ACTION, Action.MOVE_XY_RIGHT)
#         self.sendMessage(message, self.__messageChannel)
#
#     def arm(self, event):
#         message = Message(MessageType.ACTION, Action.ARM)
#         self.sendMessage(message, self.__messageChannel)
#
#     def increaseSpeed(self, event):
#         message = Message(MessageType.ACTION, Action.SPEED_INCREASE)
#         self.sendMessage(message, self.__messageChannel)
#
#     def decreaseSpeed(self, event):
#         message = Message(MessageType.ACTION, Action.SPEED_DECREASE)
#         self.sendMessage(message, self.__messageChannel)
#
#     def sendMessage(self, message:Message, messageChannel:MessageChannel) -> None:
#         messageChannel.broadcast(message)
#
#     def toggleLight(self, event):
#         print("Toggle light")
#         message = Message(MessageType.ACTION, Action.TOGGLE_LIGHTS)
#         self.sendMessage(message, self.__messageChannel)
#
#     def increaseBrightness(self, event):
#         message = Message(MessageType.ACTION, Action.BRIGHTNESS_INCREASE)
#         self.sendMessage(message, self.__messageChannel)
#
#     def decreaseBrightness(self, event):
#         message = Message(MessageType.ACTION, Action.BRIGHTNESS_DECREASE)
#         self.sendMessage(message, self.__messageChannel)
#
#     def increaseClawAngle(self, event):
#         message = Message(MessageType.ACTION, Action.CLAW_ANGLE_INCREASE)
#         self.sendMessage(message, self.__messageChannel)
#
#     def decreaseClawAngle(self, event):
#         message = Message(MessageType.ACTION, Action.CLAW_ANGLE_DECREASE)
#         self.sendMessage(message, self.__messageChannel)
#
#     def deactivateClaw(self, event):
#         message = Message(MessageType.ACTION, Action.CLAW_DEACTIVATE)
#         self.sendMessage(message, self.__messageChannel)

# keyboardInput = KeyboardInput(messageChannel)
