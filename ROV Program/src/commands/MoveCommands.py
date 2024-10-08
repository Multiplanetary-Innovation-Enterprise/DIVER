from abc import ABC

from commands.Command import Command
from commands.PropulsionCommand import PropulsionCommand

#Represents a generic move command
class MoveCommand(PropulsionCommand, ABC):
    #Whether or not the command can be repeated back to back
    def isRepeatable(self) -> bool:
        return False

#The command for stopping the ROV's movement in the XY plane
class MoveXYStopCommand(MoveCommand):
    #Executes the command
    def execute(self) -> None:
        print("XY Stop")
        #Turns off the  thrusters in the XY plane
        self._propSystem.setXYStates(False, False, False, False)

    #The action code associated with this command
    @staticmethod
    def getActionCode() -> int:
        return 1

#The command for moving the ROV forward
class MoveForwardCommand(MoveCommand):
    #Executes the command
    def execute(self) -> None:
        print("Forwards")

        #Sets both thruster speeds push forwards
        speeds = self._propSystem.getFlatSpeeds()
        self._propSystem.setXYSpeed(abs(speeds[0]), abs(speeds[1]), abs(speeds[2]), abs(speeds[3]))

        #Turns on the XY thrusters
        self._propSystem.setXYStates(True, True, True, True)

    #The action code associated with this command
    @staticmethod
    def getActionCode() -> int:
        return 2

#The command for moving the ROV backwards
class MoveBackwardCommand(MoveCommand):
    #Executes the command
    def execute(self) -> None:
        print("Backwards")

        #Sets both thruster speeds push backwards
        speeds = self._propSystem.getFlatSpeeds()
        self._propSystem.setXYSpeed(-abs(speeds[0]), -abs(speeds[1]),  -abs(speeds[2]),  -abs(speeds[3]))

        #Turns on the XY thrusters
        self._propSystem.setXYStates(True, True, True, True)

    #The action code associated with this command
    @staticmethod
    def getActionCode() -> int:
        return 3

#The command for moving the ROV to the left
class MoveLeftCommand(MoveCommand):
    #Executes the command
    def execute(self) -> None:
        print("Move Left")

        #Sets the left thruster speed to pull and the right thruster speed to push
        speeds = self._propSystem.getFlatSpeeds()
        self._propSystem.setXYSpeed(-abs(speeds[0]), abs(speeds[1]*0.76), abs(speeds[2]*0.76), -abs(speeds[3]))

        #Turns on the XY thrusters
        self._propSystem.setXYStates(True, True, True, True)

    #The action code associated with this command
    @staticmethod
    def getActionCode() -> int:
        return 4

#The command for moving the ROV to the right
class MoveRightCommand(MoveCommand):
    #Executes the command
    def execute(self) -> None:
        print("Move Right")

        #Sets the left thruster speed to push and the right thruster speed to pull
        speeds = self._propSystem.getFlatSpeeds()
        self._propSystem.setXYSpeed(abs(speeds[0]*0.76), -abs(speeds[1]), -abs(speeds[2]), abs(speeds[3]*0.76))

        #Turns on the XY thrusters
        self._propSystem.setXYStates(True, True, True, True)

    #The action code associated with this command
    @staticmethod
    def getActionCode() -> int:
        return 5
    


#The command for turning the ROV to the left
class TurnCWCommand(MoveCommand):
    #Executes the command
    def execute(self) -> None:
        print("Turn clockwise")

        #Sets the left thruster speed to pull and the right thruster speed to push
        speeds = self._propSystem.getFlatSpeeds()
        self._propSystem.setXYSpeed(abs(speeds[0]*0.76), -abs(speeds[1]), abs(speeds[2]*0.76),- abs(speeds[3]))

        #Turns on the XY thrusters
        self._propSystem.setXYStates(True, True, True, True)

    #The action code associated with this command
    @staticmethod
    def getActionCode() -> int:
        return 15

#The command for turning the ROV to the right
class TurnCCWCommand(MoveCommand):
    #Executes the command
    def execute(self) -> None:
        print("Turn counterclockwise")

        #Sets the left thruster speed to push and the right thruster speed to pull
        speeds = self._propSystem.getFlatSpeeds()
        self._propSystem.setXYSpeed(-abs(speeds[0]), abs(speeds[1]*0.76), -abs(speeds[2]), abs(speeds[3]*0.76))

        #Turns on the XY thrusters
        self._propSystem.setXYStates(True, True, True, True)

    #The action code associated with this command
    @staticmethod
    def getActionCode() -> int:
        return 16
    




#The command for stopping the ROV's vertical movement
class MoveZStopCommand(MoveCommand):
    #Executes the command
    def execute(self) -> None:
        print("Z Stop")
        #Turns off the vertical thrusters
        self._propSystem.setZStates(False, False)

    #The action code associated with this command
    @staticmethod
    def getActionCode() -> int:
        return 6

#The command for moving the ROV upwards
class MoveUpCommand(MoveCommand):
    #Executes the command
    def execute(self) -> None:
        print("Move Up")

        #Sets both vertical thruster speeds to pull upward
        speeds = self._propSystem.getVerticalSpeeds()
        self._propSystem.setVerticalSpeed(abs(speeds[0]), abs(speeds[1]))

        #Turns on the vertical thrusters
        self._propSystem.setZStates(True, True)

    #The action code associated with this command
    @staticmethod
    def getActionCode() -> int:
        return 7

#The command for moving the ROV downwards
class MoveDownCommand(MoveCommand):
    #Executes the command
    def execute(self) -> None:
        print("Move Down")

        #Sets both vertical thruster speeds to push downward
        speeds = self._propSystem.getVerticalSpeeds()
        self._propSystem.setVerticalSpeed(-abs(speeds[0]), -abs(speeds[1]))

        #Turns on the vertical thrusters
        self._propSystem.setZStates(True, True)

    #The action code associated with this command
    @staticmethod
    def getActionCode() -> int:
        return 8
