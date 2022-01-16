from abc import ABC, abstractmethod

#Represents a command that can be executed
class Command(ABC):
    #Executes the command
    @abstractmethod
    def execute(self) -> None:
        pass

    #Whether or not the command can be repeated back to back
    #(without a different command in between)
    @abstractmethod
    def isRepeatable(self) -> bool:
        pass

    #The action code associated with this command
    @staticmethod
    @abstractmethod
    def getActionCode() -> int:
        pass

    #Allows for command objects to compared and to see if all of their attributes match
    def __eq__(self, other) -> bool:
        return self.__dict__ == other.__dict__
