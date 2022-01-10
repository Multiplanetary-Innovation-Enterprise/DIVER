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
    def __decode(self, encodedMsg:str) -> Message:
        return pickle.loads(encodedMsg)

    #Recives a message from the socket
    def receive(self) -> Message:
        #Waits for a new message or socket disconnect
        events = self.__select.select(timeout=None)

        #The message header
        header = bytearray()
        headerSize = 0

        #Reads in the header of the message first
        while headerSize < 4:
            #Reads in the necessary bytes (up to 4 to finish reading in the header)
            data = self.__socket.recv(4 - headerSize)
            dataSize = len(data)

            #If nothing was read in then the connection was closed, so exit
            if dataSize == 0:
                return None

            #Updates the header
            header += data
            headerSize += dataSize

        #Gets the size of the message
        messageTotalSize = struct.unpack(">I", header)[0]

        #The byte string message read in
        message = bytearray()
        messageSize = 0

        #Reads in the actual message based on the read in size and decodes it
        while messageSize < messageTotalSize:
            #Reads in the necessary bytes to finish reading in the message
            data = self.__socket.recv(messageTotalSize - messageSize)

            #Updates the message
            message += data
            messageSize += len(data)

        #Converts the encoded message back to the orginal message
        message = self.__decode(message)

        return message
