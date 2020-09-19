import time

class Thruster:
    maxReverse = 1100
    maxForward = 1900
    stopped = 1500

    def __init__(self, pi, pinNum, rotDirection):
        self.pi = pi
        self.pinNum = pinNum
        self.rotDirection = rotDirection

        pi.set_servo_pulsewidth(pinNum, 0)

    def arm(self):
        print("arming")
        self.pi.set_servo_pulsewidth(self.pinNum, 0)
        time.sleep(1)
        self.pi.set_servo_pulsewidth(self.pinNum, Thruster.maxForward)
        time.sleep(1)
        self.pi.set_servo_pulsewidth(self.pinNum, Thruster.maxReverse)
        time.sleep(2)
        self.pi.set_servo_pulsewidth(self.pinNum, 1500)
        time.sleep(2)

    # def setUp(self):
    #
    # def setSpeed(self, speed):
    #
    # def getSpeed(self):
    #
    # dep stop():
    #
    # def setDirection(self, rotDirection):
    #
    # def getDirection(self):
