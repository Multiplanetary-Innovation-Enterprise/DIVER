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
        global isRunning
        print("Message Type: " + str(message.getType()))
        print("Message Contents: " + str(message.getContents()))

        if message.getType() == MessageType.SYSTEM_STATUS and message.getContents() == SystemStatus.SHUT_DOWN:
            print("Shuting down")
            isRunning = False
            pubListener.stop()

            print("Still runin? : " + str(isRunning))

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
print("Running...")

while isRunning:
    text = input("Enter a status: ")

    print("Still runin? : " + str(isRunning))

    if text == "a":
        action = SystemStatus.ARMED
    elif text == "s":
        action = SystemStatus.SHUT_DOWN
    else:
        action = SystemStatus.INITIALIZING

    message = Message(MessageType.SYSTEM_STATUS, action)
    outgoingMessageChannel.broadcast(message)

clientConnection.getClient().close()
print("Exiting...")
