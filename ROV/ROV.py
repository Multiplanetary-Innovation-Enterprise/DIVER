from subsystems.* import *

import pigpio
import os
import time

class ROV:
    __propSystem:PropulsionSubsystem = None
    __illuminationSystem:IlluminationSubSystem = None
    __pi = None

    def __init__(self):
        #Pi connection setup
        os.system ("sudo pigpiod")
        time.sleep(1)

        self.__pi = pigpio.pi();

        self.__propSystem = PropulsionSubsystem(self.__pi)
        self.__illuminationSystem = IlluminationSubSystem(self.__pi)

    def getPropSystem(self) -> PropulsionSubsystem:
        return self.__propSystem

    def getIlluminationSystem(self) -> IlluminationSubSystem:
        return self.__illuminationSystem
