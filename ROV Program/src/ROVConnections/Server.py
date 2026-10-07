from abc import ABC, abstractmethod

from ROVConnections.Connection import Connection

#This class represents the core operations that all servers must support
#regardless of how they are implemented
class Server(ABC):
    #Waits and accepts a client connection request once once is received
    @abstractmethod
    def getClientConnection(self) -> Connection:
        pass

    #Stops the server from accepting new client connections
    @abstractmethod
    def stop(self) -> None:
        pass
