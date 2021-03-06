from __future__ import annotations
from abc import ABC, abstractmethod

from Chasis import Chasis

#Represents a command that can be sent to the ROV
class Command(ABC):
    #Executes the command and provided with a reference to the chasis
    @abstractmethod
    def execute(self, chasis: Chasis):
        pass

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
