from signals.devices.RaspberryPi import RaspberryPi
from subsystems.PropulsionSubsystem import PropulsionSubsystem
from subsystems.IlluminationSubsystem import IlluminationSubsystem
from subsystems.SensorSubsystem import SensorSubsystem
from subsystems.VisionSubsystem import VisionSubsystem

#Represents the ROV and all the subsystems that it encompasses
class ROV:
    __pi:RaspberryPi = None                           #The Raspberry Pi used to control the ROV
    __propSystem:PropulsionSubsystem = None           #The propulsion subsystem
    __illuminationSystem:IlluminationSubsystem = None #The lightings subsystem
    __sensorSystem:SensorSubsystem = None             #The sensor subsystem
    __visionSystem:VisionSubsystem = None             #The vision subsytem

    def __init__(self):
        self.__pi = RaspberryPi()

        self.__propSystem = PropulsionSubsystem(self.__pi)
        self.__illuminationSystem = IlluminationSubsystem(self.__pi)
        self.__sensorSystem = SensorSubsystem(self.__pi)
        self.__visionSystem = VisionSubsystem(self.__pi)

    #Gets the propulsion subsystem
    def getPropSystem(self) -> PropulsionSubsystem:
        return self.__propSystem

    #Gets the illumincation subsytem
    def getIlluminationSystem(self) -> IlluminationSubsystem:
        return self.__illuminationSystem

    #Gets the sensor subsystem
    def getSensorSystem(self) -> SensorSubsystem:
        return self.__sensorSystem

    #Gets the vision subsystem
    def getVisionSystem(self) -> VisionSubsystem:
        return self.__visionSystem
