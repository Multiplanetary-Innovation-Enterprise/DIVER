from abc import ABC

from util.RotDirection import RotDirection

class Motor(ABC):
    __rotDirection = None

    def __init__(self, rotDirection:RotDirection):
        self.__rotDirection = rotDirection

    #Sets the rotational speed of the thruster
    def setRotDirection(self, rotDirection:RotDirection):
        self.__rotDirection = rotDirection

    #Gets the rotational speed of the thruster
    def getRotDirection(self):
        return self.__rotDirection
