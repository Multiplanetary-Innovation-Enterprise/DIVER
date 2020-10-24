from __future__ import annotations
from abc import ABC, abstractmethod

from Command import Command

#Represents something that can be observed for commands
class Observable(ABC):
    observers: List[Observer] = [] #List of observers listening to this subject for commands

    #Adds an observer to the list of observers
    def attach(self, observer: Observer):
        self.observers.append(observer)

    #Removes an observer from the list of observers
    def detach(self, observer: Observer):
        self.observers.remove(observer)

    #Notifies all observers that a command was sent
    @abstractmethod
    def notify(self, command: Command):
        pass

#Represents something that can listen for commands
class Observer(ABC):
    #Notifies the observer that a command has been recieved
    @abstractmethod
    def update(self, command: Command):
        pass
