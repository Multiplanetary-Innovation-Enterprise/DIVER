from abc import ABC, abstractmethod

from signals.PWM import PWM
from signals.PinMode import PinMode

#Represents a controller that does nothing for tesing the code without hardware
class DummyController(PWM, ABC):
    def __init__(self):
        super(PWM, self).__init__()

    #Updates the mode of the provided pin
    def setPinMode(self, pinNum:int, mode:PinMode) -> None:
        pass

    #Gets the mode of the provided pin
    def getPinMode(self, pinNum:int) -> PinMode:
        pass

    #Sets output value of the provided pin as an output
    def pinWrite(self, pinNum:int, value:float) -> None:
        pass

    #Gets the value of the provided pin as an input
    def pinRead(self, pinNum:int) -> float:
        pass

    #Updates the pulse width of the PWM signal
    def setPulseWidth(self, pinNum:int, pulseWidth:int) -> None:
        pass

    #Gets the pulse width of the PWM signal
    def getPulseWidth(self) -> int:
        pass
