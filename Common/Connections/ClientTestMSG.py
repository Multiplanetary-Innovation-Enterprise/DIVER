import socket

from ROVMessaging.MessageChannel import *
from ROVMessaging.MessageType import *
from ROVMessaging.Action import *
from ROVMessaging.Subscriber import *
from ROVMessaging.Message import *
from ROVMessaging.SystemStatus import *

from ROVConnections.SocketWriter import *
from ROVConnections.SubWriter import *
from ROVConnections.SocketReader import *
from ROVConnections.SocketConnection import *
from ROVConnections.PubListener import *

class MessageReaderTest(Subscriber):
    def recieveMessage(self, message:Message) -> None:
        print("Message Type: " + str(message.getType()))
        print("Message Contents: " + str(message.getContents()))

        if message.getType() == MessageType.SYSTEM_STATUS and message.getContents() == SystemStatus.SHUT_DOWN:
            shutdown()

def shutdown():
    global status
    status = SystemStatus.SHUT_DOWN

    print("Shuting down")
    pubListener.stop()

    #Sends the shutdown message to the client
    message = Message(MessageType.SYSTEM_STATUS, SystemStatus.SHUT_DOWN)
    outgoingMessageChannel.broadcast(message)

    serverConnection.shutdown(socket.SHUT_WR)
    serverConnection.close()
    print("Press enter to exit")


port = 25003
host = "127.0.0.1"

#Connect to the server
serverConnection = SocketConnection(host=host, port=port)
serverConnection.connect()

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
status = SystemStatus.RUNNING

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
        isRunning = False

        type = MessageType.SYSTEM_STATUS
        contents = SystemStatus.SHUT_DOWN
    else:
        type = MessageType.ACTION
        contents = Action.MOVE_XY_STOP

    #Checks if the shutdown command was sent locally or
    #from the server
    if not status == SystemStatus.SHUT_DOWN and isRunning:
        message = Message(type, contents)
        outgoingMessageChannel.broadcast(message)
    else:
        break
