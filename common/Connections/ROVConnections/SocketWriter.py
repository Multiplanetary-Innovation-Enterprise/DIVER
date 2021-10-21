import sys
import struct
import pickle

from ROVConnections.SocketConnection import SocketConnection
from ROVConnections.ClientConnection import ClientConnection
from ROVConnections.ServerConnection import ServerConnection
from ROVConnections.Writer import Writer

class SocketWriter(Writer):
    __socket = None

    def __init__(self, socket):
        self.__socket = socket.get()

    def encode(self, message):
        messageSize = sys.getsizeof(message)

        #Create the message size header
        messageHeader = struct.pack(">I", messageSize)

        #Converts the message to a byte stream
        serializedMessage = pickle.dumps(message);

        #Prepend the message header and return the encoded result
        return messageHeader + serializedMessage

    def send(self, message):
        #Encode the message so that it can be sent
        message = self.encode(message)

        #Send the actual message
        self.__socket.sendall(message)
