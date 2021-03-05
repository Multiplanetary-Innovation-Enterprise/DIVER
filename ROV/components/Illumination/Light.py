from abc import ABC, abstractmethod

class Light(ABC):
    __isOn: bool = None
    __brightness: float = 0

    def turnOn(self) -> None:
        self.setOn(True)

    def turnOff(self) -> None:
        self.setOn(False)

    @abstractmethod
    def setOn(self, on: bool) -> None:
        pass

    @abstractmethod
    def setBrightness(self, brightness:float) -> None:
        pass

    def getBrightness(self) -> float:
        return self.__brightness

    def isOn(self) -> bool:
        return self.__isOn
