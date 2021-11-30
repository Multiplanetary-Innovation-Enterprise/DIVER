import configparser

from sensors.TempSensor import TempSensor
from sensors.DS18B20TempSensor import DS18B20TempSensor

class SensorSubsystem():
    __internalTempSensor: TempSensor = None
    __pi = None

    def __init__(self, pi):
        self.__pi = pi

        config = configparser.ConfigParser()

        self.__internalTempSensor = DS18B20TempSensor()

    def getInternalTempSensor(self) -> TempSensor:
        return self.__internalTempSensor
