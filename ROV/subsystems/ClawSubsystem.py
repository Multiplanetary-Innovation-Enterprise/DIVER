from components.Stepper import Stepper
from util.RotDirection import RotDirection

import configparser

class ClawSubsystem:
    __stepper: Stepper = None
    __angle: float = 0

    def __init__(self, pi):
        config = configparser.ConfigParser()

        config.read('config.ini')
        stepPin = int(config['Claw']['StepperStepPin'])
        dirPin = int(config['Claw']['StepperDirPin'])
        sleepPin = int(config['Claw']['StepperSleepPin'])

        self.__stepper = Stepper(pi, stepPin, dirPin, sleepPin, RotDirection.CLOCKWISE)
        self.__stepper.wake()

    def setAngle(self, angle:float):
        diff = angle - self.__angle

        self.__angle = angle

        if(diff < 0):
            self.__stepper.setRotDirection(RotDirection.COUNTER_CLOCKWISE)
        else:
            self.__stepper.setRotDirection(RotDirection.CLOCKWISE)

        steps = abs(round(diff / Stepper.DEGREES_PER_STEP))

        self.__stepper.stepN(steps)

    def getAngle(self):
        return self.__angle

    def open(self):
        pass

    def close(self):
        pass
