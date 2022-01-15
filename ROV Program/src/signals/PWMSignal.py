from signals.PinMode import PinMode
from signals.devices.SignalDevice import SignalDevice
from signals.SinglePinSignal import SinglePinSignal

class PWMSignal(SinglePinSignal):
    __pulseWidth:int = 0 #The pulse width of the PWM signal

    def __init__(self, device:SignalDevice, pinNum:int, mode:PinMode):
        super().__init__(device, pinNum, mode)

    #Updates the pulsewidth of the signal
    def setPulseWidth(self, pulseWidth:int) -> None:
        self.__pulseWidth = pulseWidth
        self._device.setPulseWidth(self._pinNum, self.__pulseWidth)

    #Gets the pulse width of the signal
    def getPulseWidth(self) ->int:
        return self.__pulseWidth
