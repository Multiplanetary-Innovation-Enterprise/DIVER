from abc import ABC, abstractmethod

from ROVConnections.Connection import Connection

#This class represents the core operations that all servers must support
#regardless of how they are implemented
class Server(ABC):

    @abstractmethod
    def listen(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass

    @abstractmethod
    def getClientConnection(self) -> Connection:
        pass
