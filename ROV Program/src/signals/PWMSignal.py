from signals.PinMode import PinMode
from components.controllers.Controller import Controller
from signals.SinglePinSignal import SinglePinSignal

class PWMSignal(SinglePinSignal):
    __pulseWidth:int = 0 #The pulse width of the PWM signal

    def __init__(self, controller:Controller, pinNum:int, mode:PinMode):
        super().__init__(controller, pinNum, mode)

    #Updates the pulsewidth of the signal
    def setPulseWidth(self, pulseWidth:int) -> None:
        self.__pulseWidth = pulseWidth
        self._controller.setPulseWidth(self._pinNum, self.__pulseWidth)

    #Gets the pulse width of the signal
    def getPulseWidth(self) ->int:
        return self.__pulseWidth
