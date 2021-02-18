from ROVMessaging.Action import Action

from commands.Command import Command
from subsystems.PropulsionSubsystem import PropulsionSubsystem

class MoveXCommand(Command):
    __action = None
    __propSystem = None

    def __init__(self, action:Action, propSystem:PropulsionSubsystem):
        self.__action = action
        self.__propSystem = propSystem

    def execute(self):
        speed = 0

        if(self.__action == Action.MOVE_X_POS):
            speed = 0.5
        elif(self.__action == Action.MOVE_X_NEG):
            speed = -0.5
        elif(self.__action == Action.MOVE_X_STOP):
            speed = 0

        self.__propSystem.moveX(speed)

class MoveYCommand(Command):
    __action = None
    __propSystem = None

    def __init__(self, action:Action, propSystem:PropulsionSubsystem):
        self.__action = action
        self.__propSystem = propSystem

    def execute(self):
        if(self.__action == Action.MOVE_Y_POS):
            self.__propSystem.moveY(0.5)
        elif(self.__action == Action.MOVE_Y_NEG):
            self.__propSystem.moveY(-0.5)
        elif(self.__action == Action.MOVE_Y_STOP):
            self.__propSystem.moveY(0)

class MoveZCommand(Command):
    __action = None
    __propSystem = None

    def __init__(self, action:Action, propSystem:PropulsionSubsystem):
        self.__action = action
        self.__propSystem = propSystem

    def execute(self):
        if(self.__action == Action.MOVE_Z_POS):
            self.__propSystem.moveZ(0.5)
        elif(self.__action == Action.MOVE_Z_NEG):
            self.__propSystem.moveZ(-0.5)
        elif(self.__action == Action.MOVE_Z_STOP):
            self.__propSystem.moveZ(0)
