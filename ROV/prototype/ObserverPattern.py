from __future__ import annotations
from abc import ABC, abstractmethod

class Observable(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass

class Observer(ABC):
    @abstractmethod
    def update(self, observable: Observable):
        pass
