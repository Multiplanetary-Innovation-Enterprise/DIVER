from Messaging import Publisher

class PubListener(Publisher):
    __reader = None
    __channel = None
    __message = None

    def __init__(self, reader:Reader, messageChannel:MessageChannel):
        self.__reader = reader
        self.__channel = messageChannel
        self.__message = ''

    def sendMessage(self, message:Message, messageChannel:MessageChannel) -> None:
        messageChannel.broadcast(message)

    def messageReady(self):
        self.__message = self.__reader.receive()
        if self.__message == '':
            return False
        else:
            return True

    def getMessage(self):
        return message
