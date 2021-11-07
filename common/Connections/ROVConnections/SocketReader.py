import pickle
import struct
import selectors

from ROVMessaging.Message import Message

from ROVConnections.SocketConnection import SocketConnection
from ROVConnections.Reader import Reader

#Represents a reader that utilizes a socket to recieve messages
class SocketReader(Reader):
    __socket = None #The socket from the provided socket connection
    __select = None #The selector attached to the socket

    def __init__(self, socketConnection:SocketConnection):
        #Gets the socket and sets it a blocking read
        self.__socket = socketConnection.getSocket()
        self.__socket.setblocking(True);

        #Sets the socket to a blocking read until a message is recieved or a
        #disconnect occurs
        self.__select = selectors.DefaultSelector()
        self.__select.register(self.__socket, selectors.EVENT_READ)

    #Converts the byte stram encode message back to the orignal message
    def decode(self, encodedMsg:str) -> Message:
        return pickle.loads(encodedMsg)

    #Recives a message from the socket
    def receive(self) -> Message:
        print("Waiting.....")
        #Waits for a new message or socket disconnect
        events = self.__select.select(timeout=None)
        print("Data!")

        #Iterates through any events that just occured
        for key, mask in events:
            #Check if the socket was closed
            if key.fileobj.fileno() < 0:
                return None

            print(key)
            print(type(key))
            print(key.fileobj)
            print(key.fileobj.fileno())

            print(mask)
            print(type(mask))

        #Reads in the header of the message first
        header = self.__socket.recv(4)

        #Gets the size of the message
        messageSize = struct.unpack(">I", header)[0]

        #Reads in the actual message based on the read in size and decodes it
        message = self.__socket.recv(messageSize)

        #Converts the encoded message back to the orginal message
        message = self.decode(message)

        return message
