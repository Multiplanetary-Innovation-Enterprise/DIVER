from abc import ABC, abstractmethod
from Message import Message

class Publisher(ABC):
    @abstractmethod
    def send(self, message:Message) -> None:
        pass
