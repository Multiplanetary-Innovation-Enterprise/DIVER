import os
import signal
import threading
import socket as sock

from ROVConnections.SocketWriter import *
from ROVConnections.SocketReader import *
from ROVConnections.SocketServer import *

#Listens for input from the user
def proccessInput():
    while True:
        text = input("Enter a message: ")

        socketWriter.send(text)

        #Checks if the shutdown message was send
        if text == "exit":
            break

#Recieves messages from the client
def receiveMessages():
    while True:
        message = socketReader.receive()
        print("Client Message: " + str(message))

        #Checks if the connection was closed
        if message == 'exit':
            shutdown()
            break

#Handles the shutdown process
def shutdown():
    print("Shuting down...")

    #Stops accepting new client connection requests
    server.stop()

    #Sends the shutdown message to the client
    socketWriter.send("exit")

    #Closes the connection with the client
    clientConnection.shutdown(socket.SHUT_WR);
    clientConnection.close()

    #Sends the interrupt signal (used to force input() to exit)
    os.kill(os.getpid(), signal.SIGINT)

#Starts the server at the designated port
server = SocketServer('', 25003);

#Waits for the client program to connect
clientConnection = server.getClientConnection()

#Used for reading and writing to the client
socketReader = SocketReader(clientConnection)
socketWriter = SocketWriter(clientConnection)

#Create a seperate thread for reading from the client
readThread = threading.Thread(target=receiveMessages)
readThread.start()

#Starts listening for input from the user
print("Running...")
proccessInput();
