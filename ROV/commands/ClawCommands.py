from commands.Command import Command
from subsystems.ClawSubsystem import ClawSubsystem

class IncreaseClawAngle(Command):
    __clawSystem: ClawSubsystem = None

    def __init__(self, clawSystem:ClawSubsystem):
        self.__clawSystem = clawSystem

    def execute(self):
        if not self.__clawSystem.isActivated():
            self.__clawSystem.activate()

        angle = self.__clawSystem.getAngle() + 5
        self.__clawSystem.setAngle(angle)

    def isRepeatable(self):
        return True

class DecreaseClawAngle(Command):
    __clawSystem: ClawSubsystem = None

    def __init__(self, clawSystem:ClawSubsystem):
        self.__clawSystem = clawSystem

    def execute(self):
        if not self.__clawSystem.isActivated():
            self.__clawSystem.activate()

        angle = self.__clawSystem.getAngle() - 5
        self.__clawSystem.setAngle(angle)

    def isRepeatable(self):
        return True

class DeactivateClaw(Command):
    __clawSystem: ClawSubsystem = None

    def __init__(self, clawSystem:ClawSubsystem):
        self.__clawSystem = clawSystem

    def execute(self):
        if self.__clawSystem.isActivated():
            self.__clawSystem.deactivate()

    def isRepeatable(self):
        return False
