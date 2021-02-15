from abc import ABC, abstractmethod

#Represents a command that can be executed
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass
