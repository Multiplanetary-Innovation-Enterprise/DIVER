from ROVConnections.SocketConnection import SocketConnection

class ClientConnection(SocketConnection):
    __address = None

    def __init__(self, socket, address):
        super().__init__(socket)

        self.__address = address
        
    def getAddress(self):
        return self.__address
