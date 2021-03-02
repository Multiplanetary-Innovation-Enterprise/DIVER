import socket
import threading
import selectors

from ClientConnection import ClientConnection

class Server():
    socket = None
    isRunning = False
    clientConnection = None

    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket. SO_REUSEADDR, 1)
        self.socket.setblocking(False)
        self.socket.bind((host, port))

        self.sel = selectors.DefaultSelector()
        self.sel.register(self.socket, selectors.EVENT_READ, data=None)

    def start(self):
        print("listening for client connections")
        self.socket.listen()
        self.run()

    def run(self):
        self.isRunning = True
        clientAccepted = False

        while self.isRunning:
            events = self.sel.select(timeout=None)
            print("server running")
            for key, mask in events:
                if not clientAccepted:
                    self.acceptClientConnection(key.fileobj)
                    clientAccepted = True
                    print("client accepted")
                    break

    def stop(self):
        print("stopping server")
        self.isRunning = False
        self.socket.close()

        self.sel.unregister(self.socket)
        self.sel.close()

    def acceptClientConnection(self, client):
        clientSocket, addr = client.accept()
        self.clientConnection = ClientConnection(clientSocket)

    def getClientConnection(self):
        return self.clientConnection
