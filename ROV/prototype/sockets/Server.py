import socket
import selectors

clientSocket = None

def accept_connection(clientConn):
    global clientSocket

    clientSocket, addr = clientConn.accept()
    clientSocket.setblocking(False)
    sel.register(clientSocket, selectors.EVENT_READ, data=None)

def close_connection(clientSocket):
    sel.unregister(clientSocket)
    clientSocket.close()
    clientSocket = None

HOST = '127.0.0.1'
PORT = 60314

sel = selectors.DefaultSelector()

listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listenSocket.bind((HOST, PORT))
listenSocket.listen()

print("Listening for connection....")
listenSocket.setblocking(False)

sel.register(listenSocket, selectors.EVENT_READ, data=None)

isRunning = True
accepted = False

while isRunning:
    events = sel.select(timeout=None)

    for key, mask in events:
        print("data: " + str(key.data))

        if key.data is None:
            if not accepted:
                print("New Connection")
                #accept_connection(key.fileobj)
                clientSocket, addr = key.fileobj.accept()
                clientSocket.setblocking(False)
                sel.register(clientSocket, selectors.EVENT_READ, data=None)
                accepted = True
            else:
                print("Reading")

                length = clientSocket.recv(4)
                print("Read: " + str(length))
                length = int.from_bytes(length, "big")

                print("length " + str(length))

                message = clientSocket.recv(length).decode('utf-8')

                print("recv: " + message)

                if message == "close":
                    close_connection(clientSocket)
                    clientSocket = None

                    isRunning = False


        else:
            print("Socket Event!")
            print(mask)
            message = key.data
            print(message)

sel.close()
listenSocket.close()
