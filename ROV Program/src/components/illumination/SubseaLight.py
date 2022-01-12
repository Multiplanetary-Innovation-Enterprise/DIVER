from components.illumination.Light import Light
from signals.devices.SignalDevice import SignalDevice
from signals.PWMSignal import PWMSignal
from signals.PinMode import PinMode

#Represents the subsea lights used on the ROV from bluerobotics
#url: https://bluerobotics.com/store/thrusters/lights/lumen-r2-rp/
class SubseaLight(Light):
    __pwmSignal:PWMSignal = None #The PWM signal used to control the light
    LIGHT_OFF:int = 1100         #The pulse-width value to turn the light off
    LIGHT_MAX:int = 1900         #The maximim brightness pulse-width for the light

    def __init__(self, device:SignalDevice, pinNum:int):
        self.__pwmSignal = PWMSignal(device, pinNum, PinMode.PIN_OUT)
        self.setBrightness(0)

    #Performs the brightness update using the PWM interface
    def _updateBrightness(self) -> None:
        brightness = self.__brightness

        #Checks if the light should be turned on or off
        if not self.__isActive:
            brightness = 0

        #Updates the brightness accordingly
        pulseWidth = self.__convertBrightnessToPulseWidth(brightness)
        self.__pwmSignal.setPulseWidth(pulseWidth)

    #Performs the brightness conversion from the range [0,1] to [LIGHT_OFF,LIGHT_MAX]
    #LIGHT_OFF is the reference point with the total range being the difference between the max
    #brightness level(LIGHT_MAX) and the off value(LIGHT_OFF). The provided brightness is the used
    #as a scalar for that range
    def __convertBrightnessToPulseWidth(self, brightness:float) -> int:
        pulseWidth = round(SubseaLight.LIGHT_OFF + ((SubseaLight.LIGHT_MAX - SubseaLight.LIGHT_OFF)) * brightness)

        return pulseWidth
