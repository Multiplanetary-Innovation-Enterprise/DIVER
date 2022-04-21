import queue
import threading

from ROVMessaging.Subscriber import *
from ROVMessaging.Message import *
from ROVConnections.Writer import Writer
from ROVMessaging.MessageType import *

#This class is used to write any messages that it recieves using the provided writer
class SubWriter(Subscriber):
    __writer:Writer = None   #The writer used for sending the message
    __isRunning:bool = False #Whether or not the message queue is running
    __queue = None           #Stores the messages that have not been sent yet
    __thread = None          #The thread that processes the messages

    def __init__(self, writer:Writer):
        self.__writer = writer
        self.__queue = queue.Queue()

    #Uses the writer to send the message that it recieves
    def recieveMessage(self, message:Message) -> None:
        #Adds the message to queue of messsages to send out
        self.__queue.put(message)

        #Checks if the message queue is already being processed
        if not self.__isRunning:
            #Starts processsing the messages by creating a new thread
            self.__thread = threading.Thread(target=self.__sendMessage)
            self.__thread.start()

    #Processes the message queue
    def __sendMessage(self) -> None:
        self.__isRunning = True

        #Continues sending messages until all messages have been sent
        while not self.__queue.empty() and self.__isRunning:
            #Gets the next message and sends it
            message = self.__queue.get_nowait()

            #Handles exceptions if the connection was closed
            try:
                self.__writer.send(message)
            except:
                #Something broke the connection, so stop the writer and try to
                #recover elsewhere
                print("Write connection broken")
                self.__isRunning = False
                break

            print("Processing messages: " + str(self.__queue.qsize()))

        self.__isRunning = False

    def stop(self) -> None:
        self.__isRunning = False

        self.join()

    #Forces the calling thread to wait until the publisher listener has stopped
    def join(self) -> None:
        #Checks if a thread has been created yet (a message has been sent)
        if self.__thread == None:
            return

        #Prevents the listen thread from joining to itself (would infinitly block)
        if not threading.get_ident() == self.__thread.ident:
            self.__thread.join()
