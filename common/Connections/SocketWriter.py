from SocketConnection import SocketConnection
from ClientConnection import ClientConnection
from ServerConnection import ServerConnection
from Message import Message
import pickle

class SocketWriter(Writer):
    __socket = None

    def __init__(self, socket):
        self.__socket = socket.get()

    def encode(self, message):
        return pickle.dumps(message)

    def send(self, message):
        self.__socket.send(self.encode(message))
