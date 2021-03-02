from commands.Command import Command
from subsystems.PropulsionSubsystem import PropulsionSubsystem

class IncreaseSpeedCommand(Command):
    __propSystem = None

    def __init__(self, propSystem:PropulsionSubsystem):
        self.__propSystem = propSystem

    def execute(self):
        speed = self.__propSystem.getSpeed()
        print("Increase speed " + str(speed + 0.1))
        self.__propSystem.setSpeed(speed + 0.1)

    def isRepeatable(self):
        return True

class DecreaseSpeedCommand(Command):
    __propSystem = None

    def __init__(self, propSystem:PropulsionSubsystem):
        self.__propSystem = propSystem

    def execute(self):
        speed = self.__propSystem.getSpeed()
        print("Decrease speed " + str(speed - 0.1))
        self.__propSystem.setSpeed(speed - 0.1)

    def isRepeatable(self):
        return True
