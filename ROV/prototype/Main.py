from __future__ import annotations
from Thruster import Thruster
from RotDirection import RotDirection
from KeyboardInput import KeyboardInput
from Chasis import Chasis
from Display import Display
from Processor import Processor
import keyboard
from ObserverPattern import Observer, Observable
from typing import List
from random import randrange
from abc import ABC, abstractmethod
#import os
#import time
#os.system ("sudo pigpiod")
#time.sleep(1)

#import pigpio

#pi = pigpio.pi();

# processor = Processor()
#
# keyboard = KeyboardInput()
# keyboard.attach(keyboard)
# #keyboard.notify()
#
#
# #chasis = Chasis(pi)
# display = Display()
# display.construct()



print("arming....")
#chasis.arm()
print("armed")
#chasis.move(0.5, 0.5, 0.5)
#chasis.stop()
# thruster = Thruster(pi, 4, RotDirection.Clockwise)
# thruster.arm()
#
# thruster.setSpeed(0.1)
# print("speed: " + str(thruster.getSpeed()))
# print("dir: " + str(thruster.getRotDirection()))
# time.sleep(5)
# thruster.stop()
# time.sleep(2)
# thruster.setRotDirection(RotDirection.CounterClockwise)
# thruster.setSpeed(0.1)
# print("speed: " + str(thruster.getSpeed()))
# print("dir: " + str(thruster.getRotDirection()))
# time.sleep(5)
# thruster.stop()

subject = KeyboardInput()

observer_a = Processor()
subject.attach(observer_a)
display = Display()
display.construct()
#subject.notify()
