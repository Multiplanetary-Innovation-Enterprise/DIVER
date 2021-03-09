from SocketWriter import SocketWriter
from SocketReader import SocketReader
from ClientConnection import ClientConnection
from Message import Message

c = ClientConnection(25566)

c.listenAndAccept(60)
cs = SocketReader(c.client())

while True:
    message = cs.receive()
    if (message != ''):
        print(message.message())
