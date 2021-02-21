from subsystems.PropulsionSubsystem import PropulsionSubsystem

import pigpio
import os
import time


class ROV:
    __propSystem = None
    __pi = None

    def __init__(self):
        #Pi connection setup
        os.system ("sudo pigpiod")
        time.sleep(1)

        self.__pi = pigpio.pi();

        self.__propSystem = PropulsionSubsystem(self.__pi)

    def getPropSystem(self) -> PropulsionSubsystem:
        return self.__propSystem
