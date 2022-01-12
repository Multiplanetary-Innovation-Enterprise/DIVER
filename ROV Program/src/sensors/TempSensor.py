from abc import ABC, abstractmethod

from sensors.TempUnit import TempUnit

class TempSensor(ABC):
    _tempUnit:TempUnit = TempUnit.F

    def __init__(self, tempUnit:TempUnit = TempUnit.F):
        self._tempUnit = tempUnit

    @abstractmethod
    def getTemperature(self) -> float:
        pass

    def setUnits(self, tempUnit:TempUnit) -> None:
        self._tempUnit = tempUnit

    def getUnits(self):
        return self._tempUnit
