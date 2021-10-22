from ROVConnections.SocketWriter import SocketWriter
from ROVConnections.SocketReader import SocketReader
from ROVConnections.ServerConnection import ServerConnection
from ROVConnections.PubListener import PubListener
from ROVConnections.SubWriter import SubWriter

from ROVMessaging.Publisher import *
from ROVMessaging.Message import *
from ROVMessaging.MessageChannel import *
from ROVMessaging.MessageType import *
from ROVMessaging.SystemStatus import *

from input.KeyboardInput import KeyboardInput


import time
import sys

port = 25003
# host = sys.argv[1]

# serverConnection = ServerConnection(host, port)
# socketWriter = SocketWriter(serverConnection)
# subWriter = SubWriter(socketWriter)

mc = MessageChannel()
kb = KeyboardInput(mc)
pub = PubListener(None, mc)
#pub.listen()

mc.subscribe(MessageType.ACTION, subWriter)
mc.subscribe(MessageType.SYSTEM_STATUS, subWriter)

while (True):
    pass

# for i in range(10):
#     message = Message(MessageType.ACTION, "this is an action message")
#     print(f"Message: {message.getContents()}")
#     pub.sendMessage(message, mc)
#     time.sleep(1)
# # message = Message("this is a message")

# print("Send close message")
# message = Message(MessageType.SYSTEM_STATUS, SystemStatus.SHUT_DOWN)
# pub.sendMessage(message, mc)
# serverConnection.getSocket().close()
