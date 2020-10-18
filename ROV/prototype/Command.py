from __future__ import annotations
from abc import ABC, abstractmethod

from Chasis import Chasis

class Command(ABC):
    @abstractmethod
    def execute(self, chasis: Chasis):
        pass
