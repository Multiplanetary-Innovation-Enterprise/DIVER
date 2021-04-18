from subsystems.PropulsionSubsystem import PropulsionSubsystem
from subsystems.IlluminationSubsystem import IlluminationSubsystem
from subsystems.ClawSubsystem import ClawSubsystem

import pigpio
import os
import time

class ROV:
    __propSystem:PropulsionSubsystem = None
    __illuminationSystem:IlluminationSubsystem = None
    __clawSystem:ClawSubsystem = None
    __pi = None

    def __init__(self):
        #Pi connection setup
        os.system ("sudo pigpiod")
        time.sleep(1)

        self.__pi = pigpio.pi();

        self.__propSystem = PropulsionSubsystem(self.__pi)
        self.__illuminationSystem = IlluminationSubsystem(self.__pi)
        self.__clawSystem = ClawSubsystem(self.__pi)

    def getPropSystem(self) -> PropulsionSubsystem:
        return self.__propSystem

    def getIlluminationSystem(self) -> IlluminationSubsystem:
        return self.__illuminationSystem

    def getClawSystem(self) -> ClawSubsystem:
        return self.__clawSystem
