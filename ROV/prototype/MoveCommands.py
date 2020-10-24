from Command import Command
from Chasis import Chasis

#Represents a command for movement in the x-axis
class MoveX(Command):
    def __init__(self, dir: int):
        self.dir = dir

    #Performs the movement in the x-axis
    def execute(self, chasis: Chasis):
        print("Move X \n")

        #Decides which way to move in the x-axis
        if self.dir == -1:
            chasis.moveX(-chasis.getSpeed());
        elif self.dir == 1:
            chasis.moveX(chasis.getSpeed());
        else:
            chasis.moveX(0);
