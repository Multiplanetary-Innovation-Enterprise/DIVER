import threading

from ROVConnections.SocketWriter import *
from ROVConnections.SocketReader import *
from ROVConnections.ClientConnection import *

isRunning = True

def proccessInput():
    global isRunning

    while isRunning:
        text = input("Enter a message: ")
        print(text)

        socketWriter.send(text)

    print("Write stop")

port = 25003

clientConnection = ClientConnection(port)

clientConnection.listenAndAccept(10)

socketReader = SocketReader(clientConnection.client())
socketWriter = SocketWriter(clientConnection.client())

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

clientConnection.client().close()
print("Exiting...")
