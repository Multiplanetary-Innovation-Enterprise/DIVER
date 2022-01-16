from commands.Command import Command
from subsystems.PropulsionSubsystem import PropulsionSubsystem
from components.rotation.RotDirection import RotDirection

#The command for stopping the ROV's movement in the XY plane
class MoveXYStopCommand(Command):
    __propSystem:PropulsionSubsystem = None #The ROV's propulsion system

    def __init__(self, propSystem:PropulsionSubsystem):
        self.__propSystem = propSystem

    #Executes the command
    def execute(self) -> None:
        print("XY Stop")
        #Turns off the  thrusters in the XY plane
        self.__propSystem.setXYStates(False, False)

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
        print("Forwards")
        self.__propSystem.setXYRotDirections(RotDirection.CLOCKWISE, RotDirection.CLOCKWISE)
        self.__propSystem.setXYStates(True, True)

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
        print("Backwards")
        self.__propSystem.setXYRotDirections(RotDirection.COUNTER_CLOCKWISE, RotDirection.COUNTER_CLOCKWISE)
        self.__propSystem.setXYStates(True, True)

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
        print("Turn Left")
        self.__propSystem.setXYRotDirections(RotDirection.COUNTER_CLOCKWISE, RotDirection.CLOCKWISE)
        self.__propSystem.setXYStates(True, True)

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
        print("Turn Right")
        self.__propSystem.setXYRotDirections(RotDirection.CLOCKWISE, RotDirection.COUNTER_CLOCKWISE)
        self.__propSystem.setXYStates(True, True)

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
        print("Z Stop")
        #Turns off the vertical thrusters
        self.__propSystem.setZStates(False, False)

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
        print("Move Up")
        self.__propSystem.setZRotDirections(RotDirection.CLOCKWISE, RotDirection.CLOCKWISE)
        self.__propSystem.setZStates(True, True)

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
        print("Move Down")
        self.__propSystem.setZRotDirections(RotDirection.COUNTER_CLOCKWISE, RotDirection.COUNTER_CLOCKWISE)
        self.__propSystem.setZStates(True, True)

    #Whether or not the command can be repeated back to back
    def isRepeatable(self) -> bool:
        return False

    #The action code associated with this command
    def getActionCode() -> int:
        return 8
