from ROVConnections.SocketWriter import *
from ROVConnections.SocketReader import *
from ROVConnections.ClientConnection import *
from ROVConnections.SubWriter import *
from ROVConnections.PubListener import *
from ROVConnections.Server import *

from ROVMessaging.Subscriber import *
from ROVMessaging.Message import *
from ROVMessaging.MessageType import *

class TestSubscriber(Subscriber):
    def recieveMessage(self, message:Message) -> None:
        print("Recieved: " + str(message.getContents()))

class ShutdownHandler(Subscriber):
    def recieveMessage(self, message:Message) -> None:

        if message.getContents() != SystemStatus.SHUT_DOWN:
            return

        print("Shuting down...")

        pubListener.stop()
        clientConnection.close()
        server.stop()

#Server code -----------------------------------
server = Server("127.0.0.1", 25003)

print("Waiting for client connection")
clientConnection = server.getClientConnection()

messageChannel = MessageChannel()

messageChannel.subscribe(MessageType.ACTION, TestSubscriber())
messageChannel.subscribe(MessageType.SYSTEM_STATUS, ShutdownHandler())

socketReader = SocketReader(clientConnection.getSocket())
pubListener = PubListener(socketReader, messageChannel)

pubListener.listen()

print("Shutdown Complete")
