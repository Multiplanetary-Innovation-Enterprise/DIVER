import pigpio
import time

from components.Motor import Motor
from signals.DigitalSignal import DigitalSignal
from util.RotDirection import RotDirection

class Stepper(Motor):
    __stepSignal:DigitalSignal = None
    __dirSignal:DigitalSignal = None
    __sleepSignal:DigitalSignal = None

    __stepCount:int = 0
    __maxSteps:int = 200

    __isSleeping = True
    __stepDelay = 0.001

    DEGREES_PER_STEP = 1.8

    def __init__(self, pi, stepPinNum:int, dirPinNum:int, sleepPinNum:int, rotDirection:RotDirection):
        super().__init__(rotDirection)

        self.__stepSignal = DigitalSignal(pi, stepPinNum, pigpio.OUTPUT)
        self.__dirSignal = DigitalSignal(pi, dirPinNum, pigpio.OUTPUT)
        self.__sleepSignal = DigitalSignal(pi, sleepPinNum, pigpio.OUTPUT)

        self.__updateDirectionState(rotDirection)

        self.__updateSleepState(False)

    #Sets the rotational speed of the thruster
    def setRotDirection(self, rotDirection:RotDirection) -> None:
        super().setRotDirection(rotDirection)

        self.__updateDirectionState(rotDirection)

    def __updateDirectionState(self, rotDirection:RotDirection) -> None:
        if rotDirection == RotDirection.CLOCKWISE:
            self.__dirSignal.setHigh()
        else:
            self.__dirSignal.setLow()

    def __updateSleepState(self, sleepState:bool) -> None:
        if sleepState:
            self.__sleepSignal.setHigh()
        else:
            self.__sleepSignal.setLow()

        self.__isSleeping = sleepState

    def step(self) -> None:
        if self.__stepCount >= self.__maxSteps and self.getRotDirection() == RotDirection.CLOCKWISE or self.__stepCount <= 0 and self.getRotDirection() == RotDirection.COUNTER_CLOCKWISE:
            return

        self.__stepCount += 1 * self.getRotDirection().value

        self.__stepSignal.setHigh()
        #0.002 s does notwork for some reason
        time.sleep(self.__stepDelay)

        self.__stepSignal.setLow()

        time.sleep(self.__stepDelay)

    def stepN(self, steps:int) -> None:
        if steps > self.__maxSteps:
            steps = self.__maxSteps

        for step in range(steps):
            self.step()

    def getStepCount(self) -> int:
        return self.__stepCount

    def clearStepCount(self) -> None:
        self.__stepCount = 0

    def setMaxSteps(self, maxSteps:int) -> None:
        self.__maxSteps = maxSteps

    def getMaxSteps(self) -> int:
        return self.__maxSteps

    def sleep(self) -> None:
        self.__updateSleepState(False)

    def wake(self) -> None:
        self.__updateSleepState(True)

    def isSleeping(self) -> bool:
        return self.__isSleeping

    def setStepDelay(self, delay:float) -> None:
        self.__stepDelay = delay

    def getStepDelay(self) -> float:
        return self.__stepDelay
