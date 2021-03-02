from components.Thruster import Thruster
from util.RotDirection import RotDirection

class PropulsionSubsystem:
    __speed = 0 #Universal speed for all thrusters
    __activeThrusters = [];
    __xThruster = None
    __yThruster = None
    __zThruster = None

    #Constructor for the propulsion subsystem
    def __init__(self, pi):
        #Creates three thrusters. One for each axis.
        self.__xThruster = Thruster(pi, 4, RotDirection.CLOCKWISE)
        self.__yThruster = Thruster(pi, 17, RotDirection.CLOCKWISE)
        self.__zThruster = Thruster(pi, 12, RotDirection.CLOCKWISE)

    #Arms all of the thrusters in the chasis
    def arm(self) -> None:
        self.__xThruster.arm()
        self.__yThruster.arm()
        self.__zThruster.arm()

    #Sets the speed of all three thrusters independently
    def move(self, xSpeed:float, ySpeed:float, zSpeed:float) -> None:
        self.moveX(xSpeed)
        self.moveY(ySpeed)
        self.moveZ(zSpeed)

        self.updateThrusterState(self.__xThruster, speed);
        self.updateThrusterState(self.__yThruster, speed);
        self.updateThrusterState(self.__zThruster, speed);

    #Sets the speed for the thruster mounted on the x-axis
    def moveX(self, speed:float) -> None:
        self.__xThruster.setSpeed(speed)
        self.updateThrusterState(self.__xThruster, speed);

    #Sets the speed for the thruster mounted on the y-axis
    def moveY(self, speed:float)  -> None:
        self.__yThruster.setSpeed(speed)
        self.updateThrusterState(self.__yThruster, speed);

    #Sets the speed for the thruster mounted on the z-axis
    def moveZ(self, speed:float) -> None:
        self.__zThruster.setSpeed(speed)
        self.updateThrusterState(self.__zThruster, speed);

    #Stops all of the thrusters
    def stop(self) -> None:
        self.move(0, 0, 0)

    #Sets the universal speed of the chasis
    def setSpeed(self, speed:float) -> None:
        self.__speed = speed

        #Update the speed of any thrusters currently running
        self.updateActiveThrustersSpeed(self.__speed)

    #Gets the universal speed of the chasis
    def getSpeed(self) -> float:
        return self.__speed

    #Updates the provided thrusters state based on its speed
    def updateThrusterState(self, thruster: Thruster, speed:float) -> None:
        if (speed > 0 or speed < 0) and thruster not in self.__activeThrusters:
            self.__activeThrusters.append(thruster);
        elif speed <= 0 and thruster in self.__activeThrusters:
            self.__activeThrusters.remove(thruster);

    def updateActiveThrustersSpeed(self, speed:float) -> None:
        for thruster in self.__activeThrusters:
            thruster.setSpeed(speed)
