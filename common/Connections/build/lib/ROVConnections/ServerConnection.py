import socket

from ROVConnections.SocketConnection import SocketConnection

class ServerConnection(SocketConnection):
    __host = None
    __port = None

    def __init__(self, host, port):
        self.__host = host
        self.__port = port

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))

        super().__init__(sock)

    def getHost(self):
        return self.__host

    def getPort(self):
        return self.__port
