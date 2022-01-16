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
        self.__leftThruster = Thruster(controller, leftPin, RotDirection.CLOCKWISE)
        self.__rightThruster = Thruster(controller, rightPin, RotDirection.CLOCKWISE)
        self.__topFrontThruster = Thruster(controller, topFrontPin, RotDirection.CLOCKWISE)
        self.__topBackThruster = Thruster(controller, topBackPin, RotDirection.CLOCKWISE)

    #Arms all of the thrusters
    def arm(self) -> None:
        self.__leftThruster.arm()
        self.__rightThruster.arm()
        self.__topFrontThruster.arm()
        self.__topBackThruster.arm()

    #Sets the speed of all three thrusters independently
    def setSpeed(self, leftSpeed:float, rightSpeed:float, verticalSpeed:float, frontSpeed:float, backSpeed:float) -> None:
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
        self.setSpeed(0, 0, 0, 0)

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
        pass
