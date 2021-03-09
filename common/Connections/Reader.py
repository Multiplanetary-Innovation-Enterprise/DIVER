from abc import ABC, abstractmethod
# from Message import Message

class Reader(ABC):
    @abstractmethod
    def receive(self, message) -> None:
        pass
