import tkinter as tk

from ROVConnections.SocketWriter import SocketWriter
from ROVConnections.SocketReader import SocketReader
from ROVConnections.SocketConnection import SocketConnection
from ROVConnections.PubListener import PubListener
from ROVConnections.SubWriter import SubWriter

from ROVMessaging.MessageChannel import *
from ROVMessaging.MessageType import *

from input.KeyboardInput import KeyboardInput
from loggers.DataLogger import DataLogger

#Connection info for connecting to the ROV
port = 25003
host = "127.0.0.1" #127.0.0.1 raspberrypi

#Attempts to connect to the ROV
serverConnection = SocketConnection(host=host, port=port)
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

dataLogger = DataLogger()
dataLogger.openFile("..\logs\data\data_log");

#Allows the client to send action and system status messages to the ROV
outgoingMessageChannel.subscribe(MessageType.ACTION, subWriter)
outgoingMessageChannel.subscribe(MessageType.SYSTEM_STATUS, subWriter)

incomingMessageChannel.subscribe(MessageType.SENSOR_DATA, dataLogger)

#GUI stuff to move to seperate class later
window = tk.Tk()
window.mainloop()

serverConnection.close()
dataLogger.close()

print("Exiting...")
