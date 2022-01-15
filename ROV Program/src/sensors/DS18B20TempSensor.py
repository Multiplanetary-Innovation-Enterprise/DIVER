from w1thermsensor import W1ThermSensor, Unit

from sensors.TempUnit import TempUnit
from sensors.TempSensor import TempSensor

#Represents the DS18B20 temperature sensor
class DS18B20TempSensor(TempSensor):
    __sensor:W1ThermSensor = None #The temperature sensor

    def __init__(self, tempUnit:TempUnit = TempUnit.F):
        super().__init__(tempUnit)

        self.__sensor = W1ThermSensor()

    #Gets the temperature in degrees celcius
    def _getTemperatureC(self) -> float:
        return self.__sensor.get_temperature(Unit.DEGREES_C)

    #Gets the temperature in degrees fahrenheit
    def _getTemperatureF(self) -> float:
        return self.__sensor.get_temperature(Unit.DEGREES_F)

    #Gets the temperature in kelvin
    def _getTemperatureK(self) -> float:
        return self.__sensor.get_temperature(Unit.DEGREES_K)
