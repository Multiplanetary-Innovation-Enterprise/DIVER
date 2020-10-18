from Command import Command
from Chasis import Chasis

class IncreaseSpeed(Command):
    def execute(self, chasis: Chasis):
        print("incresing speed X: " + str(chasis.getSpeed()) + "\n")
        chasis.increaseSpeed(0.1)
