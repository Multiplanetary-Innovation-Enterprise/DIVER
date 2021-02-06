from abc import ABC,abstractmethod

#A subscriber can subscribe to a message channel
class Subscriber(ABC):
    #Recives a message from the subscribed message channels
    @abstractmethod
    def recieveMessage(message:Message) -> None:
        pass
