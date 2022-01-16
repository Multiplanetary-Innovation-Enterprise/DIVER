from signals.PinMode import PinMode
from signals.DigitalSignal import DigitalSignal
from components.controllers.Controller import Controller

class LimitSwitch:
    __digitalSignal:DigitalSignal = None #The signal used to check the switch state

    def __init__(self, controller:Controller, pinNum:int):
        super().__init__(rotDirection)

        self.__digitalSignal = DigitalSignal(controller, pinNum, PinMode.PIN_OUT)

    #Whether or not th switch was pressed
    def isPressed(self) -> bool:
        return self.__digitalSignal.isHigh()
