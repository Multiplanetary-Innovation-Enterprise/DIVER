from abc import ABC, abstractmethod

#The publisher can publish a message to a message channel
class Publisher(ABC):
    #Sends the provided message to the provided message channel
    @abstractmethod
    def sendMessage(message:Message, messageChannel:MessageChannel) -> None:
        pass
