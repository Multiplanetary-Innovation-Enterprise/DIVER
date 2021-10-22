import pickle
import time
import struct
import sys
import selectors

from ROVConnections.SocketConnection import SocketConnection
from ROVConnections.ClientConnection import ClientConnection
from ROVConnections.ServerConnection import ServerConnection
from ROVConnections.Reader import Reader

from ROVMessaging.Message import Message
from ROVMessaging.MessageType import MessageType

class SocketReader(Reader):
    __socket = None
    __select = None

    def __init__(self, socket):
        self.__socket = socket.get()
        self.__socket.setblocking(True);

        # self.__select = selectors.DefaultSelector()
        # self.__select = select.register(self.__socket, selectors)


    def getSocket(self):
        return self.__socket

    def decode(self, message):
        return pickle.loads(message)

    def receive(self):
        #Reads in the header of the message first
        header = self.__socket.recv(4)

        #Gets the size of the message
        messageSize = struct.unpack(">I", header)[0]

        #Reads in the actual message based on the read in size and decodes it
        message = self.__socket.recv(messageSize)

        message = self.decode(message)

        return message
