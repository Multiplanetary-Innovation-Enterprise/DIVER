from ROVConnections.SocketWriter import SocketWriter
from ROVConnections.SocketReader import SocketReader
from ROVConnections.ServerConnection import ServerConnection
from ROVConnections.PubListener import PubListener
from ROVConnections.SubWriter import SubWriter

from ROVMessaging.MessageChannel import *
from ROVMessaging.MessageType import *

from input.KeyboardInput import KeyboardInput

import tkinter as tk

#Connection info for connecting to the ROV
port = 25003
host = "127.0.0.1" #raspberrypi

#Attempts to connect to the ROV
serverConnection = ServerConnection(host, port)
serverConnection.connect()

#The sending and receiving message channels
incomingMessageChannel = MessageChannel()
outgoingMessageChannel = MessageChannel()

#Sets up ability to send messages to the ROV
socketWriter = SocketWriter(serverConnection)
subWriter = SubWriter(socketWriter)

#Sets up the abilty to recieve messages from the ROV
socketReader = SocketReader(serverConnection)
pubListener = PubListener(socketReader, incomingMessageChannel)

keyboardInput = KeyboardInput(outgoingMessageChannel)

#Start listening for messages from the ROV
pubListener.listen()

#Allows the client to send action and system status messages to the ROV
outgoingMessageChannel.subscribe(MessageType.ACTION, subWriter)
outgoingMessageChannel.subscribe(MessageType.SYSTEM_STATUS, subWriter)

window = tk.Tk()
window.mainloop()

serverConnection.close()
print("Exiting...")
