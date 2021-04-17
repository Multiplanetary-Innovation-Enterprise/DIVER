import pigpio

from components.Motor import Motor
from signals.DigitalSignal import DigitalSignal

class Stepper(Motor):
    __stepSignal:DigitalSignal = None
    __dirSignal:DigitalSignal = None
    __sleepSignal:DigitalSignal = None

    __stepCount:int = 0
    __maxSteps:int = 0

    def __init__(self, pi, stepPinNum:int, dirPinNum:int, sleepPinNum:int, rotDirection:RotDirection):
        super.init(rotDirection)

        self.__stepSignal = DigitalSignal(pi, 20, pigpio.OUTPUT)
        self.__dirSignal = DigitalSignal(pi, 21, pigpio.OUTPUT)
        self.__sleepSignal = DigitalSignal(pi, 22, pigpio.OUTPUT)

    def step(self) -> None:
        pass

    def stepN(steps:int) -> None:
        pass

    
