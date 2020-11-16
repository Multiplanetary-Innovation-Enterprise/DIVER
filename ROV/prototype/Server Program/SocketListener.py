import socket
import selectors

from ObserverPattern import Observer, Observable, Event
from MessageEvent import MessageEvent

class SocketListener(Observable):
    socket = None
    isRunning = False

    def __init__(self, socket):
        self.socket = socket
        self.sel = selectors.DefaultSelector()
        self.sel.register(self.socket, selectors.EVENT_READ, data=None)
        print("socket listener ready")

    def listen(self):
        print("listenen")

        self.isRunning = True

        while self.isRunning:
            events = self.sel.select(timeout=None)

            for key, mask in events:
                message = self.getMessage()
                print(message)

                if message == "close":
                    print("stopping")
                    self.isRunning = False
                    self.stop()
                    break

                self.notify(MessageEvent(message))

    def getMessage(self):
        length = self.socket.recv(4)
        length = int.from_bytes(length, "big")

        message = self.socket.recv(length).decode('utf-8')

        return message

    def stop(self):
        print("stopping listener")
        self.isRunning = False
        self.sel.unregister(self.socket)
        self.sel.close()

    def notify(self, event: Event):
        for observer in self.observers:
            observer.update(event)
