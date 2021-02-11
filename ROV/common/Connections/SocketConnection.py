from socket import *

class SocketConnection():
    __socket = None;

    def __init__(self):
        self.__socket = socket(AF_INET, SOCK_STREAM)

    def __init__(self, socket):
        self.__socket = socket

    def get(self):
        return self.__socket

    def close(self):
        self.__socket.close();
