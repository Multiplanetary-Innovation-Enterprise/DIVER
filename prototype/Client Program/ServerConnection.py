import socket

class ServerConnection():
    socket = None

    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setblocking(False)

    def connect(self):
        self.socket.connect_ex((self.host, self.port))

    def getSocket(self):
        return self.socket

    def close(self):
        self.socket.close()
        self.socket = None
