from RotDirection import RotDirection

import time

#Represents a thruster
class Thruster:
    maxReverse = 1100 #Max reverse PWM pulse width
    maxForward = 1900 #Max forward PWM pulse width
    stopped = 1500    #Stopped PWM pulse width

    #Creates the thruster
    def __init__(self, pi, pinNum, rotDirection):
        self.pi = pi
        self.pinNum = pinNum
        self.rotDirection = rotDirection
        self.speed = 0

    #Performs the arming sequence for the thruster
    def arm(self):
        self.pi.set_servo_pulsewidth(self.pinNum, 0)
        time.sleep(1)

        self.pi.set_servo_pulsewidth(self.pinNum, self.stopped)
        time.sleep(1)

    #Sets the speed of the thruster. Range [-1,1]
    def setSpeed(self, speed):
        #Set the direction of the thruster
        speed = self.rotDirection.value * speed
        #Converts the range [-1,1] to the actual PWM range
        self.speed = Thruster.stopped + ((Thruster.maxForward - Thruster.maxReverse) / 2) * speed
        #Stops if the speed is outide of the limits
        if self.speed > Thruster.maxForward or self.speed < Thruster.maxReverse:
            return

        self.pi.set_servo_pulsewidth(self.pinNum, self.speed)

    #Gets the speed of the thruster
    def getSpeed(self):
        return self.speed

    #Stops the thruster
    def stop(self):
        self.pi.set_servo_pulsewidth(self.pinNum, self.stopped)
        self.speed = self.stopped

    #Sets the rotational speed of the thruster
    def setRotDirection(self, rotDirection):
        self.rotDirection = rotDirection

    #Gets the rotational speed of the thruster
    def getRotDirection(self):
        return self.rotDirection

    #Brakes the thruster
    def brake(linearSpeed): pass
