import socket

class ClientConnection():
    socket = None

    def __init__(self, socket):
        self.socket = socket
        self.socket.setblocking(False)

    def getSocket(self):
        return self.socket

    def close(self):
        self.socket.close()
        self.socket = None
