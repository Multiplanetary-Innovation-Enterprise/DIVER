from abc import ABC, abstractmethod

#Represents the pwm protocol
class PWM(ABC):
    #Updates the pulse width of the PWM signal
    @abstractmethod
    def setPulseWidth(self, pinNum:int, pulseWidth:int) -> None:
        pass

    #Gets the pulse width of the PWM signal
    @abstractmethod
    def getPulseWidth(self) -> int:
        pass
