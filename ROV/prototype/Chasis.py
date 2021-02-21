from Thruster import Thruster
from RotDirection import RotDirection

#Represents the chasis of the ROV
class Chasis:
    speed = 0 #Universal speed for all thrusters
    activeThrusters = [];

    #Constructor for Chasis
    def __init__(self, pi):
        #Creates three thrusters. One for each axis.
        self.xThruster = Thruster(pi, 4, RotDirection.Clockwise)
        self.yThruster = Thruster(pi, 17, RotDirection.Clockwise)
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
        self.updateThrusterState(self.xThruster, speed);

    #Sets the speed for the thruster mounted on the y-axis
    def moveY(self, speed):
        self.yThruster.setSpeed(speed)
        self.updateThrusterState(self.yThruster, speed);

    #Sets the speed for the thruster mounted on the z-axis
    def moveZ(self, speed):
        self.zThruster.setSpeed(speed)
        self.updateThrusterState(self.zThruster, speed);

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
        print("Active thrusters: " + str(len(self.activeThrusters)) + "\n");
        self.speed += speed

        #Update the speed of any thrusters currently running
        self.updateActiveThrustersSpeed(self.speed)

    #Decreases the universal speed of the chasis by the specified amount
    def decreaseSpeed(self, speed):
        self.speed -= speed

        #Update the speed of any thrusters currently running
        self.updateActiveThrustersSpeed(self.speed)

    def updateThrusterState(self, thruster: Thruster, speed):
        if (speed > 0 or speed < 0) and thruster not in self.activeThrusters:
            self.activeThrusters.append(thruster);
        elif speed <= 0 and thruster in self.activeThrusters:
            self.activeThrusters.remove(thruster);

    def updateActiveThrustersSpeed(self, speed):
        print("Updating active thrusters\n");
        for thruster in self.activeThrusters:
            print("Updating thruster..... speed: " + str(speed) + "\n");
            thruster.setSpeed(speed)
