from ROVMessaging.Publisher import *
from ROVMessaging.Message import *
from ROVMessaging.MessageChannel import *
from ROVConnections.Reader import Reader

class PubListener(Publisher):
    __reader = None
    __channel = None
    __message = None

    def __init__(self, reader, messageChannel:MessageChannel):
        self.__reader = reader
        self.__channel = messageChannel
        self.__message = ''

    def sendMessage(self, message:Message, messageChannel:MessageChannel) -> None:
        print(f"In Pub: {message.getContents()}")
        messageChannel.broadcast(message)

    def messageReady(self):
        self.__message = self.__reader.receive()
        if self.__message == None:
            return False
        else:
            return True

    def getMessage(self):
        return self.__message
