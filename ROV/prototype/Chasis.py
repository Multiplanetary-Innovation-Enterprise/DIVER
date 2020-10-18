from Thruster import Thruster
from RotDirection import RotDirection
from KeyboardInput import KeyboardInput

class Chasis:
    def __init__(self, pi):
        self.xThruster = Thruster(pi, 4, RotDirection.Clockwise)
        self.yThruster = Thruster(pi, 5, RotDirection.Clockwise)
        self.zThruster = Thruster(pi, 12, RotDirection.Clockwise)

    def arm(self):
        self.xThruster.arm()
        self.yThruster.arm()
        self.zThruster.arm()

    def move(self, xSpeed, ySpeed, zSpeed):
        self.moveX(xSpeed)
        self.moveY(ySpeed)
        self.moveZ(zSpeed)

    def moveX(self, speed):
        self.xThruster.setSpeed(speed)

    def moveY(self, speed):
        self.yThruster.setSpeed(speed)

    def moveZ(self, speed):
        self.zThruster.setSpeed(speed)

    def stop(self):
        self.move(0, 0, 0)
