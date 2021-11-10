import socket as sock

from ROVConnections.Connection import Connection

#Represents a connection made using a socket to the socket based server
class SocketConnection(Connection):
    __socket = None    #The socket corresponding to this connection
    __host:str = None  #The host or host name for the socket to connect to
    __port:int = None  #The port for the socket to connect to

    def __init__(self, socket=None, host:str=None, port:int=None):
        print("TEst using new code");
        #Checks if a socket was provided
        if socket is None:
            #Creates a network socket, since one was not provided
            self.__socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
            self.__host = host
            self.__port = port
        else:
            #Uses the provided socket and gets its host and port
            self.__socket = socket
            self.__host = socket.getsockname()[0]
            self.__port = socket.getsockname()[1]

    #Connects to the socket based server
    def connect(self) -> None:
        self.__socket.connect((self.__host, self.__port))

    #Gets the socket corresponding to this connection
    def getSocket(self):
        return self.__socket

    #Gets the host that the socket is connected to
    def getHost(self) -> str:
        return self.__host

    #Gets the port that the socket is connected to
    def getPort(self) -> int:
        return self.__port

    #Closes the connection
    def close(self) -> None:
        #Closes the socket
        self.__socket.close();
