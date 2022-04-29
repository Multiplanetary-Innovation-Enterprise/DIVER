from signals.SinglePinSignal import SinglePinSignal
from signals.DigitalState import DigitalState

#Represents a digital signal
class DigitalSignal(SinglePinSignal):
    #Sets the resistor to the logic high state
    def setHigh(self) -> None:
        self._controller.pinWrite(self.__pinNum, DigitalState.HIGH)

    #Sets the resistor to the logic low state
    def setLow(self) -> None:
        self._controller.pinWrite(self.__pinNum, DigitalState.LOW)

    #Gets the voltage value of the pin
    def getValue(self) -> int:
        return self._controller.pinRead(self.pinNum)
