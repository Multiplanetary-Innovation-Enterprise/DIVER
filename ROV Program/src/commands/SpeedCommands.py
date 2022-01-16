from commands.Command import Command
from subsystems.PropulsionSubsystem import PropulsionSubsystem

#The command for increasing the propulsion speed of the ROV
class IncreaseSpeedCommand(Command):
    __propSystem:PropulsionSubsystem = None #The ROV's propulsion system

    def __init__(self, propSystem:PropulsionSubsystem):
        self.__propSystem = propSystem

        #Executes the command
        def execute(self) -> None:
            #Gets the speeds of all the thrusters
            #0 = left, 1 = right, 2 = top front, 3 = top back
            speeds = self.__propSystem.getSpeeds()

            print("Increase speed: " + str(speed ))

            #Increments all of the thrusters speeds by 10%
            speeds[0] += 0.1
            speeds[1] += 0.1
            speeds[2] += 0.1
            speeds[3] += 0.1

            #Updates the speed of the ROV
            self.__propSystem.setSpeed(speeds[0], speeds[1], speeds[2], speeds[3])

        #Whether or not the command can be repeated back to back
        def isRepeatable(self) -> bool:
            return True

        #The action code associated with this command
        def getActionCode() -> int:
            return 9

#The command for decreasing the propulsion speed of the ROV
class DecreaseSpeedCommand(Command):
    __propSystem:PropulsionSubsystem = None #The ROV's propulsion system

    def __init__(self, propSystem:PropulsionSubsystem):
        self.__propSystem = propSystem

        #Executes the command
        def execute(self) -> None:
            #Gets the speeds of all the thrusters
            #0 = left, 1 = right, 2 = top front, 3 = top back
            speeds = self.__propSystem.getSpeeds()

            print("Decrease speed: " + str(speed - 0.1))

            #Decrements all of the thrusters speeds by 10%
            speeds[0] -= 0.1
            speeds[1] -= 0.1
            speeds[2] -= 0.1
            speeds[3] -= 0.1

            #Updates the speed of the ROV
            self.__propSystem.setSpeed(speeds[0], speeds[1], speeds[2], speeds[3])

        #Whether or not the command can be repeated back to back
        def isRepeatable(self) -> bool:
            return True

        #The action code associated with this command
        def getActionCode() -> int:
            return 10
