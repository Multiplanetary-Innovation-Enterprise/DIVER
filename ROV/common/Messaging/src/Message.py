from MessageType import MessageType

#A message that can be published to a message channel
class Message():
    __contents = None
    __type: MessageType = None

    #Creates a message given a type and contents
    def __init__(self, type:MessageType, contents):
        self.__contents = contents
        self.__type = type

    #Gets the contents stored in the message
    def getContents(self):
        return self.__contents

    #Gets the type of the message
    def getType(self) -> MessageType:
        return self.__type
