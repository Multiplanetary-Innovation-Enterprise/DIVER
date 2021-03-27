from ROVMessaging.Publisher import *
from ROVMessaging.Message import *
from ROVMessaging.MessageType import MessageType
from ROVMessaging.SystemStatus import SystemStatus
from ROVMessaging.MessageChannel import *
from ROVConnections.Reader import Reader

class PubListener(Publisher):
    __reader = None
    __channel = None
    __message = None
    __isRunning = False

    def __init__(self, reader, messageChannel:MessageChannel):
        self.__reader = reader
        self.__channel = messageChannel
        self.__message = ''

    def sendMessage(self, message:Message, messageChannel:MessageChannel) -> None:
        messageChannel.broadcast(message)

    def messageReady(self):
        self.__message = self.__reader.receive()

        if self.__message == None:
            return False
        else:
            return True

    def listen(self):
        self.__isRunning = True

        while self.__isRunning:
            if(self.messageReady()):
                message = self.__message

                if(message.getType() == MessageType.SYSTEM_STATUS and message.getContents() == SystemStatus.SHUT_DOWN):
                    print("shutdown")
                    self.stop()
                    break

                self.sendMessage(self.__message, self.__channel)

    def stop(self):
        self.__isRunning = False
