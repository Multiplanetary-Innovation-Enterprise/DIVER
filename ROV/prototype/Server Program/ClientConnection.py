import socket

class ClientConnection():
    socket = None

    def __init__(self, socket):
        self.socket = socket
        self.socket.setblocking(False)

    def getSocket(self):
        return self.socket

    def close(self):
        print("closing client connection")
        self.socket.close()
        self.socket = None
