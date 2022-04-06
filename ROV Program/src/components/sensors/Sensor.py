from abc import ABC

#Represents a generic sensor
class Sensor(ABC):
    #Whether or not the sensor is currently connected
    _isConnected:bool = False

    #Whether or not the sensor is currently connected
    def isConnected(self):
        return self._isConnected
