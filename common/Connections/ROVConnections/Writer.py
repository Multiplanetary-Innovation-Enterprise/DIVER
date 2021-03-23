from abc import ABC, abstractmethod
# from Message import Message

class Writer(ABC):
    @abstractmethod
    def send(self, message) -> None:
        pass
