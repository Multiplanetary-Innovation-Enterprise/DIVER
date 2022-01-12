from abc import ABC, abstractmethod

#Represents a generic light
class Light(ABC):
    __isOn:bool = False      #Whether or not the light is currently turned on
    __brightness:float = 0.1 #The brightness of the light when turned on

    #Turns the light on to its current brightness
    def turnOn(self) -> None:
        self.__isOn = True
        self.setState(True)

    #Turns the light off
    def turnOff(self) -> None:
        self.__isOn = False
        self.setState(False)

    #Updates the state(on/off) of the light
    @abstractmethod
    def setState(self, isOn:bool) -> None:
        pass

    #Sets the brightness of the light
    def setBrightness(self, brightness:float) -> None:
        #Keeps the brightness in the range [0,1]
        if brightness < 0:
            brightness = 0
        elif brightness > 1:
            brightness = 1

        self.__brightness = brightness

        #Updates the state of the light based on the new brightness
        if brightness == 0:
            self.turnOff()
        else:
            self.turnOn()

    #Gets the brightness of the light when turned on
    def getBrightness(self) -> float:
        return self.__brightness

    #Gets the state(on/off) of the light
    def isOn(self) -> bool:
        return self.__isOn
