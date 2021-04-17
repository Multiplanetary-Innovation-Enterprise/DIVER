from signals.PWMSignal import PWMSignal
from components.Motor import Motor

import time

#Represents a thruster
class Thruster(Motor):
    MAX_REVERSE = 1100 #Max reverse PWM pulse width
    MAX_FORWARD = 1900 #Max forward PWM pulse width
    STOPPED = 1500    #Stopped PWM pulse width
    __pwmSignal: PWMSignal = None
    __speed = 0

    #Creates the thruster
    def __init__(self, pi, pinNum, rotDirection):
        super().__init__(rotDirection)

        self.__pwmSignal = PWMSignal(pi, pinNum)

    #Performs the arming sequence for the thruster
    def arm(self) -> None:
        self.__pwmSignal.setPulseWidth(0)
        time.sleep(1)

        self.__pwmSignal.setPulseWidth(Thruster.STOPPED)
        time.sleep(1)

    #Sets the speed of the thruster. Range [-1,1]
    def setSpeed(self, speed:float) -> None:
        if speed > 1:
            speed = 1
        elif speed < -1:
            speed = -1

        self.__speed = speed

        pulseWidth = self.__convertSpeedToPulsewidth(speed)

        self.__pwmSignal.setPulseWidth(pulseWidth)

    def __convertSpeedToPulsewidth(self, speed:float) -> int:
        #Set the direction of the thruster
        speed = self.getRotDirection().value * speed
        #Converts the range [-1,1] to the actual PWM range
        pulseWidth = round(Thruster.STOPPED + ((Thruster.MAX_FORWARD - Thruster.MAX_REVERSE) / 2) * speed)

        return pulseWidth

    #Gets the speed of the thruster
    def getSpeed(self) -> float:
        return self.__speed

    #Stops the thruster
    def stop(self) -> None:
        self.__pwmSignal.setPulseWidth(Thruster.STOPPED)
        self.__speed = Thruster.STOPPED
