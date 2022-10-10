from subsystems.Subsystem import Subsystem
from components.controllers.Controller import Controller
from components.sensors.IMU import IMU
from components.sensors.BNO055IMU import BNO055IMU
from components.sensors.TempSensor import TempSensor
from components.sensors.DS18B20TempSensor import DS18B20TempSensor
from components.sensors.BlueRoboticsTempSensor import BlueRoboticsTempSensor #4/6/22
from components.sensors.PressureSensor import PressureSensor
from components.sensors.TempUnit import TempUnit

#Represents the subsystem for collecting data
class SensorSubsystem(Subsystem):
    __internalTempSensor:TempSensor = None #The sensor for monitoring the elctronics capsule temp
    __imu:IMU = None                       #The IMU sensor
    __externalTempSensor:TempSensor = None #Blue Robotics sensor (added 4-6-22)
    __pressureSensor:PressureSensor = None #Pressure sensor added 4/8/22

    def __init__(self, controller:Controller, config):
        super().__init__(controller, config)

        #Sets up the sensors that will be used
        self.__internalTempSensor = DS18B20TempSensor(TempUnit.C)
        self.__imu = BNO055IMU()
        self.__externalTempSensor = BlueRoboticsTempSensor(TempUnit.C) #added 4/6/22
        self.__pressureSensor = PressureSensor() #added 4/8/22

    #Gets the temperature sensor that is inside the electronics capsule
    def getInternalTempSensor(self) -> TempSensor:
        return self.__internalTempSensor

    #Gets the IMU sensor on the ROV
    def getIMU(self) -> IMU:
        return self.__imu

    #Gets the externally mounted temperature sensor on the ROV
    def getExternalTempSensor(self) -> TempSensor: #added 4/6/22
        return self.__externalTempSensor    #added 4/6/22

    #Gets the externally mounted pressure sensor on the ROV
    def getPressureSensor(self) -> PressureSensor:
        return self.__pressureSensor #added 4/8/22

    #Performs any clean up on system shutdown
    def shutdown(self) -> None:
        pass
