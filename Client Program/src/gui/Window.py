from tkinter import Tk

from ROVMessaging.Publisher import Publisher
from ROVMessaging.MessageChannel import *
from ROVMessaging.MessageType import *
from ROVMessaging.Message import *
from ROVMessaging.SystemStatus import *

#Represents the window the houses all GUI frames
class Window(Tk,Publisher):
    #The message channel to send GUI events through
    __messageChannel:MessageChannel = None

    def __init__(self, messageChannel:MessageChannel):
        super().__init__()
        self.__messageChannel = messageChannel

    #Creates the window and configures it
    def create(self) -> None:
        self.geometry("1000x500")
        self.title("ROV Client")

        #Registers the window close handler
        self.protocol("WM_DELETE_WINDOW", self.onClose)

    #The on close window handler that handles shutdown
    def onClose(self) -> None:
        #Sends the shutdown message
        message = Message(MessageType.SYSTEM_STATUS, SystemStatus.SHUT_DOWN)
        self.sendMessage(message, self.__messageChannel)

        #Destroys the window
        self.destroy()

    #Sends the provided message on the provided message channel
    def sendMessage(self, message:Message, messageChannel:MessageChannel) -> None:
        messageChannel.broadcast(message)
