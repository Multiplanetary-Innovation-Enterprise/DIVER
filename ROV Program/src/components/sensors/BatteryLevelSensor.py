from components.sensors.Sensor import Sensor
from abc import ABC, abstractmethod

#Represents a generic battery level sensor
class BatteryLevelSensor(Sensor, ABC):

    def _getBatteryLevel(self,type:str) -> int:
        if type == "Voltage":
            return self._getlevelbyVoltage()
        elif type == "Coulombs":
            return self._getlevelbyCoulombs()

    @abstractmethod
    def _getlevelbyVoltage():
        pass

    @abstractmethod
    def _getlevelbyCoulombs():
        pass