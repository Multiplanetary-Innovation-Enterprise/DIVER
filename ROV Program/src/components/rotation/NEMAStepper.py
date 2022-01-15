import time

from signals.PinMode import PinMode
from signals.DigitalSignal import DigitalSignal
from signals.devices.SignalDevice import SignalDevice
from components.rotation.RotDirection import RotDirection
from components.rotation.Stepper import Stepper

#Represents the NEMA## stepper motors used on the ROV
#url:
class NEMAStepper(Stepper):
    __DEGREES_PER_STEP = 1.8           #The angle rotated for one step
    __stepSignal:DigitalSignal = None  #The signal that controls the stepping
    __dirSignal:DigitalSignal = None   #The signal that controls the direction
    __sleepSignal:DigitalSignal = None #The signal that controls sleeping

    #0.002 s does notwork for some reason for delay

    def __init__(self, device:SignalDevice, stepPinNum:int, dirPinNum:int, sleepPinNum:int, rotDirection:RotDirection):
        super().__init__(rotDirection)

        self.__stepSignal = DigitalSignal(device, stepPinNum, PinMode.PIN_OUT)
        self.__dirSignal = DigitalSignal(device, dirPinNum, PinMode.PIN_OUT)
        self.__sleepSignal = DigitalSignal(device, sleepPinNum, PinMode.PIN_OUT)

    #Performs the actual step
    def _step(self) -> None:
        self.__stepSignal.setHigh()

        time.sleep(self._stepDelay)

        self.__stepSignal.setLow()

        time.sleep(self._stepDelay)

    #Performs the actual speed update
    def _updateSpeed(self) -> None:
        pass

    #Performs the direction update
    def _updateDirectionState(self) -> None:
        if self._rotDirection == RotDirection.CLOCKWISE:
            self.__dirSignal.setHigh()
        else:
            self.__dirSignal.setLow()

    #Performs the sleep update
    def _updateSleepState(self) -> None:
        if self._isSleeping:
            self.__sleepSignal.setHigh()
        else:
            self.__sleepSignal.setLow()
