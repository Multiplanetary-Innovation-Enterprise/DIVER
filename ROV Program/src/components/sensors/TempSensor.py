from abc import ABC, abstractmethod

from components.sensors.TempUnit import TempUnit
from components.sensors.Sensor import Sensor

#Represents a generic temperature sensor
class TempSensor(Sensor, ABC):
    __tempUnit:TempUnit = None #The units used to measure the temperature

    def __init__(self, tempUnit:TempUnit = TempUnit.F):
        self.__tempUnit = tempUnit

    #Gets the temperature measured by the sensor
    def getTemperature(self) -> float:
        #Checks the units used
        if self.__tempUnit == TempUnit.C:
            temp = self._getTemperatureC()
        elif self.__tempUnit == TempUnit.F:
            temp = self._getTemperatureF()
        else:
            temp = self._getTemperatureK()

        #Formats the temperature to two decimal places
        return round(temp, 2)

    #Gets the temperature in degrees celcius
    @abstractmethod
    def _getTemperatureC(self) -> float:
        pass

    #Gets the temperature in degrees fahrenheit
    @abstractmethod
    def _getTemperatureF(self) -> float:
        pass

    #Gets the temperature in kelvin
    @abstractmethod
    def _getTemperatureK(self) -> float:
        pass

    #Updates the units of measurement for temperature used
    def setUnits(self, tempUnit:TempUnit) -> None:
        self._tempUnit = tempUnit

    #Gets the current units of measurement for temperature
    def getUnits(self) -> TempUnit:
        return self._tempUnit
