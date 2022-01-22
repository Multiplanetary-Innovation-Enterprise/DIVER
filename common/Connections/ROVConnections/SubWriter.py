from ROVMessaging.Subscriber import *
from ROVMessaging.Message import *
from ROVConnections.Writer import Writer

#This class is used to write any messages that it recieves using the provided writer
class SubWriter(Subscriber):
    __writer:Writer = None #The writer used for sending the message
    __isRunning:bool = True #Whether or not messages will be sent out

    def __init__(self, writer:Writer):
        self.__writer = writer

    #Uses the writer to send the message that it recieves
    def recieveMessage(self, message:Message) -> None:
        #If stopped, don't send the message
        if not self.__isRunning:
            return

        self.__writer.send(message)

    def stop(self) -> None:
        self.__isRunning = False
