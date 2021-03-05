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
            speed = self.__propSystem.getSpeed()
        elif(self.__action == Action.MOVE_X_NEG):
            speed = -self.__propSystem.getSpeed()
        elif(self.__action == Action.MOVE_X_STOP):
            speed = 0

        print("Move X " + str(speed))
        self.__propSystem.moveX(speed)

    def isRepeatable(self):
        return False

class MoveYCommand(Command):
    __action = None
    __propSystem = None

    def __init__(self, action:Action, propSystem:PropulsionSubsystem):
        self.__action = action
        self.__propSystem = propSystem

    def execute(self):
        speed = self.__propSystem.getSpeed()

        if(self.__action == Action.MOVE_Y_POS):
            speed = self.__propSystem.getSpeed()
        elif(self.__action == Action.MOVE_Y_NEG):
            speed = -self.__propSystem.getSpeed()
        elif(self.__action == Action.MOVE_Y_STOP):
            speed = 0

        self.__propSystem.moveY(speed)

    def isRepeatable(self):
        return False

class MoveZCommand(Command):
    __action = None
    __propSystem = None
    __speedStep = 0.5

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

        self.__propSystem.moveZ(speed)

    def isRepeatable(self):
        return False
