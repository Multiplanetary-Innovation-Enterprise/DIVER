
class Message():
    __message = None

    def __init__(self, message):
        self.__message = message

    def message(self):
        return self.__message
