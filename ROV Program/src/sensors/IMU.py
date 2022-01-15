from abc import ABC, abstractmethod

from sensors import IMUData

#Represents a generic IMU sensor
class IMU(ABC):
    #Gets all of the data from the IMU sensor
    @abstractmethod
    def getSensorData(self) -> IMUData:
        pass

    #Gets the temperature of the IMU sensor
    @abstractmethod
    def getTemperature(self) -> float:
        pass
