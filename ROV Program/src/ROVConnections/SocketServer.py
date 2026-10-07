import socket

from ROVConnections.Server import *
from ROVConnections.SocketConnection import *

#This class represents a server that is implmented using socket based communication
class SocketServer(Server):
    __socket = None   #The socket listening for client connection requests
    __host:str = None #The host or host name for the socket to connect to
    __port:int = None #The port for the socket to connect to

    def __init__(self, host:str, port:int):
        self.__host = host
        self.__port = port

        #Configures the socket to listen for client connection requests using a
        #TCP socket at the provided host name and port
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__socket.bind((host, port))
        self.__socket.listen()

    #Gets the host that the socket is connected to
    def getHost(self) -> str:
        return self.__host

    #Gets the port that the socket is connected to
    def getPort(self) -> int:
        return self.__port

    #Waits for a client connection request and returns the connection upon
    #acceptance of the connection
    def getClientConnection(self) -> SocketConnection:
        clientSocket, clientAddress = self.__socket.accept()
        clientConnection = SocketConnection(clientSocket, clientAddress[0], clientAddress[1])

        return clientConnection

    #Stops the server listening from listening for new client connection requests
    def stop(self) -> None:
        self.__socket.close()
        self.__socket = None
