from components.illumination.Light import Light
from signals.PWMSignal import PWMSignal

class SubseaLight(Light):
    __pwmSignal: PWMSignal = None
    LIGHT_OFF = 1100
    LIGHT_MAX = 1900

    def __init__(self, raspberryPi, pinNum:int):
        self.__pwmSignal = PWMSignal(raspberryPi, pinNum)
        self.setBrightness(0)

    def setOn(self, on: bool) -> None:
        brightness = SubseaLight.LIGHT_OFF

        if on:
            brightness = self.getBrightness()

        self.setBrightness(brightness)

    #Sets the brightness of the light. Range [0,1]
    def setBrightness(self, brightness:float) -> None:
        if brightness < 0:
            brightness = 0
        elif brightness > 1:
            brightness = 1

        pulseWidth = self.convertBrightnessToPulseWidth(brightness)
    
        self.__brightness = brightness
        self.__pwmSignal.setPulseWidth(pulseWidth)

    def convertBrightnessToPulseWidth(self, brightness: float) -> int:
        pulseWidth = round(SubseaLight.LIGHT_OFF + ((SubseaLight.LIGHT_MAX - SubseaLight.LIGHT_OFF)) * brightness)

        return pulseWidth
