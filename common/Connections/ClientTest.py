from SocketWriter import SocketWriter
from SocketReader import SocketReader
from ServerConnection import ServerConnection
from ROVMessaging.Publisher import *
from ROVMessaging.Message import *
from ROVMessaging.MessageChannel import *
from ROVMessaging.MessageType import *
from SubWriter import SubWriter
from PubListener import PubListener
import time
import sys

port = 25003
host = sys.argv[1]
# foundPort = False
# while not foundPort:
#     try:
#         s = ServerConnection('localhost', port)
#         foundPort = True
#     except:
#         port += 1

s = ServerConnection(host, port)
w = SocketWriter(s)
sub = SubWriter(w)
mc = MessageChannel()
pub = PubListener(None, mc)
bool = mc.subscribe(MessageType.ACTION, sub)
print(f"bool: {bool}")
for i in range(10):
    message = Message(MessageType.ACTION, "this is an action message")
    print(f"Message: {message.getContents()}")
    pub.sendMessage(message, mc)
    time.sleep(1)
# message = Message("this is a message")
message = Message(MessageType.ACTION, "Shutdown")
pub.sendMessage(message, mc)
s.close()
