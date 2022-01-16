from subsystems.Subsystem import Subsystem
from components.controllers.Controller import Controller
from sensors.IMU import IMU
from sensors.BNO055IMU import BNO055IMU
from sensors.TempSensor import TempSensor
from sensors.DS18B20TempSensor import DS18B20TempSensor

#Represents the subsystem for collecting data
class SensorSubsystem(Subsystem):
    __internalTempSensor:TempSensor = None #The sensor for monitoring the elctronics capsule temp
    __imu:IMU = None                       #The IMU sensor

    def __init__(self, controller:Controller, config):
        super().__init__(controller, config)

        #Sets up the sensors that will be used
        self.__internalTempSensor = DS18B20TempSensor()
        self.__imu = BNO055IMU()

    #Gets the temperature sensor that is inside the electronics capsule
    def getInternalTempSensor(self) -> TempSensor:
        return self.__internalTempSensor

    #Gets the IMU sensor on the ROV
    def getIMU(self) -> IMU:
        return self.__imu

    #Performs any clean up on system shutdown
    def shutdown(self) -> None:
        pass
