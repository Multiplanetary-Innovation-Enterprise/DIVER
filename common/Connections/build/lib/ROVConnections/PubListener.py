import threading

from ROVMessaging.Publisher import *
from ROVMessaging.Message import *
from ROVMessaging.MessageChannel import *
from ROVConnections.Reader import Reader

#This class is used to publish any messages recieved by the reader onto the
#provided message channel for interal communications
class PubListener(Publisher):
    __reader:Reader = None          #The reader to recieve messages from
    __channel:MessageChannel = None #The message channel to forward recieved messages to
    __isRunning:bool = False        #The runnning status of the listening thread
    __listenThread = None           #The thread used to listen for messages

    def __init__(self, reader:Reader, messageChannel:MessageChannel):
        self.__reader = reader
        self.__channel = messageChannel
        self.__message = ''

    #Sends the recieved message over the message channel
    def sendMessage(self, message:Message, messageChannel:MessageChannel) -> None:
        messageChannel.broadcast(message)

    #Starts up the thread for listening for incoming messages
    def listen(self) -> None:
        #Checks if the message listening thread already exists
        if not self.__isRunning:
            self.__listenThread = threading.Thread(target=self.__listen)
            self.__listenThread.start()

            self.__isRunning = True

    #The underlying listen function used by the listen thread
    def __listen(self) -> None:
        #Keeps listening for new messages until shutdown
        while self.__isRunning:
            #Performs the blocking reads for a new message
            message = self.__reader.receive()
            #Sends the recieved message over the message channel
            self.sendMessage(message, self.__channel)

    #Tells the message listening thread to stop
    def stop(self) -> None:
        self.__isRunning = False
