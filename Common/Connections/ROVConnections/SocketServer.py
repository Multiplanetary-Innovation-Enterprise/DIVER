import socket

from ROVConnections.ClientConnection import *

class SocketServer():
    __socket = None
    __host = None
    __port = None

    def __init__(self, host, port):
        self.__host = host
        self.__port = port

        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.setsockopt(socket.SOL_SOCKET, socket. SO_REUSEADDR, 1)
        self.__socket.bind((host, port))

    def getHost(self):
        return self.__host

    def getPort(self):
        return self.__port

    def getClientConnection(self) -> ClientConnection:
        self.__socket.listen()
        clientSocket, clientAddr = self.__socket.accept()
        clientConnection = ClientConnection(clientSocket, clientAddr)

        return clientConnection

    def stop(self):
        self.__socket.close()
        self.__socket = None
