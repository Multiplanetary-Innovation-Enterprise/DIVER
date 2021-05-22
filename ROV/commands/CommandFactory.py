from ROVMessaging.Action import Action
from ROVMessaging.MessageChannel import MessageChannel

from commands.Command import Command
from commands.ArmCommand import ArmCommand
from commands.MoveCommands import *
from commands.ClawCommands import *
from commands.SpeedCommands import *
from commands.IlluminationCommands import *

from ROV import ROV

class CommandFactory:
    __rov = None
    __messageChannel = None

    def __init__(self, rov:ROV, messageChannel:MessageChannel):
        self.__rov = rov
        self.__messageChannel = messageChannel

    def createCommand(self, action:Action) -> Command:
        command = None

        if(action == Action.MOVE_XY_FORWARD or action == Action.MOVE_XY_BACKWARD or action == Action.MOVE_XY_LEFT or action == Action.MOVE_XY_RIGHT or action == Action.MOVE_XY_STOP):
            command = MoveXYCommand(action, self.__rov.getPropSystem())
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
        elif(action == Action.CLAW_ANGLE_INCREASE):
            command = IncreaseClawAngle(self.__rov.getClawSystem())
        elif(action == Action.CLAW_ANGLE_DECREASE):
            command = DecreaseClawAngle(self.__rov.getClawSystem())
        elif(action == Action.CLAW_DEACTIVATE):
            command = DeactivateClaw(self.__rov.getClawSystem())

        print("Action: " + str(action))

        return command
