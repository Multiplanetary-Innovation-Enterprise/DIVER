import os
import signal
import socket
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

#Listens for messages from the client
class MessageReaderTest(Subscriber):
    def recieveMessage(self, message:Message) -> None:
        print("Message Type: " + str(message.getType()))
        print("Message Contents: " + str(message.getContents()))

        #Checks if the shutdown message was recieved
        if message.getType() == MessageType.SYSTEM_STATUS and message.getContents() == SystemStatus.SHUT_DOWN:
            shutdown()

#Handles the shutdown process
def shutdown():
    global status
    status = SystemStatus.SHUT_DOWN

    print("Shuting down...")

    #Stops listening for messages from the client and stops accept new client
    #connection requests
    pubListener.stop()
    server.stop()

    #Sends the shutdown message to the client
    message = Message(MessageType.SYSTEM_STATUS, SystemStatus.SHUT_DOWN)
    outgoingMessageChannel.broadcast(message)

    #Closes the connection with the client
    clientConnection.shutdown(socket.SHUT_WR)
    clientConnection.close()

    #Sends the interrupt signal (used to force input() to exit)
    os.kill(os.getpid(), signal.SIGINT)

#The port that the server listens to for new connection requests
port = 25003

#Starts the server at the designated port
server = SocketServer('', port)

#Waits for the client program to connect
clientConnection = server.getClientConnection()

#Used for reading and writing to the client
socketReader = SocketReader(clientConnection)
socketWriter = SocketWriter(clientConnection)

#Broadcasts messages sent internally to the client
subWriter = SubWriter(socketWriter)

#Listens for messages that are broadcasted internally
messageReaderTest = MessageReaderTest()

#The message channels that be utilized to send messages
incomingMessageChannel = MessageChannel()
outgoingMessageChannel = MessageChannel()

#Rebroadcasts messages recieved from the client internally
pubListener = PubListener(socketReader, incomingMessageChannel)
pubListener.listen()

#Registers all of the subscribers to the message types that they are interested in
incomingMessageChannel.subscribe(MessageType.ACTION, messageReaderTest)
incomingMessageChannel.subscribe(MessageType.SYSTEM_STATUS, messageReaderTest)
outgoingMessageChannel.subscribe(MessageType.ACTION, subWriter)
outgoingMessageChannel.subscribe(MessageType.SYSTEM_STATUS, subWriter)

#The status the system is currently in
status = SystemStatus.RUNNING
print("Running...")

#Listens for text input from the user
while True:
    #Listens for user text input
    text = input("Enter a status: ")

    #Checks the user text for the message to send
    if text == "a":
        action = SystemStatus.ARMED
    elif text == "sd":
        action = SystemStatus.SHUT_DOWN
    else:
        action = SystemStatus.INITIALIZING

    #Checks if the system is not shutting down
    if not status == SystemStatus.SHUT_DOWN:
        message = Message(MessageType.SYSTEM_STATUS, action)
        outgoingMessageChannel.broadcast(message)

    #Checks if the system is shutting down or is sending the shutdown message
    if status == SystemStatus.SHUT_DOWN or action == SystemStatus.SHUT_DOWN:
        break
