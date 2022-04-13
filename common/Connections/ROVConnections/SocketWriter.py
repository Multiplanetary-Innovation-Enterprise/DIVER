import struct
import pickle

from ROVMessaging.Message import Message

from ROVConnections.SocketConnection import SocketConnection
from ROVConnections.Writer import Writer

#Represents a write that utilizes a socket to send messages
class SocketWriter(Writer):
    __socket = None #The socket from the provided connection used to send messages

    def __init__(self, socketConnection:SocketConnection):
        self.__socket = socketConnection.getSocket()

    #Encodes the provided message into a byte stream that can be sent over a socket
    #connection
    def __encode(self, message:Message) -> str:
        #Converts the message to a byte stream
        serializedMessage = pickle.dumps(message);

        #Gets the size of the serialized message
        messageSize = len(serializedMessage)

        #Create the message size header
        messageHeader = struct.pack(">I", messageSize)

        #Prepend the message header and return the encoded result
        return messageHeader + serializedMessage

    #Sends the provided message over the socket connection
    def send(self, message:Message) -> None:
        print("Message Type: " + str(message.getType()))
        #Encode the message so that it can be sent
        message = self.__encode(message)

        self.__socket.sendall(message)
