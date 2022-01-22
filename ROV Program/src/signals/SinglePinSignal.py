from abc import ABC

from signals.PinMode import PinMode
from signals.Signal import Signal
from components.controllers.Controller import Controller

#Represents a signal that has only one pin
class SinglePinSignal(Signal, ABC):
    _pinNum:int = None #The pin number that the signal is on

    def __init__(self, controller:Controller, pinNum:int, mode:PinMode):
        super().__init__(controller)

        self._pinNum = pinNum
        self._controller.setPinMode(pinNum, mode)

    #Gets the pin associated with the signal
    def getPinNum(self) -> int:
        return self._pinNum
