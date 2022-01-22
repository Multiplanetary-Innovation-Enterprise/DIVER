from components.illumination.Light import Light
from components.controllers.Controller import Controller
from signals.PWMSignal import PWMSignal
from signals.PinMode import PinMode

#Represents the subsea lights used on the ROV from bluerobotics
#url: https://bluerobotics.com/store/thrusters/lights/lumen-r2-rp/
class SubseaLight(Light):
    __pwmSignal:PWMSignal = None #The PWM signal used to control the light
    __LIGHT_OFF:int = 1100         #The pulse-width value to turn the light off
    __LIGHT_MAX:int = 1900         #The maximim brightness pulse-width for the light

    def __init__(self, controller:Controller, pinNum:int):
        self.__pwmSignal = PWMSignal(controller, pinNum, PinMode.PIN_OUT)
        self.setBrightness(0)

    #Performs the brightness update using the PWM interface
    def _updateBrightness(self) -> None:
        brightness = self._brightness

        #Checks if the light should be turned on or off
        if not self._isActive:
            brightness = 0

        #Updates the brightness accordingly
        pulseWidth = self.__convertBrightnessToPulseWidth(brightness)
        self.__pwmSignal.setPulseWidth(pulseWidth)

    #Performs the brightness conversion from the range [0,1] to [LIGHT_OFF,LIGHT_MAX]
    #LIGHT_OFF is the reference point with the total range being the difference between the max
    #brightness level(LIGHT_MAX) and the off value(LIGHT_OFF). The provided brightness is then used
    #as a scalar for that range
    def __convertBrightnessToPulseWidth(self, brightness:float) -> int:
        pulseWidth = round(self.__LIGHT_OFF + ((self.__LIGHT_MAX - self.__LIGHT_OFF)) * brightness)

        return pulseWidth
