import threading
import socket as sock

from ROVConnections.SocketWriter import *
from ROVConnections.SocketReader import *
from ROVConnections.SocketServer import *

isRunning = True

def proccessInput():
    global isRunning

    while isRunning:
        text = input("Enter a message: ")
        print(text)

         #Checks if the shutdown message was send
        if text == "exit":
            clientConnection.shutdown(sock.SHUT_WR)
            break

        #Checks if the connections was closed while waiting
        #for user input
        if not isRunning:
            break

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

    #Checks if the connection was closed
    if message == None:
        print("Exiting...")
        isRunning = False

        server.stop()
        clientConnection.shutdown(socket.SHUT_WR);
        clientConnection.close()

        print("Press enter to exit")
        break
