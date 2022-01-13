from abc import ABC, abstractmethod

#Represents a generic light source
class Light(ABC):
    _isActive:bool = False  #Whether or not the light is currently turned on
    _brightness:float = 0.1 #The brightness of the light when turned on

    #Turns the light on to its current brightness
    def turnOn(self) -> None:
        self._isActive = True
        self._updateBrightness()

    #Turns the light off
    def turnOff(self) -> None:
        self._isActive = False
        self._updateBrightness()

    #Sets the brightness of the light
    def setBrightness(self, brightness:float) -> None:
        self._brightness = self.__boundBrightness(brightness)
        self._isActive = self._brightness > 0

        #Updates the state of the light based on the new brightness
        self._updateBrightness()

    #Keeps the brightness in the range [0,1]
    def __boundBrightness(self, brightness:float) -> float:
        if brightness < 0:
            brightness = 0
        elif brightness > 1:
            brightness = 1

        return brightness

    #Performs the actual brightness update, since lights can have different
    #hardware interfaces
    @abstractmethod
    def _updateBrightness(self) -> None:
        pass

    #Gets the brightness of the light when turned on
    def getBrightness(self) -> float:
        return self._brightness

    #Gets the state(on/off) of the light
    def isActive(self) -> bool:
        return self._isActive
