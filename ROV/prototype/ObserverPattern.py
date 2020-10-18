from __future__ import annotations
from abc import ABC, abstractmethod

from Command import Command

class Observable(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self, command: Command):
        pass

class Observer(ABC):
    @abstractmethod
    def update(self, command: Command):
        pass
