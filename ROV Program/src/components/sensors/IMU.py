from abc import ABC, abstractmethod

from components.sensors.IMUData import IMUData
from components.sensors.Sensor import Sensor

#Represents a generic IMU sensor
class IMU(Sensor, ABC):
    #Gets all of the data from the IMU sensor
    @abstractmethod
    def getSensorData(self) -> IMUData:
        pass

    #Gets the temperature of the IMU sensor
    @abstractmethod
    def getTemperature(self) -> float:
        pass
