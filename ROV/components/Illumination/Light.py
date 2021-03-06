from abc import ABC, abstractmethod

class Light(ABC):
    __isOn: bool = None
    __currentBrightness: float = 0
    __lastBrightness: float = 0

    def turnOn(self) -> None:
        self.setOn(True)

    def turnOff(self) -> None:
        self.setOn(False)

    @abstractmethod
    def setOn(self, on: bool) -> None:
        pass

    def setBrightness(self, brightness:float) -> None:
        currentBrightness = self.getBrightness()

        self.setLastBrightness(currentBrightness)

        if brightness < 0:
            brightness = 0
        elif brightness > 1:
            brightness = 1

        self.__currentBrightness = brightness

    def getBrightness(self) -> float:
        return self.__currentBrightness

    def setLastBrightness(self, brightness:float) -> None:
        self.__lastBrightness = brightness

    def getLastBrightness(self) -> float:
        return self.__lastBrightness

    def isOn(self) -> bool:
        return self.__isOn
