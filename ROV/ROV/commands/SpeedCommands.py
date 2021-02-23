from commands.Command import Command
from subsystems.PropulsionSubsystem import PropulsionSubsystem

class IncreaseSpeedCommand(Command):
    __propSystem = None

    def __init__(self, propSystem:PropulsionSubsystem):
        self.__propSystem = propSystem

    def execute(self):
        speed = self.__propSystem.getSpeed()

        self.__propSystem.setSpeed(speed + 0.5)

class DecreaseSpeedCommand(Command):
    __propSystem = None

    def __init__(self, propSystem:PropulsionSubsystem):
        self.__propSystem = propSystem

    def execute(self):
        speed = self.__propSystem.getSpeed()

        self.__propSystem.setSpeed(speed - 0.5)
