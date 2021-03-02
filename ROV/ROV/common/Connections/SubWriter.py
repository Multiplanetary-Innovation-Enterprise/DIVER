from Messaging import Subscriber

class SubWriter(Subscriber):
    __writer = None

    def __init__(writer:Writer):
        self.__writer = writer

    def recieveMessage(self, message:Message) -> None:
        self.__writer.send(message)
