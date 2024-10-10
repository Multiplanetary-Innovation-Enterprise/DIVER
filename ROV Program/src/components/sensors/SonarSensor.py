from abc import ABC, abstractmethod

from components.sensors.Sensor import Sensor

#Represents a generic sonar sensor
class IMU(Sensor, ABC):
    #Gets all of the data from the IMU sensor
    @abstractmethod
    def getSensorData(self) -> int:
        pass
