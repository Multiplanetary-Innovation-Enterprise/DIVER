from abc import ABC

from signals.PinMode import PinMode
from signals.Signal import Signal
from signals.devices.SignalDevice import SignalDevice

#Represents a signal that has only one pin
class SinglePinSignal(Signal, ABC):
    __pinNum:int = None #The pin number that the signal is on

    def __init__(self, device:SignalDevice, pinNum:int, mode:PinMode):
        super(Signal, self).__init(device)

        self.__pinNum = pinNum
        self.__device.setMode(pinNum, mode)

    #Gets the pin associated with the signal
    def getPinNum(self) -> int:
        return self.__pinNum
