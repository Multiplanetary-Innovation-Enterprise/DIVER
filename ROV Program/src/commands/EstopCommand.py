from commands.Command import Command
from subsystems.EStopSubSystem import EStopSubsystem

class EstopCommand(Command):
    __estopSystem: EStopSubsystem = None

    def __init__(self, estopSystem:EStopSubsystem):
        self._illuminationSystem = EStopSubsystem

    def execute(self) -> None:
        print("EXECUTING E-STOP")
        EStopSubsystem.triggerEStop()
    def isRepeatable(self) -> bool:
        return False
    @staticmethod
    def getActionCode() -> int:
        return 17