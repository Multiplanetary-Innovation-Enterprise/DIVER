from Server import Server
from SocketListener import SocketListener

import threading

HOST = '127.0.0.1'
PORT = 60314

def listen():
    isRunning = True

    while isRunning:
        clientConnection = server.getClientConnection()

        if not clientConnection == None:
            socket = server.getClientConnection().getSocket()
            socketListener = SocketListener(socket)
            socketListener.listen()
            isRunning = False
            server.stop()

            server.getClientConnection().close()
            break


server = Server(HOST, PORT)

thread = threading.Thread(target=listen)
thread.start()
print("server start")
server.start()
