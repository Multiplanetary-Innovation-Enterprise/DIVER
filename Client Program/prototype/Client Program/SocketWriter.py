class SocketWriter():
    socket = None

    def __init__(self, socket):
        self.socket = socket

    def write(self, message):
        self.writeHeader(message)
        self.socket.send(message.encode())

    def writeHeader(self, message):
        length = len(message)
        bytes = length.to_bytes(4, 'big')

        self.socket.send(bytes)
