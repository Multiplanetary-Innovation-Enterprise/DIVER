import sys
sys.path.append("tsys01-python-master")
sys.path.insert(0, r"pi\home\tsys01-python-master\tsys01")
sys.path.insert(0, r"pi\home\tsys01-python-master")
from tsys01 import TSYS01

from components.sensors.TempUnit import TempUnit

from components.sensors.TempSensor import TempSensor

class BlueRoboticsTempSensor(TempSensor):
    __sensor:TSYS01 = None #The temperature sensor

    def __init__(self, tempUnit:TempUnit = TempUnit.F):
        super().__init__(tempUnit)
       # self.__sensor = TSYS01() # Use default I2C bus 1
        #self.__sensor.init()
       # if not self.__sensor.init():
        #   print("Error initializing sensor")
         #  exit(1
        try:
           self.__sensor = TSYS01()
           self.__sensor.init()
           self._isConnected = True
        except:
           print("Failed to detect BR Temp Sensor")
           self._isConnected = False

    #Gets the temperature reading from the sensor
    def getTemperature(self) -> float:
        #Skips the temperature reading if the sensor was not found
        if not self._isConnected:
            return None

        #Performs the temperature reading
        self.__sensor.read()

        super().getTemperature()

    #Returns the current temperature value in celsius
    def _getTemperatureC(self) -> float:
        return self.__sensor.temperature()

    #Returns the current temperature value in fahrenheit
    def _getTemperatureF(self) -> float:
        return (self.__sensor.temperature() * 9/5) + 32

    #Returns the current temperature value in fahrenheit
    def _getTemperatureK(self) -> float:
        return self.__sensor.temperature() + 273.15
