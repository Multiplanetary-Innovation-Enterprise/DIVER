import sys
import threading
import socket

from ROVConnections.SocketWriter import SocketWriter
from ROVConnections.SocketReader import SocketReader
from ROVConnections.SocketConnection import SocketConnection

isRunning = False
port = 25003
host = "127.0.0.1"

def proccessRead():
    global isRunning

    while isRunning:
        message = socketReader.receive()
        print("Server Message: " + str(message))

        #Checks if the connection was closed
        if message == None:
            print("Exiting...")
            isRunning = False

            serverConnection.close()

    print("Read stop")

#Connect to the server
serverConnection = SocketConnection(host=host, port=port)
serverConnection.connect()

socketWriter = SocketWriter(serverConnection)
socketReader = SocketReader(serverConnection)

isRunning = True

#Create a seperate thread for reading from the server
readThread = threading.Thread(target=proccessRead)
readThread.start()

while isRunning:
    text = input("Enter a message: ")

    #Checks if the exit command was sent
    if text == "exit":
        serverConnection.shutdown(socket.SHUT_WR)
        break

    #Checks if the connections was closed while waiting
    #for user input
    if not isRunning:
        break

    socketWriter.send(text)
