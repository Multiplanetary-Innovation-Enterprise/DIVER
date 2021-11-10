from socket import *

from ROVConnections.SocketConnection import SocketConnection

#This is the connection used by the server to listen for a client connection
class ClientConnection(SocketConnection):
    #The socket connection that is used to communicate with the client program
    __clientSocketConnection:SocketConnection = None

    def __init__(self, host:str, port:int):
        super().__init__(host=host, port=port)

        #Sets up the listening socket for client program to connect to
        self.getSocket().setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.getSocket().bind((self.getHost(), self.getPort()))

    #Gets the client socket connection
    def getClient(self) -> SocketConnection:
        return self.__clientSocketConnection

    #Used by the server to listen for the client program and accept its connection
    #request, once recieved
    def listenAndAccept(self, backlogSize:int) -> None:
        #Waits for the client's connection request
        self.getSocket().listen(backlogSize)

        #Accepts the client's connect request
        clientSocket, clientAddress = self.getSocket().accept()

        #Creates the client socket connection from the provided data
        self.__clientSocketConnection = SocketConnection(clientSocket, clientAddress[0], clientAddress[1])
