from abc import ABC, abstractmethod

from ROVMessaging.Message import Message

#This is the base class for all readers regardless of how they perform their read
class Reader(ABC):
    #Receives a message
    @abstractmethod
    def receive(self, message:Message) -> None:
        pass
