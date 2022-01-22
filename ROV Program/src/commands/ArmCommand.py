from commands.Command import Command
from subsystems.PropulsionSubsystem import PropulsionSubsystem

#The command for arming the propulstion system
class ArmCommand(Command):
    __propSystem:PropulsionSubsystem = None #The ROV's propulsion system

    def __init__(self, propSystem:PropulsionSubsystem):
        self.__propSystem = propSystem

    #Executes the command
    def execute(self) -> None:
        print("Arming beep boop")
        self.__propSystem.arm()

    #Whether or not the command can be repeated back to back
    def isRepeatable(self) -> bool:
        return False

    #The action code associated with this command
    def getActionCode() -> int:
        return 0
