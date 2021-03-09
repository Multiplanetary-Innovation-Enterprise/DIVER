from components.Thruster import Thruster
from util.RotDirection import RotDirection

class PropulsionSubsystem:
    __speed = 0.1 #Universal speed for all thrusters
    __activeThrusters = [];
    __leftThruster = None
    __rightThruster = None
    __topThruster = None

    #Constructor for the propulsion subsystem
    def __init__(self, pi):
        #Creates three thrusters. Two for the x-y movement and one for z movement
        self.__leftThruster = Thruster(pi, 4, RotDirection.CLOCKWISE)
        self.__rightThruster = Thruster(pi, 17, RotDirection.CLOCKWISE)
        self.__topThruster = Thruster(pi, 12, RotDirection.CLOCKWISE)

    #Arms all of the thrusters in the chasis
    def arm(self) -> None:
        self.__leftThruster.arm()
        self.__rightThruster.arm()
        self.__topThruster.arm()

    #Sets the speed of all three thrusters independently
    def move(self, leftSpeed:float, rightSpeed:float, verticalSpeed:float) -> None:
        self.moveLeft(leftSpeed)
        self.moveRight(rightSpeed)
        self.moveVertical(topSpeed)

        self.updateThrusterState(self.__leftThruster, speed);
        self.updateThrusterState(self.__rightThruster, speed);
        self.updateThrusterState(self.__topThruster, speed);

    #Sets the speed for the thruster mounted on the left side of the ROV
    def moveLeft(self, speed:float) -> None:
        self.__leftThruster.setSpeed(speed)
        self.updateThrusterState(self.__leftThruster, speed);

    #Sets the speed for the thruster mounted on the right side of the ROV
    def moveRight(self, speed:float) -> None:
        self.__rightThruster.setSpeed(speed)
        self.updateThrusterState(self.__rightThruster, speed);

    #Sets the speed for the thruster mounted on the top of the ROV
    def moveVertical(self, speed:float) -> None:
        self.__topThruster.setSpeed(speed)
        self.updateThrusterState(self.__topThruster, speed);

    #Stops all of the thrusters
    def stop(self) -> None:
        self.move(0, 0, 0)

    #Sets the universal speed of the chasis
    def setSpeed(self, speed:float) -> None:
        self.__speed = speed

        #Update the speed of any thrusters currently running
        self.updateActiveThrustersSpeed(self.__speed)

    #Gets the current speed of the propulsion subsystem
    def getSpeed(self) -> float:
        return self.__speed

    #Updates the provided thruster's state based on its speed
    def updateThrusterState(self, thruster: Thruster, speed:float) -> None:
        if (speed > 0 or speed < 0) and thruster not in self.__activeThrusters:
            self.__activeThrusters.append(thruster);
        elif speed <= 0 and thruster in self.__activeThrusters:
            self.__activeThrusters.remove(thruster);

    #Updates the speeds of the thrusters that are currently running
    def updateActiveThrustersSpeed(self, speed:float) -> None:
        for thruster in self.__activeThrusters:
            thruster.setSpeed(speed)
