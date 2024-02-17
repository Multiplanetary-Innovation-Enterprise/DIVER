from commands.Command import Command

class ChangeAutoCommand(Command):
    Autonomous = False

    def __init__(self,AutoSystem):
        self.AutoSystem = AutoSystem

    def execute(self) -> None:
        print("Changing Autonomy settings")

        pass
    def isRepeatable(self) -> bool:
        return True

    @staticmethod
    def getActionCode() -> int:
        return 18