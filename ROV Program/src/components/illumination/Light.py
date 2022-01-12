from abc import ABC, abstractmethod

#Represents a generic light source
class Light(ABC):
    __isActive:bool = False  #Whether or not the light is currently turned on
    __brightness:float = 0.1 #The brightness of the light when turned on

    #Turns the light on to its current brightness
    def turnOn(self) -> None:
        self.__isActive = True
        self._updateBrightness()

    #Turns the light off
    def turnOff(self) -> None:
        self.__isActive = False
        self._updateBrightness()

    #Sets the brightness of the light
    def setBrightness(self, brightness:float) -> None:
        self.__brightness = self.__boundBrightness(brightness)
        self.__isActive = self.__brightness > 0

        #Updates the state of the light based on the new brightness
        self._updateBrightness()

    #Keeps the brightness in the range [0,1]
    def __boundBrightness(self, brightness:float) -> float:
        if brightness < 0:
            brightness = 0
        elif brightness > 1:
            brightness = 1

        return brightness

    #Performs the actual brightness update, since light's can have different
    #hardware interfaces
    @abstractmethod
    def _updateBrightness(self) -> None:
        pass

    #Gets the brightness of the light when turned on
    def getBrightness(self) -> float:
        return self.__brightness

    #Gets the state(on/off) of the light
    def isActive(self) -> bool:
        return self.__isActive
