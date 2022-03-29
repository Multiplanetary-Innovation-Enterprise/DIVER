import sys
sys.path.append("tsys01-python-master")
sys.path.insert(0, r"pi\home\tsys01-python-master\tsys01")
sys.path.insert(0, r"pi\home\tsys01-python-master")
from tsys01 import TSYS01




class BlueRoboticsTempSensor:
    __sensor = None



    def __init__(self):
        self.__sensor = TSYS01() # Use default I2C bus 1
        #self.__sensor.init()
        if not self.__sensor.init():
           print("Error initializing sensor")
           exit(1)

#Read the sensor and update the temperature value
    def _read(self):
        return self.__sensor.read()
    
#Returns the current temperature value in celsius
    def _getTemperatureC(self):
        return self.__sensor.temperature()

#Returns the current temperature value in fahrenheit
    def _getTemperatureF(self):
        return (self.__sensor.temperature()*9/5)+32
        
        
        #Returns the current temperature value in fahrenheit
    def _getTemperatureK(self):
        return self.__sensor.temperature()+273.15
