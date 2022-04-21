#Client example using the messaging library with connection recovery

import os
import signal
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

#Listens for messages from the server
class MessageReaderTest(Subscriber):
    def recieveMessage(self, message:Message) -> None:
        print("Message Type: " + str(message.getType()))
        print("Message Contents: " + str(message.getContents()))

        #Checks if the shutdown message was recieved
        if message.getType() == MessageType.SYSTEM_STATUS and message.getContents() == SystemStatus.SHUT_DOWN:
            shutdown()

#Listens for input from the user
def processInput():
    while True:
        #Listens for user text input
        text = input("Enter a message: ")

        #Checks the user text for the message to send
        if text == "w":
            type = MessageType.ACTION
            contents = Action.MOVE_XY_FORWARD
        elif text == "s":
            type = MessageType.ACTION
            contents = Action.MOVE_XY_BACKWARD
        elif text == "sd":
            type = MessageType.SYSTEM_STATUS
            contents = SystemStatus.SHUT_DOWN
        else:
            type = MessageType.ACTION
            contents = Action.MOVE_XY_STOP

        #Checks if the system is not shutting down
        if not status == SystemStatus.SHUT_DOWN:
            message = Message(type, contents)
            outgoingMessageChannel.broadcast(message)

        #Checks if the system is shutting down or is sending the shutdown message
        if status == SystemStatus.SHUT_DOWN or (type == MessageType.SYSTEM_STATUS and contents == SystemStatus.SHUT_DOWN):
            break

#Handles the shutdown process
def shutdown():
    global status
    status = SystemStatus.SHUT_DOWN

    print("Shuting down...")

    #Sends the shutdown message to the server
    message = Message(MessageType.SYSTEM_STATUS, SystemStatus.SHUT_DOWN)
    outgoingMessageChannel.broadcast(message)

    #Closes the connection with the server
    subWriter.stop()
    serverConnection.shutdown(socket.SHUT_WR)
    serverConnection.close()

    #Sends the interrupt signal (used to force input() to exit)
    os.kill(os.getpid(), signal.SIGINT)

#The server connection info
port = 25003
host = "127.0.0.1"

#Attemps to connect to the server
serverConnection = SocketConnection(host=host, port=port)
serverConnection.connect()

#Used for reading and writing to the server
socketWriter = SocketWriter(serverConnection)
socketReader = SocketReader(serverConnection)

#Broadcasts messages sent internally to the client
subWriter = SubWriter(socketWriter)

#The message channels that be utilized to send messages
incomingMessageChannel = MessageChannel()
outgoingMessageChannel = MessageChannel()

#Listens for messages that are broadcasted internally
messageReaderTest = MessageReaderTest()

#Rebroadcasts messages recieved from the server internally
pubListener = PubListener(socketReader, incomingMessageChannel)
pubListener.listen()

#Registers all of the subscribers to the message types that they are interested in
outgoingMessageChannel.subscribe(MessageType.ACTION, subWriter)
outgoingMessageChannel.subscribe(MessageType.SYSTEM_STATUS, subWriter)
incomingMessageChannel.subscribe(MessageType.ACTION, messageReaderTest)
incomingMessageChannel.subscribe(MessageType.SYSTEM_STATUS, messageReaderTest)

#The status the system is currently in
status = SystemStatus.RUNNING

#The contents and message type of the message to send
contents = None
type = None

print("Running")
processInput()


#Stops listening for messages from the server
pubListener.stop()
