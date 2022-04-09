import sys
sys.path.append("tsys01-python-master")
sys.path.insert(0, r"pi\home\tsys01-python-master\tsys01")
sys.path.insert(0, r"pi\home\tsys01-python-master")
from components.sensors.kellerLD import KellerLD




class PressureSensor:
    __sensor = None
    isConnected = None



    def __init__(self):
       # self.__sensor = TSYS01() # Use default I2C bus 1
        #self.__sensor.init()
       # if not self.__sensor.init():
        #   print("Error initializing sensor")
         #  exit(1
        try:
           self.__sensor = KellerLD()
           self.__sensor.init()
           self.isConnected = True
        except:
           print("Failed to detect BR Pressure Sensor")
           self.isConnected = False
    
#Read the sensor and update the temperature value
    def _read(self):
 
        return self.__sensor.read()
    
#Returns the current temperature value in celsius
    def _getPressure(self):
        return self.__sensor.pressure()


