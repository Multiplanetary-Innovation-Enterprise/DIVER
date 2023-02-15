from commands.Command import Command
from subsystems.PropulsionSubsystem import PropulsionSubsystem
from commands.PropulsionCommand import PropulsionCommand

#The command for increasing the propulsion speed of the ROV
class IncreaseSpeedCommand(PropulsionCommand):
    #Executes the command
    def execute(self) -> None:
        #Gets the speeds of all the thrusters
        #0 = left, 1 = right, 2 = top front, 3 = top back
        speeds = self._propSystem.getSpeeds()

        #Slowly increments all of the thrusters speeds by 10%
        #Increment by 2.5%
        speeds[0] += 0.025
        speeds[1] += 0.025
        speeds[2] += 0.025
        speeds[3] += 0.025
        
        #Wait 1 second
        time.sleep(1)
            
        #Increment by 2.5%
        speeds[0] += 0.025
        speeds[1] += 0.025
        speeds[2] += 0.025
        speeds[3] += 0.025
        
        #Wait 1 second
        time.sleep(1)
        
        #Increment by 2.5%
        speeds[0] += 0.025
        speeds[1] += 0.025
        speeds[2] += 0.025
        speeds[3] += 0.025
        
        #Wait 1 second
        time.sleep(1)
        
        #Increment by 2.5%
        speeds[0] += 0.025
        speeds[1] += 0.025
        speeds[2] += 0.025
        speeds[3] += 0.025

        print("Increase speed: " + str(speeds[0]))

        #Updates the speed of the ROV
        self._propSystem.setSpeed(speeds[0], speeds[1], speeds[2], speeds[3])

    #Whether or not the command can be repeated back to back
    def isRepeatable(self) -> bool:
        return True

    #The action code associated with this command
    def getActionCode() -> int:
        return 9

#The command for decreasing the propulsion speed of the ROV
class DecreaseSpeedCommand(PropulsionCommand):
    #Executes the command
    def execute(self) -> None:
        #Gets the speeds of all the thrusters
        #0 = left, 1 = right, 2 = top front, 3 = top back
        speeds = self._propSystem.getSpeeds()

        #Slowly decrements all of the thrusters speeds by 10%
        #Decrement by 2.5%
        speeds[0] -= 0.025
        speeds[1] -= 0.025
        speeds[2] -= 0.025
        speeds[3] -= 0.025
        
        #Wait 1 second
        time.sleep(1)
            
        #Decrement by 2.5%
        speeds[0] -= 0.025
        speeds[1] -= 0.025
        speeds[2] -= 0.025
        speeds[3] -= 0.025
        
        #Wait 1 second
        time.sleep(1)
        
        #Decrement by 2.5%
        speeds[0] -= 0.025
        speeds[1] -= 0.025
        speeds[2] -= 0.025
        speeds[3] -= 0.025
        
        #Wait 1 second
        time.sleep(1)
        
        #Decrement by 2.5%
        speeds[0] -= 0.025
        speeds[1] -= 0.025
        speeds[2] -= 0.025
        speeds[3] -= 0.025

        print("Decrease speed: " + str(speeds[0]))

        #Updates the speed of the ROV
        self._propSystem.setSpeed(speeds[0], speeds[1], speeds[2], speeds[3])

    #Whether or not the command can be repeated back to back
    def isRepeatable(self) -> bool:
        return True

    #The action code associated with this command
    def getActionCode() -> int:
        return 10
