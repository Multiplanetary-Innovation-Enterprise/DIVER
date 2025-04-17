from subsystems.Subsystem import Subsystem
from components.controllers.Controller import Controller
from components.rotation.Thruster import Thruster
from components.rotation.RotDirection import RotDirection

#Represents the subsystem for controlling propulsion
class PropulsionSubsystem(Subsystem):
    __FrontLeftThruster:Thruster = None     #The thruster mounted on the front left side of the ROV
    __FrontRightThruster:Thruster = None    #The thruster mounted on the front right side of the ROV
    __BackLeftThruster:Thruster = None     #The thruster mounted on the back left side of the ROV
    __BackRightThruster:Thruster = None    #The thruster mounted on the back right side of the ROV
    __TopBackThruster:Thruster = None #The thruster mounted on the top front side of the ROV
    __TopFrontThruster:Thruster = None  #The thruster mounted on the top back side of the ROV
    

    def __init__(self, controller:Controller, config):
        super().__init__(controller, config)

        #Gets the GPIO pins for the thrusters
        frontLeftPin  = int(config['Propulsion']['FrontLeftThrusterPin'])
        frontRightPin = int(config['Propulsion']['FrontRightThrusterPin'])
        backLeftPin   = int(config['Propulsion']['BackLeftThrusterPin'])
        backRightPin  = int(config['Propulsion']['BackRightThrusterPin'])
        topBackPin    = int(config['Propulsion']['TopBackThrusterPin'])
        topFrontPin   = int(config['Propulsion']['TopFrontThrusterPin'])

        #Creates three thrusters. Two for the x-y movement and two for z movement
        self.__FrontLeftThruster  = Thruster(controller, frontLeftPin, RotDirection.CLOCKWISE)
        self.__FrontRightThruster = Thruster(controller, frontRightPin, RotDirection.CLOCKWISE)   
        self.__BackLeftThruster   = Thruster(controller, backLeftPin, RotDirection.CLOCKWISE)
        self.__BackRightThruster  = Thruster(controller, backRightPin, RotDirection.CLOCKWISE)

        self.__TopBackThruster  = Thruster(controller, topBackPin, RotDirection.CLOCKWISE)
        self.__TopFrontThruster = Thruster(controller, topFrontPin, RotDirection.CLOCKWISE)

    #Arms all of the thrusters
    def arm(self) -> None:
        print("Arming thrusters!!!!!")
        self.__FrontLeftThruster.arm()
        self.__FrontRightThruster.arm()
        self.__BackLeftThruster.arm()
        self.__BackRightThruster.arm()
        self.__TopBackThruster.arm()
        self.__TopFrontThruster.arm()
        
    #Sets the speed of all three thrusters independently
    #0 = TopFront, 1 = TopBack, 2 = FrontLeft, 3 = BackLeft, 4 = FrontRight, 5 = BackRight
    def setSpeed(self, TopFrontSpeed:float, TopBackSpeed:float, FrontLeftSpeed:float, BackLeftSpeed:float, FrontRightSpeed:float, BackRightSpeed:float) -> None:
        
        self.setXYSpeed(FrontLeftSpeed, BackLeftSpeed, FrontRightSpeed, BackRightSpeed)
        self.setVerticalSpeed(TopFrontSpeed, TopBackSpeed)

    #Sets all the thrusters to the same speed (python does not allow function overloading)
    def setSpeedSame(self, speed:float) -> None:
        self.setSpeed(speed,speed,speed,speed, speed, speed)

    #Sets the speed of the thrusters mountd in the XY plane
    def setXYSpeed(self, FrontLeftSpeed:float, BackLeftSpeed:float, FrontRightSpeed:float, BackRightSpeed:float) -> None:
        self.__FrontRightThruster.setSpeed(FrontRightSpeed)
        self.__FrontLeftThruster.setSpeed(FrontLeftSpeed)
        self.__BackRightThruster.setSpeed(BackRightSpeed)
        self.__BackLeftThruster.setSpeed(BackLeftSpeed)

    #Sets the XY thrusters to the same speed (python does not allow function overloading)
    def setXYSpeedSame(self, speed:float) -> None:
        self.setXYSpeed(speed, speed, speed, speed)

    #Sets the speed of the thrusters mounted vertically
    def setVerticalSpeed(self, TopFrontSpeed:float, TopBackSpeed:float) -> None:
        self.__TopFrontThruster.setSpeed(TopFrontSpeed)
        self.__TopBackThruster.setSpeed(TopBackSpeed)

    #Sets the vertical thrusters to the same speed (python does not allow function overloading)
    def setVerticalSpeedSame(self, speed:float) -> None:
        self.setVerticalSpeed(speed, speed)

    #Gets the speeds of all the thrusters
     #0 = TopFront, 1 = TopBack, 2 = FrontLeft, 3 = BackLeft, 4 = FrontRight, 5 = BackRight
    def getSpeeds(self) -> list:
        speeds = [
            self.__TopFrontThruster.getSpeed(),
            self.__TopBackThruster.getSpeed(),
            self.__FrontLeftThruster.getSpeed(),
            self.__BackLeftThruster.getSpeed(),
            self.__FrontRightThruster.getSpeed(),
            self.__BackRightThruster.getSpeed()
        ]

        return speeds

    #Gets the flat speed of the thrusters to undo 76% adjustment, use Top thrusters sine they are never multipled by 0.76
    def getFlatSpeeds(self) -> list:
        speeds = [
            self.__TopFrontThruster.getSpeed(),
            self.__TopBackThruster.getSpeed(),
            self.__TopFrontThruster.getSpeed(),
            self.__TopBackThruster.getSpeed(),
            self.__TopFrontThruster.getSpeed(),
            self.__TopBackThruster.getSpeed()
        ]

        return speeds

    #Gets the speeds of the vertical thrusters
    def getVerticalSpeeds(self) -> list:
        speeds = [
            self.__TopFrontThruster.getSpeed(),
            self.__TopBackThruster.getSpeed()
        ]

        return speeds

    #Stops all of the thrusters
    def stop(self) -> None:
        self.setStates(False, False, False, False, False, False)

     #0 = TopFront, 1 = TopBack, 2 = FrontLeft, 3 = BackLeft, 4 = FrontRight, 5 = BackRight
    #Sets the rotational direction for all thrusters
    def setRotDirections(self, TopFrontRotDir:RotDirection, TopBackRotDir:RotDirection, FrontLeftRotDir:RotDirection, BackLeftRotDir:RotDirection, FrontRightRotDir:RotDirection,  BackRightRotDir:RotDirection) -> None:
        self.setXYRotDirections(FrontLeftRotDir, BackLeftRotDir, FrontRightRotDir, BackRightRotDir)
        self.setZRotDirections(TopFrontRotDir, TopBackRotDir)

    #Sets the rotational direction for the thrusters in the XY plane
    def setXYRotDirections(self, FrontLeftRotDir:RotDirection, BackLeftRotDir:RotDirection, FrontRightRotDir:RotDirection,  BackRightRotDir:RotDirection) -> None:
        self.__FrontLeftThruster.setRotDirection(FrontLeftRotDir)
        self.__FrontRightThruster.setRotDirection(FrontRightRotDir)
        self.__BackLeftThruster.setRotDirection(BackLeftRotDir)
        self.__BackRightThruster.setRotDirection(BackRightRotDir)
        
    #Sets the rotational direction for the vertical thrusters
    def setZRotDirections(self, TopFrontRotDir:RotDirection, TopBackRotDir:RotDirection) -> None:
        self.__TopFrontThruster.setRotDirection(TopFrontRotDir)
        self.__TopBackThruster.setRotDirection(TopBackRotDir)

    #Gets the rotation directions of all the thrusters
    def getRotDirections(self) -> list:
        dirs = [
            self.__TopFrontThruster.getRotDirection(),
            self.__TopBackThruster.getRotDirection(),
            self.__FrontLeftThruster.getRotDirection(),
            self.__BackLeftThruster.getRotDirection(),
            self.__FrontRightThruster.getRotDirection(),
            self.__BackRightThruster.getRotDirection()
        ]

        return dirs

    #0 = TopFront, 1 = TopBack, 2 = FrontLeft, 3 = BackLeft, 4 = FrontRight, 5 = BackRight
    #Sets the states of all the thrusters(active/not-active)
    def setStates(self, TopFrontActive:bool, TopBackActive:bool, FrontLeftActive:bool, BackLeftActive:bool, FrontRightActive:bool,  BackRightActive:bool) -> None:
        self.setXYStates(FrontLeftActive,  BackLeftActive, FrontRightActive, BackRightActive)
        self.setZStates(TopFrontActive, TopBackActive)

    #Sets the states of all the thrusters in the XY plane(active/not-active)
    def setXYStates(self, FrontLeftActive:bool, BackLeftActive:bool, FrontRightActive:bool, BackRightActive:bool) -> None:
        self.__FrontRightThruster.setState(FrontRightActive)
        self.__FrontLeftThruster.setState(FrontLeftActive)
        self.__BackRightThruster.setState(BackRightActive)
        self.__BackLeftThruster.setState(BackLeftActive)


    #Sets the states of the vertical thrusters(active/not-active)
    def setZStates(self, TopFrontActive:bool, TopBackActive:bool) -> None:
        self.__TopFrontThruster.setState(TopFrontActive)
        self.__TopBackThruster.setState(TopBackActive)

    #Gets the states of all the thrusters
    def getStates(self) -> list:
        states = [
            self.__TopFrontThruster.isActive(),
            self.__TopBackThruster.isActive(),
            self.__FrontLeftThruster.isActive(),
            self.__BackLeftThruster.isActive(),
            self.__FrontRightThruster.isActive(),
            self.__BackRightThruster.isActive(),
        ]

        return states

    #Gets the the thruster mounted on the left side of the ROV
    def getFrontLeftThruster(self) -> Thruster:
        return self.__FrontLeftThruster

    #Gets the the thruster mounted on the right side of the ROV
    def getFrontRightThruster(self) -> Thruster:
        return self.__FrontRightThruster

    #Gets the the thruster mounted on the top front side of the ROV
    def getBackLeftThruster(self) -> Thruster:
        return self.__BackLeftThruster

    #Gets the the thruster mounted on the top back side of the ROV
    def getBackRightThruster(self) -> Thruster:
        return self.__BackRightThruster
    
    #Gets the the thruster mounted on the top front side of the ROV
    def getTopFrontThruster(self) -> Thruster:
        return self.__TopFrontThruster

    #Gets the the thruster mounted on the top back side of the ROV
    def getTopBackThruster(self) -> Thruster:
        return self.__TopBackThruster

    #Performs any clean up on system shutdown
    def shutdown(self) -> None:
        self.stop()
