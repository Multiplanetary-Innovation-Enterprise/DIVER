from components.sensors.Sensor import Sensor
from abc import ABC, abstractmethod
import serial

#Represents the DFRobot sonar sensor
class DFRobotSonarSensor():
    #__sensor = None #The sonar sensor
    __serialData = None

    def __init__(self,):
        super().__init__()

        try:
            self.__serialData = serial.Serial(
                port='/dev/ttyS0', #Serial port
                baudrate = 115200,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1
            )

            counter = 1
            self.__serialData.write('Write counter: %d \n'%(counter))

            #self.__sensor = x()
            self._isConnected = True
        except:
            print("Failed to detect the internal thermal sensor")
            self._isConnected = False

    #Gets the temperature reading
    def getData(self) -> int:
        #Checks if the sensor is connected
        if self._isConnected:
            #Sensor is connected, proceeds as normal

            #0 - frame 
            #1 - higher 8 bits of data 
            #2 - lower 8 bits of data 
            #3 - checksum
            message = [0] *4
            for x in range (0, 4):
                message[x] = self.__serialData.readline()
            
            #combine higher and lower bits
            data = message[1]*256 + message[2]
            return data
        else:
            return None

