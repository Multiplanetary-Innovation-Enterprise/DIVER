from Thruster import Thruster
from RotDirection import RotDirection

#Represents the chasis of the ROV
class Chasis:
    speed = 0 #Universal speed for all thrusters

    #Constructor for Chasis
    def __init__(self, pi):
        #Creates three thrusters. One for each axis.
        self.xThruster = Thruster(pi, 4, RotDirection.Clockwise)
        self.yThruster = Thruster(pi, 5, RotDirection.Clockwise)
        self.zThruster = Thruster(pi, 12, RotDirection.Clockwise)

    #Arms all of the thrusters in the chasis
    def arm(self):
        self.xThruster.arm()
        self.yThruster.arm()
        self.zThruster.arm()

    #Sets the speed of all three thrusters independently
    def move(self, xSpeed, ySpeed, zSpeed):
        self.moveX(xSpeed)
        self.moveY(ySpeed)
        self.moveZ(zSpeed)

    #Sets the speed for the thruster mounted on the x-axis
    def moveX(self, speed):
        self.xThruster.setSpeed(speed)

        #Sets the speed for the thruster mounted on the y-axis
    def moveY(self, speed):
        self.yThruster.setSpeed(speed)

    #Sets the speed for the thruster mounted on the z-axis
    def moveZ(self, speed):
        self.zThruster.setSpeed(speed)

    #Stops all of the thrusters
    def stop(self):
        self.move(0, 0, 0)

    #Sets the universal speed of the chasis
    def setSpeed(self, speed):
        self.speed = speed

    #Gets the universal speed of the chasis
    def getSpeed(self):
        return round(self.speed, 2)

    #Increases the universal speed of the chasis by the specified amount
    def increaseSpeed(self, speed):
        self.speed += speed

    #Decreases the universal speed of the chasis by the specified amount
    def decreaseSpeed(self, speed):
        self.speed -= speed
