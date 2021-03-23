from socket import *

class SocketConnection():
    __socket = None;

    def __init__(self, *args):
        if (len(args) == 0):
            self.__socket = socket(AF_INET, SOCK_STREAM)
        else:
            self.__socket = args[0]

    # @classmethod
    # def withsocket(self, socket):
    #     self.__socket = socket

    def get(self):
        return self.__socket

    def close(self):
        self.__socket.close();
