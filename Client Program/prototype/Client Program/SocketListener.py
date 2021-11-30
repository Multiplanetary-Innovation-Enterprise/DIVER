import socket
import selectors

class SocketListener():
    socket = None
    isRunning = False

    def __init__(self, socket):
        self.socket = socket
        self.sel = selectors.DefaultSelector()
        self.sel.register(self.socket, selectors.EVENT_READ, data=None)

    def listen(self):
        while self.isRunning:
            events = sel.select(timeout=None)
            #Notify that data is available to read

    def stop(self):
        self.isRunning = False
        self.sel.unregister(self.socket)
        self.sel.close()
