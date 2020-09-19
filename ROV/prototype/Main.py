from Thruster import Thruster

import os
import time
os.system ("sudo pigpiod")
time.sleep(1)

import pigpio

pi = pigpio.pi();

thruster = Thruster(pi, 4, "Clockwise"); #make direction enum

thruster.arm();
