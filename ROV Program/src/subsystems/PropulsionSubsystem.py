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
    __TopLeftThruster:Thruster = None #The thruster mounted on the top front side of the ROV
    __TopRightThruster:Thruster = None  #The thruster mounted on the top back side of the ROV
    

    def __init__(self, controller:Controller, config):
        super().__init__(controller, config)

        #Gets the GPIO pins for the thrusters
        frontLeftPin  = int(config['Propulsion']['FrontLeftThrusterPin'])
        frontRightPin = int(config['Propulsion']['FrontRightThrusterPin'])
        backLeftPin   = int(config['Propulsion']['BackLeftThrusterPin'])
        backRightPin  = int(config['Propulsion']['BackRightThrusterPin'])
        topLeftPin    = int(config['Propulsion']['TopLeftThrusterPin'])
        topRightPin   = int(config['Propulsion']['TopRightThrusterPin'])

        #Creates three thrusters. Two for the x-y movement and two for z movement
        self.__FrontLeftThruster  = Thruster(controller, frontLeftPin, RotDirection.COUNTER_CLOCKWISE)
        self.__FrontRightThruster = Thruster(controller, frontRightPin, RotDirection.COUNTER_CLOCKWISE)   
        self.__BackLeftThruster   = Thruster(controller, backLeftPin, RotDirection.COUNTER_CLOCKWISE)
        self.__BackRightThruster  = Thruster(controller, backRightPin, RotDirection.COUNTER_CLOCKWISE)

        self.__TopLeftThruster  = Thruster(controller, topLeftPin, RotDirection.COUNTER_CLOCKWISE)
        self.__TopRightThruster = Thruster(controller, topRightPin, RotDirection.CLOCKWISE)

    #Arms all of the thrusters
    def arm(self) -> None:
        print("Arming thrusters!!!!!")
        self.__FrontLeftThruster.arm()
        self.__FrontRightThruster.arm()
        self.__BackLeftThruster.arm()
        self.__BackRightThruster.arm()

        # self.__leftThruster.arm()
        # self.__rightThruster.arm()
        self.__TopLeftThruster.arm()
        self.__TopRightThruster.arm()
        
    #Sets the speed of all three thrusters independently
    #0 = RightTop, 1 = LeftTop, 2 = FrontRight, 3 = FrontLeft, 4 = BackRight, 5 = Backeft
    def setSpeed(self, RightTopSpeed:float, LeftTopSpeed:float, FrontRightSpeed:float, FrontLeftSpeed:float, BackRightSpeed:float, BackLeftSpeed:float) -> None:
        
        self.setXYSpeed(FrontRightSpeed, FrontLeftSpeed,  BackRightSpeed, BackLeftSpeed)
        self.setVerticalSpeed(RightTopSpeed, LeftTopSpeed)

    #Sets all the thrusters to the same speed (python does not allow function overloading)
    def setSpeedSame(self, speed:float) -> None:
        self.setSpeed(speed,speed,speed,speed, speed, speed)

    #Sets the speed of the thrusters mountd in the XY plane
    def setXYSpeed(self, FrontRightSpeed:float, FrontLeftSpeed:float, BackRightSpeed:float, BackLeftSpeed:float) -> None:
        self.__FrontRightThruster.setSpeed(FrontRightSpeed)
        self.__FrontLeftThruster.setSpeed(FrontLeftSpeed)
        self.__BackRightThruster.setSpeed(BackRightSpeed)
        self.__BackLeftThruster.setSpeed(BackLeftSpeed)

    #Sets the XY thrusters to the same speed (python does not allow function overloading)
    def setXYSpeedSame(self, speed:float) -> None:
        self.setXYSpeed(speed, speed, speed, speed)

    #Sets the speed of the thrusters mounted vertically
    def setVerticalSpeed(self, TopRightSpeed:float, TopLeftSpeed:float) -> None:
        self.__TopRightThruster.setSpeed(TopRightSpeed)
        self.__TopLeftThruster.setSpeed(TopLeftSpeed)

    #Sets the vertical thrusters to the same speed (python does not allow function overloading)
    def setVerticalSpeedSame(self, speed:float) -> None:
        self.setVerticalSpeed(speed, speed)

    #Gets the speeds of all the thrusters
    #0 = TopRight, 1 = TopLeft, 2 = FrontRight, 3 = FrontLeft, 4 = BackRight, 5 = Backeft
    def getSpeeds(self) -> list:
        speeds = [
            self.__TopRightThruster.getSpeed(),
            self.__TopLeftThruster.getSpeed(),
            self.__FrontRightThruster.getSpeed(),
            self.__FrontLeftThruster.getSpeed(),
            self.__BackRightThruster.getSpeed(),
            self.__BackLeftThruster.getSpeed()
            
        ]

        return speeds

    #Gets the flat speed of the thrusters to undo 76% adjustment
    def getFlatSpeeds(self) -> list:
        speeds = [
            self.__TopRightThruster.getSpeed(),
            self.__TopLeftThruster.getSpeed(),
            self.__TopRightThruster.getSpeed(),
            self.__TopLeftThruster.getSpeed()
        ]

        return speeds

    #Gets the speeds of the vertical thrusters
    def getVerticalSpeeds(self) -> list:
        speeds = [
            self.__TopRightThruster.getSpeed(),
            self.__TopLeftThruster.getSpeed()
        ]

        return speeds

    #Stops all of the thrusters
    def stop(self) -> None:
        self.setStates(False, False, False, False, False, False)

    #0 = TopRight, 1 = TopLeft, 2 = FrontRight, 3 = FrontLeft, 4 = BackRight, 5 = Backeft
    #Sets the rotational direction for all thrusters
    def setRotDirections(self, TopRightRotDir:RotDirection, TopLeftRotDir:RotDirection, FrontRightRotDir:RotDirection, FrontLeftRotDir:RotDirection, BackRightRotDir:RotDirection, BackLeftRotDir:RotDirection) -> None:
        self.setXYRotDirections(FrontRightRotDir, FrontLeftRotDir, BackRightRotDir, BackLeftRotDir)
        self.setZRotDirections(TopRightRotDir, TopLeftRotDir)

    #Sets the rotational direction for the thrusters in the XY plane
    def setXYRotDirections(self, FrontRightRotDir:RotDirection, FrontLeftRotDir:RotDirection, BackRightRotDir:RotDirection, BackLeftRotDir:RotDirection) -> None:
        self.__FrontRightThruster.setRotDirection(FrontRightRotDir)
        self.__FrontLeftThruster.setRotDirection(FrontLeftRotDir)
        self.__BackRightThruster.setRotDirection(BackRightRotDir)
        self.__BackLeftThruster.setRotDirection(BackLeftRotDir)

    #Sets the rotational direction for the vertical thrusters
    def setZRotDirections(self, TopRightRotDir:RotDirection, TopLeftRotDir:RotDirection) -> None:
        self.__TopRightThruster.setRotDirection(TopRightRotDir)
        self.__TopLeftThruster.setRotDirection(TopLeftRotDir)

    #Gets the rotation directions of all the thrusters
    def getRotDirections(self) -> list:
        dirs = [
            self.__TopRightThruster.getRotDirection(),
            self.__TopLeftThruster.getRotDirection(),
            self.__FrontRightThruster.getRotDirection(),
            self.__FrontLeftThruster.getRotDirection(),
            self.__BackRightThruster.getRotDirection(),
            self.__BackLeftThruster.getRotDirection()
  
        ]

        return dirs

    #0 = TopRight, 1 = TopLeft, 2 = FrontRight, 3 = FrontLeft, 4 = BackRight, 5 = BackLeft
    #Sets the states of all the thrusters(active/not-active)
    def setStates(self, TopRightActive:bool, TopLeftActive:bool, FrontRightActive:bool, FrontLeftActive:bool, BackRightActive:bool, BackLeftActive:bool) -> None:
        self.setXYStates(FrontRightActive, FrontLeftActive, BackRightActive, BackLeftActive)
        self.setZStates(TopRightActive, TopLeftActive)

    #Sets the states of all the thrusters in the XY plane(active/not-active)
    def setXYStates(self, FrontRightActive:bool, FrontLeftActive:bool, BackRightActive:bool, BackLeftActive:bool) -> None:
        self.__FrontRightThruster.setState(FrontRightActive)
        self.__FrontLeftThruster.setState(FrontLeftActive)
        self.__BackRightThruster.setState(BackRightActive)
        self.__BackLeftThruster.setState(BackLeftActive)


    #Sets the states of the vertical thrusters(active/not-active)
    def setZStates(self, TopRightActive:bool, TopLeftActive:bool) -> None:
        self.__TopRightThruster.setState(TopRightActive)
        self.__TopLeftThruster.setState(TopLeftActive)

    #Gets the states of all the thrusters
    def getStates(self) -> list:
        states = [
            self.__TopRightThruster.isActive(),
            self.__TopLeftThruster.isActive(),
            self.__FrontRightThruster.isActive(),
            self.__FrontLeftThruster.isActive(),
            self.__BackRightThruster.isActive(),
            self.__BackLeftThruster.isActive()
          
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
    def getTopLeftThruster(self) -> Thruster:
        return self.__TopLeftThruster

    #Gets the the thruster mounted on the top back side of the ROV
    def getTopRightThruster(self) -> Thruster:
        return self.__TopRightThruster

    #Performs any clean up on system shutdown
    def shutdown(self) -> None:
        self.stop()
