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

import configparser

class ShutdownHandler(Subscriber):
    def recieveMessage(self, message:Message) -> None:

        if message.getContents() != SystemStatus.SHUT_DOWN:
            return

        print("Shuting down...")

        pubListener.stop()
        clientConnection.close()
        server.stop()

messageChannel = MessageChannel()

rov = ROV()
prop = rov.getPropSystem();

commandFactory = CommandFactory(rov, messageChannel)

commandProcessor = CommandProcessor(commandFactory)

config = configparser.ConfigParser()
config.read('config.ini')

port = int(config['Server']['Port'])

clientConnection = ClientConnection(25010)

print("Waiting for client connection")
clientConnection.listenAndAccept(10)

socketReader = SocketReader(clientConnection.client())
pubListener = PubListener(socketReader, messageChannel)

socketWriter = SocketWriter(clientConnection.client())
subWriter = SubWriter(socketWriter)

messageChannel.subscribe(MessageType.ACTION, commandProcessor)
messageChannel.subscribe(MessageType.SYSTEM_STATUS, ShutdownHandler())
messageChannel.subscribe(MessageType.ACTION, subWriter)

pubListener.listen()

#----------------------------testing purpose only below-----------------------------------
import keyboard
import tkinter as tk

class KeyboardInput(Publisher):
    __messageChannel = None
    def __init__(self, messageChannel:MessageChannel):
        self.__messageChannel = messageChannel

        keyboard.on_press_key('space', self.arm, True)

        keyboard.on_press_key('w', self.forward, True)
        keyboard.on_release_key('w', self.stopXY, True)

        keyboard.on_press_key('s', self.backward, True)
        keyboard.on_release_key('s', self.stopXY, True)

        keyboard.on_press_key('a', self.left, True)
        keyboard.on_release_key('a', self.stopXY, True)

        keyboard.on_press_key('d', self.right, True)
        keyboard.on_release_key('d', self.stopXY, True)

        keyboard.on_press_key('up', self.up, True)
        keyboard.on_release_key('up', self.stopZ, True)

        keyboard.on_press_key('down', self.down, True)
        keyboard.on_release_key('down', self.stopZ, True)

        keyboard.on_press_key('right', self.increaseSpeed, True)
        keyboard.on_press_key('left', self.decreaseSpeed, True)

        keyboard.on_release_key('l', self.toggleLight, True)

        keyboard.on_press_key(']', self.increaseBrightness, True)
        keyboard.on_press_key('[', self.decreaseBrightness, True)

    #Sends move forward action
    def forward(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_XY_FORWARD)
        self.sendMessage(message, self.__messageChannel)

    #Send move backward action
    def backward(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_XY_BACKWARD)
        self.sendMessage(message, self.__messageChannel)

    def stopXY(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_XY_STOP)
        self.sendMessage(message, self.__messageChannel)

    #Send move up action
    def up(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_Z_POS)
        self.sendMessage(message, self.__messageChannel)

    #Send move down action
    def down(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_Z_NEG)
        self.sendMessage(message, self.__messageChannel)

    def stopZ(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_Z_STOP)
        self.sendMessage(message, self.__messageChannel)

    #Sends a move right command
    def right(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_XY_LEFT)
        self.sendMessage(message, self.__messageChannel)

    #Sends a move left command
    def left(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_XY_RIGHT)
        self.sendMessage(message, self.__messageChannel)

    def arm(self, event):
        message = Message(MessageType.ACTION, Action.ARM)
        self.sendMessage(message, self.__messageChannel)

    def increaseSpeed(self, event):
        message = Message(MessageType.ACTION, Action.SPEED_INCREASE)
        self.sendMessage(message, self.__messageChannel)

    def decreaseSpeed(self, event):
        message = Message(MessageType.ACTION, Action.SPEED_DECREASE)
        self.sendMessage(message, self.__messageChannel)

    def sendMessage(self, message:Message, messageChannel:MessageChannel) -> None:
        messageChannel.broadcast(message)

    def toggleLight(self, event):
        print("Toggle light")
        message = Message(MessageType.ACTION, Action.TOGGLE_LIGHTS)
        self.sendMessage(message, self.__messageChannel)

    def increaseBrightness(self, event):
        message = Message(MessageType.ACTION, Action.BRIGHTNESS_INCREASE)
        self.sendMessage(message, self.__messageChannel)

    def decreaseBrightness(self, event):
        message = Message(MessageType.ACTION, Action.BRIGHTNESS_DECREASE)
        self.sendMessage(message, self.__messageChannel)

keyboardInput = KeyboardInput(messageChannel)

#Simple GUI
label = tk.Label(text="ROV GUI")
label.pack()
tk.mainloop()
