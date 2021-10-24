import threading

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
    __listenThread = None

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

    #Starts up the thread for listening to incoming messages
    def listen(self):
        if not self.__isRunning:
            self.__listenThread = threading.Thread(target=self.__listen)
            self.__listenThread.start()

            self.__isRunning = True

    #The underlying listen function used by the listen thread
    def __listen(self):
        print("Pub listening")

        while self.__isRunning:
            if(self.messageReady()):
                message = self.__message

                self.sendMessage(self.__message, self.__channel)
        print("Pub listener stopped")

    def stop(self):
        print("Stopping pub listener")
        self.__isRunning = False
