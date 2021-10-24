from abc import ABC, abstractmethod

from ROVMessaging.Message import Message

class Reader(ABC):
    @abstractmethod
    def receive(self, message:Message) -> None:
        pass
