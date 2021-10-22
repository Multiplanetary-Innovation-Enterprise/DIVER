import socket

from ROVMessaging.MessageChannel import *
from ROVMessaging.MessageType import *
from ROVMessaging.Action import *
from ROVMessaging.Subscriber import *
from ROVMessaging.Message import *
from ROVMessaging.SystemStatus import *

from SocketWriter import SocketWriter
from SubWriter import SubWriter
from SocketReader import SocketReader
from ServerConnection import ServerConnection
from PubListener import PubListener

class MessageReaderTest(Subscriber):
    def recieveMessage(self, message:Message) -> None:
        print("Message Type: " + str(message.getType()))
        print("Message Contents: " + str(message.getContents()))

port = 25003
host = "127.0.0.1"

#Connect to the server
serverConnection = ServerConnection(host, port)

socketWriter = SocketWriter(serverConnection)
socketReader = SocketReader(serverConnection)

subWriter = SubWriter(socketWriter)

incomingMessageChannel = MessageChannel()
outgoingMessageChannel = MessageChannel()

messageReaderTest = MessageReaderTest()

outgoingMessageChannel.subscribe(MessageType.ACTION, subWriter)
outgoingMessageChannel.subscribe(MessageType.SYSTEM_STATUS, subWriter)
incomingMessageChannel.subscribe(MessageType.ACTION, messageReaderTest)
incomingMessageChannel.subscribe(MessageType.SYSTEM_STATUS, messageReaderTest)

pubListener = PubListener(socketReader, incomingMessageChannel)
pubListener.listen()

isRunning = True
contents = None
type = None

while isRunning:
    text = input("Enter a message: ")

    if text == "w":
        type = MessageType.ACTION
        contents = Action.MOVE_XY_FORWARD
    elif text == "s":
        type = MessageType.ACTION
        contents = Action.MOVE_XY_BACKWARD
    elif text == "sd":
        type = MessageType.SYSTEM_STATUS
        contents = SystemStatus.SHUT_DOWN

        pubListener.stop()
        isRunning = False
    else:
        type = MessageType.ACTION
        contents = Action.MOVE_XY_STOP

    message = Message(type, contents)
    outgoingMessageChannel.broadcast(message)

serverConnection.get().shutdown(socket.SHUT_RDWR)
print("Exiting...")
