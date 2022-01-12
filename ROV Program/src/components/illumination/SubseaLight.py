from components.illumination.Light import Light
from signals.devices.SignalDevice import SignalDevice
from signals.PWMSignal import PWMSignal
from signals.PinMode import PinMode

class SubseaLight(Light):
    __pwmSignal:PWMSignal = None
    LIGHT_OFF:int = 1100
    LIGHT_MAX:int = 1900

    def __init__(self, device:SignalDevice, pinNum:int):
        self.__pwmSignal = PWMSignal(device, pinNum, PinMode.PIN_OUT)
        self.setBrightness(0)

    def setState(self, isOn:bool) -> None:
        brightness = self.__brightness

        #Checks if the light should be turned on or off
        if not isOn:
            brightness = 0

        #Updates the brightness accordingly
        pulseWidth = self.__convertBrightnessToPulseWidth(brightness)
        self.__pwmSignal.setPulseWidth(pulseWidth)

    def __convertBrightnessToPulseWidth(self, brightness:float) -> int:
        pulseWidth = round(SubseaLight.LIGHT_OFF + ((SubseaLight.LIGHT_MAX - SubseaLight.LIGHT_OFF)) * brightness)

        return pulseWidth
