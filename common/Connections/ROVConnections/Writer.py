from abc import ABC, abstractmethod

from Message import Message

#This is the base class for all writers regardless of how they perform their write
class Writer(ABC):
    @abstractmethod
    def send(self, message:Message) -> None:
        pass
