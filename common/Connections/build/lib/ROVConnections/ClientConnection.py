from ROVConnections.SocketConnection import SocketConnection

class ClientConnection(SocketConnection):
    __port = None
    __clientSocket = None
    __clientAddress = None

    def __init__(self, port):
        super().__init__()
        self.__port = port
        self.get().bind(('', port))

    def getPort(self):
        return self.__port

    def client(self):
        return self.__clientSocket

    def claddr(self):
        return self.__clientAddress

    def listenAndAccept(self, seconds):
        self.get().listen(seconds)
        connection, address = self.get().accept()
        self.__clientSocket = SocketConnection(connection)
        self.__clientAddress = address

    def close(self):
        self.__clientSocket.close()
