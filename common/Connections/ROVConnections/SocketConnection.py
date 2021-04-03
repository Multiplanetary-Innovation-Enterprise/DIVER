from socket import *

class SocketConnection():
    __socket = None;

    def __init__(self, socket):
        self.__socket = socket

    def getSocket(self):
        return self.__socket

    def close(self):
        self.__socket.close();
