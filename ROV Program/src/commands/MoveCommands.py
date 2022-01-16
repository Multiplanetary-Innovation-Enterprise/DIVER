from commands.Command import Command
from subsystems.PropulsionSubsystem import PropulsionSubsystem

#The command for stopping the ROV's movement in the XY plane
class MoveXYStopCommand(Command):
    __propSystem:PropulsionSubsystem = None #The ROV's propulsion system

    def __init__(self, propSystem:PropulsionSubsystem):
        self.__propSystem = propSystem

    #Executes the command
    def execute(self) -> None:
        self.__propSystem.setXYSpeed(0, 0)

    #Whether or not the command can be repeated back to back
    def isRepeatable(self) -> bool:
        return False

    #The action code associated with this command
    def getActionCode() -> int:
        return 1

#The command for moving the ROV forward
class MoveForwardCommand(Command):
    __propSystem:PropulsionSubsystem = None #The ROV's propulsion system

    def __init__(self, propSystem:PropulsionSubsystem):
        self.__propSystem = propSystem

    #Executes the command
    def execute(self) -> None:
        #Gets the speeds of the XY thrusters
        # 0 = left, 1 = right
        speeds = self.__propSystem.getXYSpeeds()
        self.__propSystem.setXYSpeed(speeds[0], speeds[1])

    #Whether or not the command can be repeated back to back
    def isRepeatable(self) -> bool:
        return False

    #The action code associated with this command
    def getActionCode() -> int:
        return 2

#The command for moving the ROV backwards
class MoveBackwardCommand(Command):
    __propSystem:PropulsionSubsystem = None #The ROV's propulsion system

    def __init__(self, propSystem:PropulsionSubsystem):
        self.__propSystem = propSystem

    #Executes the command
    def execute(self) -> None:
        #Gets the speeds of the XY thrusters
        # 0 = left, 1 = right
        speeds = self.__propSystem.getXYSpeeds()
        self.__propSystem.setXYSpeed(-speeds[0], -speeds[1])

    #Whether or not the command can be repeated back to back
    def isRepeatable(self) -> bool:
        return False

    #The action code associated with this command
    def getActionCode() -> int:
        return 3

#The command for turning the ROV to the left
class TurnLeftCommand(Command):
    __propSystem:PropulsionSubsystem = None #The ROV's propulsion system

    def __init__(self, propSystem:PropulsionSubsystem):
        self.__propSystem = propSystem

    #Executes the command
    def execute(self) -> None:
        #Gets the speeds of the XY thrusters
        # 0 = left, 1 = right
        speeds = self.__propSystem.getXYSpeeds()
        self.__propSystem.setXYSpeed(-speeds[0], speeds[1])

    #Whether or not the command can be repeated back to back
    def isRepeatable(self) -> bool:
        return False

    #The action code associated with this command
    def getActionCode() -> int:
        return 4

#The command for turning the ROV to the right
class TurnRightCommand(Command):
    __propSystem:PropulsionSubsystem = None #The ROV's propulsion system

    def __init__(self, propSystem:PropulsionSubsystem):
        self.__propSystem = propSystem

    #Executes the command
    def execute(self) -> None:
        #Gets the speeds of the XY thrusters
        # 0 = left, 1 = right
        speeds = self.__propSystem.getXYSpeeds()
        self.__propSystem.setXYSpeed(speeds[0], -speeds[1])

    #Whether or not the command can be repeated back to back
    def isRepeatable(self) -> bool:
        return False

    #The action code associated with this command
    def getActionCode() -> int:
        return 5

#The command for stopping the ROV's vertical movement
class MoveZStopCommand(Command):
    __propSystem:PropulsionSubsystem = None #The ROV's propulsion system

    def __init__(self, propSystem:PropulsionSubsystem):
        self.__propSystem = propSystem

    #Executes the command
    def execute(self) -> None:
        #Gets the speeds of the vertical thrusters
        self.__propSystem.setVerticalSpeed(0, 0)

    #Whether or not the command can be repeated back to back
    def isRepeatable(self) -> bool:
        return False

    #The action code associated with this command
    def getActionCode() -> int:
        return 6

#The command for moving the ROV upwards
class MoveUpCommand(Command):
    __propSystem:PropulsionSubsystem = None #The ROV's propulsion system

    def __init__(self, propSystem:PropulsionSubsystem):
        self.__propSystem = propSystem

    #Executes the command
    def execute(self) -> None:
        #Gets the speeds of the vertical thrusters
        # 0 = front top, 1 = back top
        speeds = self.__propSystem.getVerticalSpeeds()
        self.__propSystem.setVerticalSpeed(speeds[0], speeds[1])

    #Whether or not the command can be repeated back to back
    def isRepeatable(self) -> bool:
        return False

    #The action code associated with this command
    def getActionCode() -> int:
        return 7

#The command for moving the ROV downwards
class MoveDownCommand(Command):
    __propSystem:PropulsionSubsystem = None #The ROV's propulsion system

    def __init__(self, propSystem:PropulsionSubsystem):
        self.__propSystem = propSystem

    #Executes the command
    def execute(self) -> None:
        #Gets the speeds of the vertical thrusters
        # 0 = front top, 1 = back top
        speeds = self.__propSystem.getVerticalSpeeds()
        self.__propSystem.setVerticalSpeed(-speeds[0], -speeds[1])

    #Whether or not the command can be repeated back to back
    def isRepeatable(self) -> bool:
        return False

    #The action code associated with this command
    def getActionCode() -> int:
        return 8
