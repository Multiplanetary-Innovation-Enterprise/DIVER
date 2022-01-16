import pigpio
import os
import time

from signals.PinMode import PinMode
from signals.ResistorType import ResistorType
from components.controllers.Controller import Controller

#Represents the Raspberry Pi itself (a wrapper for the pigpio library)
class RaspberryPi(Controller):
    __pi = None #The raspberry pi

    def __init__(self):
        # os.system ("sudo pigpiod")
        # time.sleep(1)
        #
        # self.__pi = pigpio.pi()
        pass

    #Updates the mode of the provided pin
    def setPinMode(self, pinNum:int, mode:PinMode) -> None:
        #self.__pi.set_mode(pinNum, mode)
        pass

    #Gets the mode of the provided pin
    def getPinMode(self, pinNum:int) -> PinMode:
        return self.__pi.get_mode(pinNum)

    #Sets output value of the provided pin as an output
    def pinWrite(self, pinNum:int, value:float) -> None:
        self.__pi.write(pinNum, value)

    #Gets the value of the provided pin as an input
    def pinRead(self, pinNum:int) -> float:
        return self.__pi.read(pinNum)

    #Updates the pulse width of the PWM signal
    def setPulseWidth(self, pinNum:int, pulseWidth:int) -> None:
        #self.__pi.set_servo_pulsewidth(pinNum, pulseWidth)
        pass

    #Gets the pulse width of the PWM signal
    def getPulseWidth(self) -> int:
        self.__pi.get_servo_pulsewidth(self.__pinNum)

    #Gets the underlying raspberry pi device
    def getRaspberryPi(self):
        return self.__pi

    #Updates the interal resistor type connected to the pin (none, pull-up, pull-down)
    def setInternalResistorType(self, pinNum:int, type:ResistorType) -> None:
        self.__pi.set_pull_up_down(pinNum, type)
