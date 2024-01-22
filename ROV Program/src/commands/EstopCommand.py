from commands.Command import Command

class EstopCommand(Command):
    def execute(self) -> None:
        print("EXECUTING E-STOP")
        #PUT FUTURE E-STOP CODE HERE
        pass
    def isRepeatable(self) -> bool:
        return False
    @staticmethod
    def getActionCode() -> int:
        return 17