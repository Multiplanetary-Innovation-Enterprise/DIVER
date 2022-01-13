from signals.PinMode import PinMode
from signals.DigitalSignal import DigitalSignal
from signals.devices.SignalDevice import SignalDevice

class LimitSwitch:
    __digitalSignal:DigitalSignal = None #The signal used to check the switch state

    def __init__(self, device:SignalDevice, pinNum:int):
        super().__init__(rotDirection)

        self.__digitalSignal = DigitalSignal(device, pinNum, PinMode.PIN_OUT)

    #Whether or not th switch was pressed
    def isPressed(self) -> bool:
        return self.__digitalSignal.isHigh()
