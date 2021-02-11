class ClientConnection(SocketConnection):
    __port = None

    def __init__(self, port):
        super().__init__()
        self.__port = port
        self.get().bind(('', port))

    def getPort(self):
        return self.__port

    
