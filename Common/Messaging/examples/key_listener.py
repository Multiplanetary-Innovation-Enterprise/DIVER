#Key listener pub-sub example
#NOTE: MUST INSTALL THIS LIBRARY (pip) IN ORDER TO RUN THIS EXAMPLE IF RUNNING THIS
#THIS FILE DIRECTLY. OTHERWISE RUN FROM run_examples.py IN MESSAGING DIRECTORY.

import keyboard
import tkinter as tk

from ROVMessaging.MessageChannel import MessageChannel
from ROVMessaging.Message import Message
from ROVMessaging.MessageType import MessageType
from ROVMessaging.Publisher import Publisher
from ROVMessaging.Subscriber import Subscriber

class KeyboardInput(Publisher):
    __messageChannel = None
    def __init__(self, messageChannel:MessageChannel):
        self.__messageChannel = messageChannel

        keyboard.on_press_key('w', self.forward, True)
        keyboard.on_press_key('s', self.backward, True)
        keyboard.on_press_key('up', self.up, True)
        keyboard.on_press_key('down', self.down, True)

    #Sends move forward action
    def forward(self, event):
        message = Message(MessageType.ACTION, "Move forward!")
        self.sendMessage(message, self.__messageChannel)

    #Send move backward action
    def backward(self, event):
        message = Message(MessageType.ACTION, "Move backward!")
        self.sendMessage(message, self.__messageChannel)

    #Send move up action
    def up(self, event):
        message = Message(MessageType.ACTION, "Move up!")
        self.sendMessage(message, self.__messageChannel)

    #Send move down action
    def down(self, event):
        message = Message(MessageType.ACTION, "Move down!")
        self.sendMessage(message, self.__messageChannel)

    def sendMessage(self, message:Message, messageChannel:MessageChannel) -> None:
        messageChannel.broadcast(message)

class ROV(Subscriber):
    def recieveMessage(self, message:Message) -> None:
        print("Action: " + str(message.getContents()))

messageChannel = MessageChannel()

keyboardInput = KeyboardInput(messageChannel)
rov = ROV()

messageChannel.subscribe(MessageType.ACTION, rov)

#Simple GUI
label = tk.Label(text="ROV GUI")
label.pack()
tk.mainloop()
