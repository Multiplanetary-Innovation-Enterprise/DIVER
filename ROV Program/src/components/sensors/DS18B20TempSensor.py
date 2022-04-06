from w1thermsensor import W1ThermSensor, Unit

from components.sensors.TempUnit import TempUnit
from components.sensors.TempSensor import TempSensor

#Represents the DS18B20 temperature sensor
class DS18B20TempSensor(TempSensor):
    __sensor:W1ThermSensor = None #The temperature sensor

    def __init__(self, tempUnit:TempUnit = TempUnit.F):
        super().__init__(tempUnit)

        #Attempts to connect to the IMU sensor
        try:
            self.__sensor = W1ThermSensor()
            self._isConnected = True
        except:
            print("Failed to detect thermal sensor")
            self._isConnected = False

    #Gets the temperature reading
    def getTemperature(self) -> float:
        #Checks if the sensor is connected
        if self._isConnected:
            #Sensor is connected, proceeds as normal
            super().getTemperature()
        else:
            return None

    #Gets the temperature in degrees celcius
    def _getTemperatureC(self) -> float:
        return self.__sensor.get_temperature(Unit.DEGREES_C)

    #Gets the temperature in degrees fahrenheit
    def _getTemperatureF(self) -> float:
        return self.__sensor.get_temperature(Unit.DEGREES_F)

    #Gets the temperature in kelvin
    def _getTemperatureK(self) -> float:
        return self.__sensor.get_temperature(Unit.DEGREES_K)
