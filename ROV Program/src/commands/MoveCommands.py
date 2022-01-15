from ROVMessaging.Action import Action

from commands.Command import Command
from subsystems.PropulsionSubsystem import PropulsionSubsystem

class MoveXYCommand(Command):
    __propSystem:PropulsionSubsystem = None
    __action:Action = None

    def __init__(self, action:Action, propSystem:PropulsionSubsystem):
        self.__propSystem = propSystem
        self.__action = action

    def execute(self):
        speed = self.__propSystem.getSpeed()

        leftSpeedModifier = 0
        rightSpeedModifier = 0

        if(self.__action ==Action.MOVE_XY_FORWARD):
            leftSpeedModifier = 1
            rightSpeedModifier = 1
        elif(self.__action ==Action.MOVE_XY_BACKWARD):
            leftSpeedModifier = -1
            rightSpeedModifier = -1
        elif(self.__action ==Action.MOVE_XY_LEFT):
            leftSpeedModifier = -1
            rightSpeedModifier = 1
        elif(self.__action ==Action.MOVE_XY_RIGHT):
            leftSpeedModifier = 1
            rightSpeedModifier = -1

        self.__propSystem.setXYSpeed(speed * rightSpeedModifier, speed * leftSpeedModifier)

    def isRepeatable(self):
        False

class MoveZCommand(Command):
    __action = None
    __propSystem:PropulsionSubsystem = None

    def __init__(self, action:Action, propSystem:PropulsionSubsystem):
        self.__action = action
        self.__propSystem = propSystem

    def execute(self):
        speed = self.__propSystem.getSpeed()

        if(self.__action == Action.MOVE_Z_POS):
            speed = self.__propSystem.getSpeed()
        elif(self.__action == Action.MOVE_Z_NEG):
            speed = -self.__propSystem.getSpeed()
        elif(self.__action == Action.MOVE_Z_STOP):
            speed = 0

        self.__propSystem.setVerticalSpeedSpeed(speed, speed)

    def isRepeatable(self):
        return False
