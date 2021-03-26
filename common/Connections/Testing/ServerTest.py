from ROVConnections.SocketWriter import *
from ROVConnections.SocketReader import *
from ROVConnections.ClientConnection import *
from ROVConnections.SubWriter import *
from ROVConnections.PubListener import *
from ROVMessaging.Publisher import *
from ROVMessaging.Message import *
from ROVMessaging.MessageChannel import *


port = 25003
# foundPort = False
# while not foundPort:
#     try:
#         c = ClientConnection(port)
#         foundPort = True
#     except:
#         port += 1

c = ClientConnection(port)
c.listenAndAccept(10)
cs = SocketReader(c.client())



noneCount = 0 #timeout counter
timeout = 6

while True:

    message = cs.receive()
    
    if (message != None):
        print(message.getContents())
        if (message.getContents() == "Shutdown"):
            cs.getSocket().close()
            print("listening")
            c.listenAndAccept(5)
            cs = SocketReader(c.client())
        noneCount = 0
            # cs = SocketReader(c.client())
            # noneCount = 0
        # if (message.getContents() == "Shutdown"):
        #     c.close()
        #     exit(0)
    else:
        noneCount += 1
        print("None!")
    if (noneCount >= timeout):
        c.close()
        exit(0)
