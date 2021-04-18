from components.Stepper import Stepper
from util.RotDirection import RotDirection

class ClawSubsystem:
    __stepper: Stepper = None
    __angle: float = 0

    def __init__(self, pi):
        self.__stepper = Stepper(pi, 20, 21, 22, RotDirection.CLOCKWISE)
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
