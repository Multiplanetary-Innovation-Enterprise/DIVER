import sys
sys.path.append("tsys01-python-master")
sys.path.insert(0, r"pi\home\tsys01-python-master\tsys01")
sys.path.insert(0, r"pi\home\tsys01-python-master")

from components.sensors.kellerLD import KellerLD
from components.sensors.Sensor import Sensor

class PressureSensor(Sensor):
    __sensor = None

    def __init__(self):
        try:
           self.__sensor = KellerLD()
           self.__sensor.init()
           self._isConnected = True
        except:
           print("Failed to detect BR Pressure Sensor")
           self._isConnected = False

    #Read the sensor and update the pressure value
    def _read(self) ->float:
        return self.__sensor.read()

    #Returns the current pressure value
    def getPressure(self) -> float:
        return self.__sensor.pressure()
