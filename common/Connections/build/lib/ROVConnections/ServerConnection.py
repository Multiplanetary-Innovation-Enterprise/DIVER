import socket

from ROVConnections.SocketConnection import SocketConnection

class ServerConnection(SocketConnection):
    def __init__(self, host, port):
        super().__init__(host=host, port=port)

    def connect(self):
        self.getSocket().connect((self.getHost(), self.getPort()))
