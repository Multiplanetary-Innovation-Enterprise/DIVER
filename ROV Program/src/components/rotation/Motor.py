from abc import ABC

from components.rotation.RotDirection import RotDirection

class Motor(ABC):
    __rotDirection:RotDirection = None

    def __init__(self, rotDirection:RotDirection):
        self.__rotDirection = rotDirection

    #Sets the rotational direction of the motor
    def setRotDirection(self, rotDirection:RotDirection) -> None:
        self.__rotDirection = rotDirection

    #Gets the rotational direction of the motor
    def getRotDirection(self) -> RotDirection:
        return self.__rotDirection
