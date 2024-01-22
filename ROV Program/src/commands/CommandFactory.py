from commands.Command import Command
from commands.ArmCommand import ArmCommand
from commands.MoveCommands import *
from commands.SpeedCommands import *
from commands.IlluminationCommands import *
from commands.CaptureImageCommand import *
from commands.EstopCommand import *

from ROV import ROV

#Creates any command from its corresponding action code
class CommandFactory:
    __rov:ROV = None #The ROV (used to get access to its subsystems)

    def __init__(self, rov:ROV):
        self.__rov = rov

    #Creates the command associated with the provided action code
    def createCommand(self, actionCode:int) -> Command:
        command = None

        #Looks for the command with the matching action code
        if actionCode == ArmCommand.getActionCode():
            command = ArmCommand(self.__rov.getPropSystem())
        elif actionCode == MoveXYStopCommand.getActionCode():
                command = MoveXYStopCommand(self.__rov.getPropSystem())
        elif actionCode == MoveForwardCommand.getActionCode():
                command = MoveForwardCommand(self.__rov.getPropSystem())
        elif actionCode == MoveBackwardCommand.getActionCode():
                command = MoveBackwardCommand(self.__rov.getPropSystem())
        
        
        elif actionCode == MoveLeftCommand.getActionCode():
                command = MoveLeftCommand(self.__rov.getPropSystem())
        elif actionCode == MoveRightCommand.getActionCode():
                command = MoveRightCommand(self.__rov.getPropSystem())
                
                
        elif actionCode == TurnCCWCommand.getActionCode():
                command = TurnCCWCommand(self.__rov.getPropSystem())
        elif actionCode == TurnCWCommand.getActionCode():
                command = TurnCWCommand(self.__rov.getPropSystem())

        elif actionCode == MoveZStopCommand.getActionCode():
                command = MoveZStopCommand(self.__rov.getPropSystem())
        elif actionCode == MoveUpCommand.getActionCode():
                command = MoveUpCommand(self.__rov.getPropSystem())
        elif actionCode == MoveDownCommand.getActionCode():
                command = MoveDownCommand(self.__rov.getPropSystem())
        elif actionCode == IncreaseSpeedCommand.getActionCode():
                command = IncreaseSpeedCommand(self.__rov.getPropSystem())
        elif actionCode == DecreaseSpeedCommand.getActionCode():
                command = DecreaseSpeedCommand(self.__rov.getPropSystem())
        elif actionCode == ToggleLightStateCommand.getActionCode():
                command = ToggleLightStateCommand(self.__rov.getIlluminationSystem())
        elif actionCode == IncreaseLightBrightnessCommand.getActionCode():
                command = IncreaseLightBrightnessCommand(self.__rov.getIlluminationSystem())
        elif actionCode == DecreaseLightBrightnessCommand.getActionCode():
                command = DecreaseLightBrightnessCommand(self.__rov.getIlluminationSystem())
        elif actionCode == CaptureImageCommand.getActionCode():
                command = CaptureImageCommand(self.__rov.getVisionSystem())
        elif  actionCode == EstopCommand.getActionCode():
               pass
        return command
