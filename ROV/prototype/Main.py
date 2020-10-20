from Thruster import Thruster
from RotDirection import RotDirection
from KeyboardInput import KeyboardInput
from Chasis import Chasis
from Display import Display
from Processor import Processor
import keyboard

import os
import time
os.system ("sudo pigpiod")
time.sleep(1)

import pigpio

pi = pigpio.pi();

print("arming....")
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
print("Initializing. Please wait...\n")
keyboard = KeyboardInput()
chasis = Chasis(pi)
chasis.arm()
print("armed")

processor = Processor(chasis)
keyboard.attach(processor)

display = Display()
display.construct()