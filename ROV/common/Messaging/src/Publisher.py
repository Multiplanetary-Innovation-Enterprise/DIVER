from abc import ABC, abstractmethod

from MessageChannel import MessageChannel
from Message import Message

#The publisher can publish a message to a message channel
class Publisher(ABC):
    #Sends the provided message to the provided message channel
    @abstractmethod
    def sendMessage(self, message:Message, messageChannel:MessageChannel) -> None:
        pass
