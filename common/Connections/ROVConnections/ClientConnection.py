from ROVConnections.SocketConnection import SocketConnection
from socket import *

class ClientConnection(SocketConnection):
    __clientSocketConnection = None

    def __init__(self, host, port):
        super().__init__(host=host, port=port)

        self.getSocket().setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.getSocket().bind((self.getHost(), self.getPort()))

    def getClient(self):
        return self.__clientSocketConnection

    def listenAndAccept(self, backlogSize):
        self.getSocket().listen(backlogSize)

        clientSocket, clientAddress = self.getSocket().accept()

        self.__clientSocketConnection = SocketConnection(clientSocket, clientAddress[0], clientAddress[1])
