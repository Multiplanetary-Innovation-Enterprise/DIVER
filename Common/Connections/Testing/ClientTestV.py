import sys
import threading


from ROVConnections.SocketWriter import SocketWriter
from ROVConnections.SocketReader import SocketReader
from ROVConnections.ServerConnection import ServerConnection

isRunning = False
port = 25003
host = "127.0.0.1"

def proccessRead():
    global isRunning

    while isRunning:
        message = socketReader.receive()
        print("Server Message: " + str(message))

        if message == "exit":
            isRunning = False

    print("Read stop")

#Connect to the server
serverConnection = ServerConnection(host, port)
serverConnection.connect()

socketWriter = SocketWriter(serverConnection)
socketReader = SocketReader(serverConnection)

isRunning = True

#Create a seperate thread for reading from the server
readThread = threading.Thread(target=proccessRead)
readThread.start()

while isRunning:
    text = input("Enter a message: ")
    socketWriter.send(text)

serverConnection.close()
print("Exiting...")
