import socket as sock

class SocketConnection():
    __socket = None
    __host = None
    __port = None

    def __init__(self, socket=None, host=None, port=None):
        if socket is None:
            self.__socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
            self.__host = host
            self.__port = port
        else:
            self.__socket = socket
            self.__host = socket.getsockname()[0]
            self.__port = socket.getsockname()[1]

    def getSocket(self):
        return self.__socket

    def getHost(self):
        return self.__host

    def getPort(self):
        return self.__port

    def close(self):
        self.__socket.close();
