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

    #Sends the recieved message over the message channel
    def sendMessage(self, message:Message, messageChannel:MessageChannel) -> None:
        messageChannel.broadcast(message)

    #Starts up the thread for listening for incoming messages
    def listen(self) -> None:
        #Checks if the message listening thread already exists
        if not self.__isRunning:
            self.__listenThread = threading.Thread(target=self.__listen)
            self.__listenThread.start()

    #The underlying listen function used by the listen thread
    def __listen(self) -> None:
        self.__isRunning = True

        #Keeps listening for new messages until shutdown
        while self.__isRunning:
            #Handles exceptions if the connection was closed
            try:
                #Performs the blocking reads for a new message
                message = self.__reader.receive()
            except:
                #Something broke the connection, so stop the listener and try to
                #recover elsewhere
                self.__isRunning = False
                print("Reader connection broken")
                break

            #Checks if a message was recieved. Used to check if the connection was closed.
            if message == None:
                continue

            #Sends the recieved message over the message channel
            self.sendMessage(message, self.__channel)

    #Stops the publisher listener from receiving any more messages via the reader
    def stop(self) -> None:
        self.__isRunning = False

        #Wait for the reader to stop listening for new messages
        self.join()

    #Forces the calling thread to wait until the publisher listener has stopped
    def join(self) -> None:
        #Prevents the listen thread from joining to itself (would infinitly block)
        if not threading.get_ident() == self.__listenThread.ident:
            self.__listenThread.join()
