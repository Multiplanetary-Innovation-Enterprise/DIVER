from abc import ABC, abstractmethod

#This class represents any type of connection to the server regardless of how it
#performs its connection
class Connection(ABC):
    #Performs the connection to the server
    @abstractmethod
    def connect(self) -> None:
        pass

    #Closes the connection to the server
    @abstractmethod
    def close(self) -> None:
        pass
