from abc import ABC, abstractmethod

from components.rotation.Motor import Motor
from components.rotation.RotDirection import RotDirection

#Represents a generic servo motor
class Servo(Motor):
    __angle:float = 0      #The angle that the servo is curently at
    __minAngle:float = 0   #The minimum angle in degrees
    __maxAngle:float = 180 #The maximum angle in degrees

    def __init__(self, rotDirection:RotDirection):
        super().__init__(rotDirection)

    #Sets the angle of the servo
    def setAngle(self, angle:float) -> None:
        self.__angle = self.__boundAngle(angle)

        self._updateAngle()

    #Keeps the angle in the range [minAngle,maxAngle]
    def __boundAngle(self, angle:float) -> float:
        if angle > self.__maxAngle:
            angle = self.__maxAngle
        elif angle < self.__minAngle:
            angle = self.__minAngle

        return angle

    #Performs the actual angle update, since servos can have different
    #hardware interfaces
    @abstractmethod
    def _updateAngle(self) -> None:
        pass

    #Gets the angle that the servo is at
    def getAngle(self) -> float:
        return self.__angle

    #Sets the minium angle that the servo can move to
    def setMinAngle(self, angle:float) -> None:
        self.__minAngle = angle

    #Gets the minium angle that the servo can move to
    def getMinAngle(self) -> float:
        return self.__minAngle

    #Sets the maximum angle that the servo can move to
    def setMaxAngle(self, angle:float) -> None:
        self.__maxAngle = angle

    #Gets the maxiumum angle that the servo can move to
    def getMaxAngle(self) -> float:
        return self.__maxAngle
