import socket

from ROVConnections.SocketConnection import SocketConnection

class ServerConnection(SocketConnection):
    __host = None
    __port = None

    def __init__(self, host, port):
        super().__init__()
        self.__host = host
        self.__port = port
        self.get().connect((host, port))

    def getHost(self):
        return self.__host

    def getPort(self):
        return self.__port
