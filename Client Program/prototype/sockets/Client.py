import socket
import selectors
import _thread

isRunning = True

def write():
    global isRunning

    while isRunning:
        print('write')
        message = input()
        mLength = len(message)

        bytes = mLength.to_bytes(4, 'big')

        print("message length: " + str(mLength))
        #Send length of message
        socket.send(bytes)

        print("message length: " + str(bytes))
        #Send the actual message
        socket.send(message.encode())

        if message == "close":
            print("closing....")
            isRunning = False


HOST = '127.0.0.1'
PORT = 60314

sel = selectors.DefaultSelector()

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setblocking(False)
socket.connect_ex((HOST, PORT))
events = selectors.EVENT_READ
sel.register(socket, events, data=None)

_thread.start_new_thread(write, ())

while isRunning:
    events = sel.select(timeout=None)

    

print("closing socket")
sel.unregister(socket)
sel.close()
socket.close()
socket = None
