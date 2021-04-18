from components.Stepper import Stepper
from util.RotDirection import RotDirection
from subsystems.ClawSubsystem import ClawSubsystem

import pigpio
import os
import time

#Pi connection setup
os.system ("sudo pigpiod")
time.sleep(1)

pi = pigpio.pi();

# stepper = Stepper(pi, 20, 21, 22, RotDirection.CLOCKWISE)
# stepper.setMaxSteps(200)

clawSystem = ClawSubsystem(pi)

clawSystem.setAngle(30)
time.sleep(2)
clawSystem.setAngle(50)
time.sleep(2)
clawSystem.setAngle(25)

# while True:
#     stepper.step()
#     print("Steps: " + str(stepper.getStepCount()))
