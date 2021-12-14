from abc import ABC, abstractmethod

#Represents a command that can be executed
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    #Allows for command objects to compared and to see if all of their attributes match
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    #Whether or not the command can be repeated back to back
    @abstractmethod
    def isRepeatable(self) -> bool:
        pass

    #TODO implement
    #Gets the code of the corresponding action
    @abstractmethod
    def getActionCode(self) -> int:
        pass
