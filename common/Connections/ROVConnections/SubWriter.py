from ROVMessaging.Subscriber import *
from ROVMessaging.Message import *
from ROVConnections.Writer import Writer

class SubWriter(Subscriber):
    __writer:Writer = None

    def __init__(self, writer:Writer):
        self.__writer = writer

    def recieveMessage(self, message:Message) -> None:
        print("Sending")
        self.__writer.send(message)
