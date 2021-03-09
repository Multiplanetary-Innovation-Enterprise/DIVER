from SocketWriter import SocketWriter
from SocketReader import SocketReader
from ServerConnection import ServerConnection
from Message import Message

s = ServerConnection('localhost', 25566)
w = SocketWriter(s)
message = Message("this is a message")
w.send(message)
