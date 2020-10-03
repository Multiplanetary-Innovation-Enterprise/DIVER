from Thruster import Thruster
from RotDirection import RotDirection

import os
import time
os.system ("sudo pigpiod")
time.sleep(1)

import pigpio

pi = pigpio.pi();

thruster = Thruster(pi, 4, RotDirection.Clockwise)
print("arming....")
thruster.arm()
print("armed")

thruster.setSpeed(0.1)
print("speed: " + str(thruster.getSpeed()))
print("dir: " + str(thruster.getRotDirection()))
time.sleep(5)
thruster.stop()
time.sleep(2)
thruster.setRotDirection(RotDirection.CounterClockwise)
thruster.setSpeed(0.1)
print("speed: " + str(thruster.getSpeed()))
print("dir: " + str(thruster.getRotDirection()))
time.sleep(5)
thruster.stop()
