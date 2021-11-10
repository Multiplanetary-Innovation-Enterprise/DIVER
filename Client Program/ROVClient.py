import csv

from ROVConnections.SocketWriter import SocketWriter
from ROVConnections.SocketReader import SocketReader
from ROVConnections.ServerConnection import ServerConnection
from ROVConnections.PubListener import PubListener
from ROVConnections.SubWriter import SubWriter

from ROVMessaging.MessageChannel import *
from ROVMessaging.MessageType import *
from ROVMessaging.Subscriber import Subscriber

from input.KeyboardInput import KeyboardInput

import tkinter as tk

#Temporary for testing
class TempLogger(Subscriber):
    __file = None
    __writer = None

    def __init__(self):
        header = ["time", "temperature"];
        self.__file = open("ROV_Temp_Data.csv", "w+");

        self.__writer = csv.writer(self.__file)
        self.__writer.writerow(header)


    def recieveMessage(self, message:Message) -> None:
        print("Sensor data recieved")
        temp = message.getContents()['internalTemp']
        time = message.getContents()['time']

        print("Temp: " + str(temp) + " F @ Time: " + str(time) + "sec")
        #write entry to csv file
        self.__writer.writerow([time, temp])

#Connection info for connecting to the ROV
port = 25003
host = "raspberrypi" #127.0.0.1

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

tempLogger = TempLogger()

#Allows the client to send action and system status messages to the ROV
outgoingMessageChannel.subscribe(MessageType.ACTION, subWriter)
outgoingMessageChannel.subscribe(MessageType.SYSTEM_STATUS, subWriter)

incomingMessageChannel.subscribe(MessageType.SENSOR_DATA, tempLogger)

window = tk.Tk()
window.mainloop()

serverConnection.close()
print("Exiting...")
