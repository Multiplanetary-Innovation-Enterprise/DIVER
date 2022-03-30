from subsystems.Subsystem import Subsystem
from components.controllers.Controller import Controller
from components.rotation.Thruster import Thruster
from components.rotation.RotDirection import RotDirection

#Represents the subsystem for controlling propulsion
class PropulsionSubsystem(Subsystem):
    __leftThruster:Thruster = None     #The thruster mounted on the left side of the ROV
    __rightThruster:Thruster = None    #The thruster mounted on the right side of the ROV
    __topFrontThruster:Thruster = None #The thruster mounted on the top front side of the ROV
    __topBackThruster:Thruster = None  #The thruster mounted on the top back side of the ROV

    def __init__(self, controller:Controller, config):
        super().__init__(controller, config)

        #Gets the GPIO pins for the thrusters
        leftPin = int(config['Propulsion']['LeftThrusterPin'])
        rightPin = int(config['Propulsion']['RightThrusterPin'])
        topFrontPin = int(config['Propulsion']['TopFrontThrusterPin'])
        topBackPin = int(config['Propulsion']['TopBackThrusterPin'])

        #Creates three thrusters. Two for the x-y movement and two for z movement
        self.__leftThruster = Thruster(controller, leftPin, RotDirection.COUNTER_CLOCKWISE)
        self.__rightThruster = Thruster(controller, rightPin, RotDirection.COUNTER_CLOCKWISE)
        self.__topFrontThruster = Thruster(controller, topFrontPin, RotDirection.CLOCKWISE)
        self.__topBackThruster = Thruster(controller, topBackPin, RotDirection.COUNTER_CLOCKWISE)

    #Arms all of the thrusters
    def arm(self) -> None:
        print("Arming thrusters!!!!!")
        self.__leftThruster.arm()
        self.__rightThruster.arm()
        self.__topFrontThruster.arm()
        self.__topBackThruster.arm()

    #Sets the speed of all three thrusters independently
    def setSpeed(self, leftSpeed:float, rightSpeed:float, frontSpeed:float, backSpeed:float) -> None:
        self.setXYSpeed(leftSpeed, rightSpeed)
        self.setVerticalSpeed(frontSpeed, rightSpeed)

    #Sets all the thrusters to the same speed (python does not allow function overloading)
    def setSpeedSame(self, speed:float) -> None:
        self.setSpeed(speed,speed,speed,speed)

    #Sets the speed of the thrusters mountd in the XY plane
    def setXYSpeed(self, leftSpeed:float, rightSpeed:float) -> None:
        self.__leftThruster.setSpeed(leftSpeed)
        self.__rightThruster.setSpeed(rightSpeed)

    #Sets the XY thrusters to the same speed (python does not allow function overloading)
    def setXYSpeedSame(self, speed:float) -> None:
        self.setXYSpeed(speed, speed)

    #Sets the speed of the thrusters mounted vertically
    def setVerticalSpeed(self, frontSpeed:float, backSpeed:float) -> None:
        self.__topFrontThruster.setSpeed(frontSpeed)
        self.__topBackThruster.setSpeed(backSpeed)

    #Sets the vertical thrusters to the same speed (python does not allow function overloading)
    def setVerticalSpeedSame(self, speed:float) -> None:
        self.setVerticalSpeed(speed, speed)

    #Gets the speeds of all the thrusters
    def getSpeeds(self) -> list:
        speeds = [
            self.__leftThruster.getSpeed(),
            self.__rightThruster.getSpeed(),
            self.__topFrontThruster.getSpeed(),
            self.__topBackThruster.getSpeed()
        ]

        return speeds

    #Gets the speeds of the thrusters mounted in the XY plane
    def getXYSpeeds(self) -> list:
        speeds = [
            self.__leftThruster.getSpeed(),
            self.__rightThruster.getSpeed()
        ]

        return speeds

    #Gets the speeds of the vertical thrusters
    def getVerticalSpeeds(self) -> list:
        speeds = [
            self.__topFrontThruster.getSpeed(),
            self.__topBackThruster.getSpeed()
        ]

        return speeds

    #Stops all of the thrusters
    def stop(self) -> None:
        self.setStates(False, False, False, False)

    #Sets the rotational direction for all thrusters
    def setRotDirections(self, leftRotDir:RotDirection, rightRotDir:RotDirection, frontRotDir:RotDirection, backRotDir:RotDirection) -> None:
        self.setRotDirectionsXY(leftRotDir, rightRotDir)
        self.setRotDirectionsZ(frontRotDir, backRotDir)

    #Sets the rotational direction for the thrusters in the XY plane
    def setXYRotDirections(self, leftRotDir:RotDirection, rightRotDir:RotDirection) -> None:
        self.__leftThruster.setRotDirection(leftRotDir)
        self.__rightThruster.setRotDirection(rightRotDir)

    #Sets the rotational direction for the vertical thrusters
    def setZRotDirections(self, frontRotDir:RotDirection, backRotDir:RotDirection) -> None:
        self.__topFrontThruster.setRotDirection(frontRotDir)
        self.__topBackThruster.setRotDirection(backRotDir)

    #Gets the rotation directions of all the thrusters
    def getRotDirections(self) -> list:
        dirs = [
            self.__leftThruster.getRotDirection(),
            self.__rightThruster.getRotDirection(),
            self.__topFrontThruster.getRotDirection(),
            self.__topBackThruster.getRotDirection()
        ]

        return dirs

    #Sets the states of all the thrusters(active/not-active)
    def setStates(self, leftActive:bool, rightActive:bool, frontActive:bool, backActive:bool) -> None:
        self.setXYStates(leftActive, rightActive)
        self.setZStates(frontActive, backActive)

    #Sets the states of all the thrusters in the XY plane(active/not-active)
    def setXYStates(self, leftActive:bool, rightActive:bool) -> None:
        self.__leftThruster.setState(leftActive)
        self.__rightThruster.setState(rightActive)

    #Sets the states of the vertical thrusters(active/not-active)
    def setZStates(self, frontActive:bool, backActive:bool) -> None:
        self.__topFrontThruster.setState(frontActive)
        self.__topBackThruster.setState(backActive)

    #Gets the states of all the thrusters
    def getStates(self) -> list:
        states = [
            self.__leftThruster.isActive(),
            self.__rightThruster.isActive(),
            self.__topFrontThruster.isActive(),
            self.__topBackThruster.isActive()
        ]

        return states

    #Gets the the thruster mounted on the left side of the ROV
    def getLeftThruster(self) -> Thruster:
        return self.__leftThruster

    #Gets the the thruster mounted on the right side of the ROV
    def getRightThruster(self) -> Thruster:
        return self.__rightThruster

    #Gets the the thruster mounted on the top front side of the ROV
    def getTopFrontThruster(self) -> Thruster:
        return self.__topFrontThruster

    #Gets the the thruster mounted on the top back side of the ROV
    def getTopBackThruster(self) -> Thruster:
        return self.__topBackThruster

    #Performs any clean up on system shutdown
    def shutdown(self) -> None:
        self.stop()
