from util.RotDirection import RotDirection

import time

#Represents a thruster
class Thruster:
    MAX_REVERSE = 1100 #Max reverse PWM pulse width
    MAX_FORWARD = 1900 #Max forward PWM pulse width
    STOPPED = 1500    #Stopped PWM pulse width
    __rotDirection = RotDirection.CLOCKWISE
    __speed = 0

    #Creates the thruster
    def __init__(self, pi, pinNum, rotDirection):
        self.pi = pi
        self.pinNum = pinNum
        self.__rotDirection = rotDirection

    #Performs the arming sequence for the thruster
    def arm(self):
        self.pi.set_servo_pulsewidth(self.pinNum, 0)
        time.sleep(1)

        self.pi.set_servo_pulsewidth(self.pinNum, self.stopped)
        time.sleep(1)

    #Sets the speed of the thruster. Range [-1,1]
    def setSpeed(self, speed):
        #Set the direction of the thruster
        speed = self.__rotDirection.value * speed
        #Converts the range [-1,1] to the actual PWM range
        self.__speed = Thruster.STOPPED + ((Thruster.MAX_FORWARD - Thruster.MAX_REVERSE) / 2) * speed
        #Stops if the speed is outide of the limits

        if self.__speed > Thruster.MAX_FORWARD or self.__speed < Thruster.MAX_REVERSE:
            return

        self.pi.set_servo_pulsewidth(self.pinNum, self.__speed)

    #Gets the speed of the thruster
    def getSpeed(self):
        return self.__speed

    #Stops the thruster
    def stop(self):
        self.pi.set_servo_pulsewidth(self.pinNum, Thruster.STOPPED)
        self.__speed = Thruster.STOPPED

    #Sets the rotational speed of the thruster
    def setRotDirection(self, rotDirection):
        self.__rotDirection = rotDirection

    #Gets the rotational speed of the thruster
    def getRotDirection(self):
        return self.__rotDirection
