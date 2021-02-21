from ROVMessaging.MessageChannel import MessageChannel
from ROVMessaging.MessageType import MessageType
from ROVMessaging.Message import Message
from ROVMessaging.Action import Action
from ROVMessaging.Publisher import Publisher

from commands.CommandProcessor import CommandProcessor
from commands.CommandFactory import CommandFactory

from ROV import ROV

messageChannel = MessageChannel()

rov = ROV()

commandFactory = CommandFactory(rov, messageChannel)

commandProcessor = CommandProcessor(commandFactory)

messageChannel.subscribe(MessageType.ACTION, commandProcessor)

#messageChannel.broadcast(Message(MessageType.ACTION, Action.MOVE_X_POS))

#----------------------------testing purpose only below-----------------------------------
import keyboard
import tkinter as tk

class KeyboardInput(Publisher):
    __messageChannel = None
    def __init__(self, messageChannel:MessageChannel):
        self.__messageChannel = messageChannel

        keyboard.on_press_key('space', self.arm, True)

        keyboard.on_press_key('w', self.forward, True)
        keyboard.on_release_key('w', self.stopX, True)

        keyboard.on_press_key('s', self.backward, True)
        keyboard.on_release_key('s', self.stopX, True)


        keyboard.on_press_key('a', self.left, True)
        keyboard.on_release_key('a', self.stopY, True)

        keyboard.on_press_key('d', self.right, True)
        keyboard.on_release_key('d', self.stopY, True)

        keyboard.on_press_key('up', self.up, True)
        keyboard.on_release_key('up', self.stopZ, True)

        keyboard.on_press_key('down', self.down, True)
        keyboard.on_release_key('down', self.stopZ, True)

        keyboard.on_press_key('right', self.increaseSpeed, True)
        keyboard.on_press_key('left', self.decreaseSpeed, True)

    #Sends move forward action
    def forward(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_X_POS)
        self.sendMessage(message, self.__messageChannel)

    #Send move backward action
    def backward(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_X_NEG)
        self.sendMessage(message, self.__messageChannel)

    def stopX(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_X_STOP)
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
        message = Message(MessageType.ACTION, Action.MOVE_Y_POS)
        self.sendMessage(message, self.__messageChannel)

    #Sends a move left command
    def left(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_Y_NEG)
        self.sendMessage(message, self.__messageChannel)

    #Sends a stop moving in y-axis command
    def stopY(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_Y_STOP)
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

keyboardInput = KeyboardInput(messageChannel)

#Simple GUI
label = tk.Label(text="ROV GUI")
label.pack()
tk.mainloop()
