from ROVMessaging.Action import Action
from ROVMessaging.MessageChannel import MessageChannel

from commands.Command import Command
from commands.ArmCommand import ArmCommand
from commands.MoveCommands import *
from commands.SpeedCommands import *
from commands.IlluminationCommands import *
from util.Direction import Direction

from ROV import ROV

class CommandFactory:
    __rov = None
    __messageChannel = None

    def __init__(self, rov:ROV, messageChannel:MessageChannel):
        self.__rov = rov
        self.__messageChannel = messageChannel

    def createCommand(self, action:Action) -> Command:
        command = None

        if(action == Action.MOVE_XY_FORWARD):
            command = MoveXYCommand(Direction.FORWARD, Direction.FORWARD, self.__rov.getPropSystem())
        elif(action == Action.MOVE_XY_BACKWARD):
            command = MoveXYCommand(Direction.BACKWARD, Direction.BACKWARD, self.__rov.getPropSystem())
        elif(action == Action.MOVE_XY_LEFT):
            command = MoveXYCommand(Direction.BACKWARD, Direction.FORWARD, self.__rov.getPropSystem())
        elif(action == Action.MOVE_XY_RIGHT):
            command = MoveXYCommand(Direction.FORWARD, Direction.BACKWARD, self.__rov.getPropSystem())
        elif(action == Action.MOVE_XY_STOP):
            command = MoveXYCommand(Direction.STOP, Direction.STOP, self.__rov.getPropSystem())
        elif(action == Action.MOVE_Z_POS or action == Action.MOVE_Z_NEG or action == Action.MOVE_Z_STOP):
            command = MoveZCommand(action, self.__rov.getPropSystem())
        elif(action == Action.ARM):
            command = ArmCommand(self.__rov.getPropSystem())
        elif(action == Action.SPEED_INCREASE):
            command = IncreaseSpeedCommand(self.__rov.getPropSystem())
        elif(action == Action.SPEED_DECREASE):
            command = DecreaseSpeedCommand(self.__rov.getPropSystem())
        elif(action == Action.TOGGLE_LIGHTS):
            command = LightStateToggleCommand(self.__rov.getIlluminationSystem())
        elif(action == Action.BRIGHTNESS_INCREASE):
            command = LightIncreaseBrightnessCommand(self.__rov.getIlluminationSystem())
        elif(action == Action.BRIGHTNESS_DECREASE):
            command = LightDecreaseBrightnessCommand(self.__rov.getIlluminationSystem())

        return command
