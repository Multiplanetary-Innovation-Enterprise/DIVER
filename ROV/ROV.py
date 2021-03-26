from subsystems.PropulsionSubsystem import PropulsionSubsystem
from subsystems.IlluminationSubsystem import IlluminationSubsystem

import pigpio
import os
import time

class ROV:
    __propSystem:PropulsionSubsystem = None
    __illuminationSystem:IlluminationSubsystem = None
    __pi = None

    def __init__(self):
        #Pi connection setup
        # os.system ("sudo pigpiod")
        # time.sleep(1)
        #
        # self.__pi = pigpio.pi();
        #
        # self.__propSystem = PropulsionSubsystem(self.__pi)
        # self.__illuminationSystem = IlluminationSubsystem(self.__pi)
        pass

    def getPropSystem(self) -> PropulsionSubsystem:
        return self.__propSystem

    def getIlluminationSystem(self) -> IlluminationSubsystem:
        return self.__illuminationSystem
