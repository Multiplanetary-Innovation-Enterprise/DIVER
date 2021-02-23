from commands.Command import Command
from subsystems.PropulsionSubsystem import PropulsionSubsystem

class ArmCommand(Command):
    __action = None
    __propSystem = None

    def __init__(self, propSystem:PropulsionSubsystem):
        self.__propSystem = propSystem

    def execute(self):
        self.__propSystem.arm()
