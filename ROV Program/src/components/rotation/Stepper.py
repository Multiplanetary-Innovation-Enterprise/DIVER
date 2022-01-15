from abc import ABC, abstractmethod

from components.rotation.Motor import Motor
from components.rotation.RotDirection import RotDirection

#Represents a generic steeper motor
class Stepper(Motor, ABC):
    __stepCount:int = 0       #The number of steps that were taken relative to the start position
    __maxSteps:int = 200      #The maximum steps that can be taken away from the motor
    _isSleeping:bool = False #Whether or not the motor is sleeping
    _stepDelay:float = 0.001 #The delay between each step (correlates to speed)

    def __init__(self, rotDirection:RotDirection):
        super(Motor, self).__init__(rotDirection)

        #Updates the stepper motor's config
        self._updateDirectionState()
        self._updateSleepState()

    #Performs the actual step, which is dependent on the stepper motor's
    #hardware interface
    @abstractmethod
    def _step(self):
        pass

    #Steps the motor once
    def step(self) -> None:
        steps = self.__boundSteps(1)

        #Checks if the next step was in bounds
        if steps > 0:
            self.__steps += self.getRotDirection().value
            self._step()

    #Steps the motor N times
    def stepN(self, steps:int) -> None:
        steps = self.__boundSteps(steps)
        self.__steps += steps * self.getRotDirection().value

        for step in range(steps):
            self._step()

    #Keeps the stepper motor within its constrained assembly
    #TODO Figure out correct math
    def __boundSteps(self, steps:int) -> int:
        stepsSign = 1 #The sign of the steps (pos/neg)

        #Invert the sign for a negative steps value
        if steps < 0:
            stepsSign = -1

        #Calculates the minimum and maxium steps based on the sign of the steps value
        minSteps = self.__stepCount - (stepsSign *steps)
        maxSteps = self.__stepCount + (stepsSign * steps)

        #Checks the rotational direction first
        if self._rotDirection == RotDirection.CLOCKWISE:
            if minSteps < 0:
                steps = 0
            elif maxSteps > self.__maxSteps:
                steps = self.__maxSteps
        elif self._rotDirection == RotDirection.COUNTER_CLOCKWISE:
            steps = self.__maxSteps

        return steps

    #Sets the rotational direction of the stepper
    def setRotDirection(self, rotDirection:RotDirection) -> None:
        super().setRotDirection(rotDirection)

        self._updateDirectionState()

    #Performs the actual direction update, which is dependent on the stepper motor's
    #hardware interface
    @abstractmethod
    def _updateDirectionState(self, rotDirection:RotDirection) -> None:
        pass

    #Gets the number of steps that the stepper motor has taken from its starting position
    def getStepCount(self) -> int:
        return self.__stepCount

    #Resets the step count
    def clearStepCount(self) -> None:
        self.__stepCount = 0

    #Updates the max step limit of the stepper motor
    def setMaxSteps(self, maxSteps:int) -> None:
        self.__maxSteps = maxSteps

    #Gets the maximum steps that the stepper motor can take away from it
    def getMaxSteps(self) -> int:
        return self.__maxSteps

    #Puts the steeper motor to sleep
    def sleep(self) -> None:
        self._isSleeping = True
        self._updateSleepState()

    #Wakes the steeper motor up
    def wake(self) -> None:
        self._isSleeping = False
        self._updateSleepState()

    #Checks whether or not the motor is sleeping
    def isSleeping(self) -> bool:
        return self._isSleeping

    #Performs the actual sleep update, which is dependent on the stepper motor's
    #hardware interface
    @abstractmethod
    def _updateSleepState(self) -> None:
        pass
