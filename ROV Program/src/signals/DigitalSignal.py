from signals.SinglePinSignal import SinglePinSignal
from components.controllers.Controller import Controller
from signals.PinMode import PinMode
from signals.DigitalState import DigitalState

#Represents a digital signal
class DigitalSignal(SinglePinSignal):
    def __init__(self, controller:Controller, pinNum:int, mode:PinMode):
        super().__init__(controller, pinNum, mode)

    #Sets the resistor to the logic high state
    def setHigh(self) -> None:
        self._controller.pinWrite(self.__pinNum, DigitalState.HIGH)

    #Sets the resistor to the logic low state
    def setLow(self) -> None:
        self._controller.pinWrite(self.__pinNum, DigitalState.LOW)

    #Gets the voltage value of the pin
    def getValue(self) -> int:
        return self._controller.pinRead(self.pinNum)
