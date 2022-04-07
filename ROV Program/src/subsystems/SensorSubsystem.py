from subsystems.Subsystem import Subsystem
from components.controllers.Controller import Controller
from components.sensors.IMU import IMU
from components.sensors.BNO055IMU import BNO055IMU
from components.sensors.TempSensor import TempSensor
from components.sensors.DS18B20TempSensor import DS18B20TempSensor
from components.sensors.BlueRoboticsTempSensor import BlueRoboticsTempSensor #4/6/22

#Represents the subsystem for collecting data
class SensorSubsystem(Subsystem):
    __internalTempSensor:TempSensor = None #The sensor for monitoring the elctronics capsule temp
    __imu:IMU = None                       #The IMU sensor
    __externalTempSensor:TempSensor = None #Blue Robotics sensor (added 4-6-22)

    def __init__(self, controller:Controller, config):
        super().__init__(controller, config)

        #Sets up the sensors that will be used
        self.__internalTempSensor = DS18B20TempSensor()
        self.__imu = BNO055IMU()
        self.__externalTempSensor = BlueRoboticsTempSensor() #added 4/6/22

    #Gets the temperature sensor that is inside the electronics capsule
    def getInternalTempSensor(self) -> TempSensor:
        return self.__internalTempSensor

    #Gets the IMU sensor on the ROV
    def getIMU(self) -> IMU:
        return self.__imu

    def getExternalTempSensor(self) -> TempSensor: #added 4/6/22 
        return self.__externalTempSensor    #added 4/6/22

    #Performs any clean up on system shutdown
    def shutdown(self) -> None:
        pass
