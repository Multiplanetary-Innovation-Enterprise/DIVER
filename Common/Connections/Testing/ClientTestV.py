import os
import signal
import threading
import socket

from ROVConnections.SocketWriter import SocketWriter
from ROVConnections.SocketReader import SocketReader
from ROVConnections.SocketConnection import SocketConnection

#The server connection info
port = 25003
host = "127.0.0.1"

#Listens for input from the user
def proccessInput():
    while True:
        text = input("Enter a message: ")

        socketWriter.send(text)

        #Checks if the exit command was sent
        if text == "exit":
            break

#Listens for messages from the server
def receiveMessages():
    #Continue reading until shutdown was sent
    while True:
        message = socketReader.receive()
        print("Message: " + str(message))

        #Checks if the connection was closed
        if message == "exit":
            shutdown()
            break

#Handles the shutdown process
def shutdown():
    print("Shuting down...")

    #Sends the shutdown message to the server
    socketWriter.send("exit")

    #Closes the connection with the server
    serverConnection.shutdown(socket.SHUT_WR);
    serverConnection.close()

    #Sends the interrupt signal (used to force input() to exit)
    os.kill(os.getpid(), signal.SIGINT)

#Attemps to connect to the server
serverConnection = SocketConnection(host=host, port=port)
serverConnection.connect()

#Used for reading and writing to the server
socketWriter = SocketWriter(serverConnection)
socketReader = SocketReader(serverConnection)

#Create a seperate thread for reading from the server
readThread = threading.Thread(target=receiveMessages)
readThread.start()

#Starts listening for input from the user
print("Running...")
proccessInput();
