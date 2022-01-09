import threading

from ROVMessaging.MessageChannel import *
from ROVMessaging.MessageType import *
from ROVMessaging.Action import *
from ROVMessaging.SystemStatus import *

from ROVConnections.SocketWriter import *
from ROVConnections.SubWriter import *
from ROVConnections.SocketReader import *
from ROVConnections.SocketServer import *
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

    print("Shuting down...")
    pubListener.stop()
    server.stop()

    #Sends the shutdown message to the client
    message = Message(MessageType.SYSTEM_STATUS, SystemStatus.SHUT_DOWN)
    outgoingMessageChannel.broadcast(message)

    clientConnection.shutdown(socket.SHUT_WR)
    clientConnection.close()
    print("Press enter to exit")

port = 25003

server = SocketServer('', port)

clientConnection = server.getClientConnection()

incomingMessageChannel = MessageChannel()
outgoingMessageChannel = MessageChannel()

messageReaderTest = MessageReaderTest()

socketReader = SocketReader(clientConnection)
socketWriter = SocketWriter(clientConnection)
subWriter = SubWriter(socketWriter)

pubListener = PubListener(socketReader, incomingMessageChannel)
pubListener.listen()

incomingMessageChannel.subscribe(MessageType.ACTION, messageReaderTest)
incomingMessageChannel.subscribe(MessageType.SYSTEM_STATUS, messageReaderTest)
outgoingMessageChannel.subscribe(MessageType.ACTION, subWriter)
outgoingMessageChannel.subscribe(MessageType.SYSTEM_STATUS, subWriter)

isRunning = True
status = SystemStatus.RUNNING

print("Running...")

while isRunning:
    text = input("Enter a status: ")

    if text == "a":
        action = SystemStatus.ARMED
    elif text == "sd":
        isRunning = False
        action = SystemStatus.SHUT_DOWN
    else:
        action = SystemStatus.INITIALIZING

    #Checks if the shutdown command was sent locally or
    #from the server
    if not status == SystemStatus.SHUT_DOWN and isRunning:
        message = Message(type, contents)
        outgoingMessageChannel.broadcast(message)
    else:
        break
