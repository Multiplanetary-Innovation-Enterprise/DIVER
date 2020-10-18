from RotDirection import RotDirection

import time

class Thruster:
    maxReverse = 1100
    maxForward = 1900
    stopped = 1500

    def __init__(self, pi, pinNum, rotDirection):
        self.pi = pi
        self.pinNum = pinNum
        self.rotDirection = rotDirection
        self.speed = 0

    def arm(self):
        self.pi.set_servo_pulsewidth(self.pinNum, 0)
        time.sleep(1)

        self.pi.set_servo_pulsewidth(self.pinNum, self.stopped)
        time.sleep(1)

    def setSpeed(self, speed):
        speed = self.rotDirection.value * speed
        self.speed = Thruster.stopped + ((Thruster.maxForward - Thruster.maxReverse) / 2) * speed

        if self.speed >  Thruster.maxForward or self.speed < Thruster.maxReverse:
            return

        self.pi.set_servo_pulsewidth(self.pinNum, self.speed)

    def getSpeed(self):
        return self.speed

    def stop(self):
        self.pi.set_servo_pulsewidth(self.pinNum, self.stopped)
        self.speed = self.stopped

    def setRotDirection(self, rotDirection):
        self.rotDirection = rotDirection

    def getRotDirection(self):
        return self.rotDirection

    def brake(linearSpeed): pass
