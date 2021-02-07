from abc import ABC, abstractmethod

from Message import Message

#A subscriber can subscribe to a message channel
class Subscriber(ABC):
    #Recives a message from the subscribed message channels
    @abstractmethod
    def recieveMessage(self, message:Message) -> None:
        pass
