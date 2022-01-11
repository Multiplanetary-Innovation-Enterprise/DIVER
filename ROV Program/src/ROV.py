import pigpio
import os
import time

from subsystems.PropulsionSubsystem import PropulsionSubsystem
from subsystems.IlluminationSubsystem import IlluminationSubsystem
from subsystems.SensorSubsystem import SensorSubsystem

class ROV:
    __propSystem:PropulsionSubsystem = None
    __illuminationSystem:IlluminationSubsystem = None
    __sensorSystem:SensorSubsystem = None
    __pi = None

    def __init__(self):
        #For testing
        pi = None
        #Pi connection setup
        # os.system ("sudo pigpiod")
        # time.sleep(1)
        #
        # self.__pi = pigpio.pi();
        #
        # self.__propSystem = PropulsionSubsystem(self.__pi)
        # self.__illuminationSystem = IlluminationSubsystem(self.__pi)
        self.__sensorSystem = SensorSubsystem(self.__pi)
        pass

    def getPropSystem(self) -> PropulsionSubsystem:
        return self.__propSystem

    def getIlluminationSystem(self) -> IlluminationSubsystem:
        return self.__illuminationSystem

    def getSensorSystem(self) -> SensorSubsystem:
        return self.__sensorSystem
