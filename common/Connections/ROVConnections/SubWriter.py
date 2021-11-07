from ROVMessaging.Subscriber import *
from ROVMessaging.Message import *
from ROVConnections.Writer import Writer

#This class is used to write any messages that it recieves using the provided writer
class SubWriter(Subscriber):
    __writer:Writer = None #The writer used for sending the message

    def __init__(self, writer:Writer):
        self.__writer = writer

    #Uses the writer to send the message that it recieves
    def recieveMessage(self, message:Message) -> None:
        self.__writer.send(message)
