from abc import ABC, abstractmethod

from components.rotation.RotDirection import RotDirection

#Represents a generic motor
class Motor(ABC):
    _rotDirection:RotDirection = None #The direction that the motor rotates in
    _speed:float = 0                  #The speed at which the motor rotates

    def __init__(self, rotDirection:RotDirection):
        self._rotDirection = rotDirection

    #Sets the rotational direction of the motor
    def setRotDirection(self, rotDirection:RotDirection) -> None:
        self._rotDirection = rotDirection

    #Gets the rotational direction of the motor
    def getRotDirection(self) -> RotDirection:
        return self._rotDirection

    #Sets the speed of the thruster. Range [-1,1]
    def setSpeed(self, speed:float) -> None:
        self._speed = self.__boundSpeed(speed)

        #Performs the speed update
        self._updateSpeed()

    #Keeps the speed in the range [-1,1]
    def __boundSpeed(self, speed:float) -> float:
        if speed > 1:
            speed = 1
        elif speed < -1:
            speed = -1

        return speed

    #Performs the actual speed update, since motors can have different
    #hardware interfaces
    @abstractmethod
    def _updateSpeed(self) -> None:
        pass

    #Gets the speed of the thruster
    def getSpeed(self) -> float:
        return self._speed
