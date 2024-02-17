from components.controllers.RaspberryPi import RaspberryPi
from components.controllers.DummyController import DummyController
from components.controllers.Controller import Controller

from subsystems.PropulsionSubsystem import PropulsionSubsystem
from subsystems.IlluminationSubsystem import IlluminationSubsystem
from subsystems.SensorSubsystem import SensorSubsystem
from subsystems.VisionSubsystem import VisionSubsystem
from subsystems.AutonomySubsystem import AutonomySubsystem

#Represents the ROV and all the subsystems that it encompasses
class ROV:
    __controller:Controller = None                    #The controller used to control the ROV
    __propSystem:PropulsionSubsystem = None           #The propulsion subsystem
    __illuminationSystem:IlluminationSubsystem = None #The lightings subsystem
    __sensorSystem:SensorSubsystem = None             #The sensor subsystem
    __visionSystem:VisionSubsystem = None             #The vision subsytem
    __autonomySystem:AutonomySubsystem = None
    __config = None                                   #The configuration file

    def __init__(self, config):
        self.__config = config

        #Used to determine which controller to use
        if self.__config['Testing']['FakeHardware'].lower() == "true":
            print("Testing mode! Hardware is being faked with a dummy controller")
            self.__controller = DummyController()
        else:
            self.__controller = RaspberryPi()

        self.__propSystem = PropulsionSubsystem(self.__controller, self.__config)
        self.__illuminationSystem = IlluminationSubsystem(self.__controller, self.__config)
        self.__sensorSystem = SensorSubsystem(self.__controller, self.__config)
        self.__visionSystem = VisionSubsystem(self.__controller, self.__config)
        self.__autonomySystem = AutonomySubsystem()

    #Gets the propulsion subsystem
    def getPropSystem(self) -> PropulsionSubsystem:
        return self.__propSystem
    
    def getAutonomySystem(self) -> AutonomySubsystem:
        return self.__autonomySystem

    #Gets the illumincation subsytem
    def getIlluminationSystem(self) -> IlluminationSubsystem:
        return self.__illuminationSystem

    #Gets the sensor subsystem
    def getSensorSystem(self) -> SensorSubsystem:
        return self.__sensorSystem

    #Gets the vision subsystem
    def getVisionSystem(self) -> VisionSubsystem:
        return self.__visionSystem

    #Shuts down all of the subsystems
    def shutdown(self) -> None:
        self.__autonomySystem.shutdown()
        self.__propSystem.shutdown()
        self.__illuminationSystem.shutdown()
        self.__sensorSystem.shutdown()
        self.__visionSystem.shutdown()
