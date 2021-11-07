import socket

from ROVConnections.SocketConnection import SocketConnection

#Represents the connection used by the client to connect to the server
class ServerConnection(SocketConnection):
    def __init__(self, host:str, port:int):
        super().__init__(host=host, port=port)

    #Gets the underlying socket connection and attempts to connect to the server
    def connect(self) -> None:
        self.getSocket().connect((self.getHost(), self.getPort()))
