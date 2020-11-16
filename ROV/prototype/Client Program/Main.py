from ServerConnection import ServerConnection
from SocketListener import SocketListener
from SocketWriter import SocketWriter

import threading

def close():
    print("stopping listener")
    socketListener.stop()

    print("closing")
    connection.close()

def process():
    print("running")
    isRunning = True

    while isRunning:
        message = input()
        socketWriter.write(message)

        if message == "close":
            print("closing....")
            #isRunning = False
            #close()

HOST = '127.0.0.1'
PORT = 60314

connection = ServerConnection(HOST, PORT)
socket  = connection.getSocket()
print("Connecting")
connection.connect()

socketListener = SocketListener(socket)
socketListener.listen()

socketWriter = SocketWriter(socket)

thread = threading.Thread(target=process)
thread.start()
