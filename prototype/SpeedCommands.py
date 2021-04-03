from Command import Command
from Chasis import Chasis

class SpeedCommand(Command):
    pass


#Represents a command for increasing the chasis speed
class IncreaseSpeed(SpeedCommand):
    def execute(self, chasis: Chasis):
        chasis.increaseSpeed(0.1)
        print("incresing speed X: " + str(chasis.getSpeed()) + "\n")

#Represents a command for decreasing the chasis speed
class DecreaseSpeed(SpeedCommand):
    def execute(self, chasis: Chasis):
        chasis.decreaseSpeed(0.1)
        print("decreasing speed X: " + str(chasis.getSpeed()) + "\n")