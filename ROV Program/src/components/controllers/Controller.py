from abc import ABC, abstractmethod

from signals.PWM import PWM
from signals.PinMode import PinMode

#Represents a generic controller that can send signals
class Controller(PWM, ABC):
    def __init__(self):
        super(PWM, self).__init__()

    #Updates the mode of the provided pin
    @abstractmethod
    def setPinMode(self, pinNum:int, mode:PinMode) -> None:
        pass

    #Gets the mode of the provided pin
    @abstractmethod
    def getPinMode(self, pinNum:int) -> PinMode:
        pass

    #Sets output value of the provided pin as an output
    @abstractmethod
    def pinWrite(self, pinNum:int, value:float) -> None:
        pass

    #Gets the value of the provided pin as an input
    @abstractmethod
    def pinRead(self, pinNum:int) -> float:
        pass
