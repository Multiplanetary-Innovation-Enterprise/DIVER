from ROVConnections.SocketConnection import SocketConnection
from ROVConnections.ClientConnection import ClientConnection
from ROVConnections.ServerConnection import ServerConnection
from ROVConnections.Writer import Writer
import pickle

class SocketWriter(Writer):
    __socket = None

    def __init__(self, socket):
        self.__socket = socket.get()

    def encode(self, message):
        return pickle.dumps(message)

    def send(self, message):
        self.__socket.send(self.encode(message))
