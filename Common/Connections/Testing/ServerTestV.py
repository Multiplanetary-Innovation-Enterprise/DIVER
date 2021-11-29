import threading

from ROVConnections.SocketWriter import *
from ROVConnections.SocketReader import *
from ROVConnections.SocketServer import *

isRunning = True

def proccessInput():
    global isRunning

    while isRunning:
        text = input("Enter a message: ")
        print(text)

        socketWriter.send(text)

    print("Write stop")

server = SocketServer('', 25003);

clientConnection = server.getClientConnection()

socketReader = SocketReader(clientConnection)
socketWriter = SocketWriter(clientConnection)

#Create a seperate thread for writing to the client
writeThread = threading.Thread(target=proccessInput)
writeThread.start()

print("Running...")

while isRunning:
    message = socketReader.receive()
    print("Client Message: " + str(message))

    if message == "exit":
        socketWriter.send("exit")
        isRunning = False

clientConnection.close()
print("Exiting...")
