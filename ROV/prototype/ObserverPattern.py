from __future__ import annotations
from abc import ABC, abstractmethod

from Command import Command

class Observable(ABC):
    observers: List[Observer] = []

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    @abstractmethod
    def notify(self, command: Command):
        pass

class Observer(ABC):
    @abstractmethod
    def update(self, command: Command):
        pass
