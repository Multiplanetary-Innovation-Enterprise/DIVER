from Command import Command
from Chasis import Chasis

#Represents a command for movement in the x-axis
class MoveX(Command):
    def __init__(self, dir: int):
        self.dir = dir

    #Performs the movement in the x-axis
    def execute(self, chasis: Chasis):
        #Decides which way to move in the x-axis
        if self.dir == -1:
            chasis.moveX(-chasis.getSpeed());
            print("backward\n")
        elif self.dir == 1:
            chasis.moveX(chasis.getSpeed());
            print("forward\n")
        else:
            chasis.moveX(0);
            print("stop x\n")

class MoveY(Command):
    def __init__(self, dir: int):
        self.dir = dir

    #Performs the movement in the x-axis
    def execute(self, chasis: Chasis):
        #Decides which way to move in the x-axis
        if self.dir == -1:
            chasis.moveY(-chasis.getSpeed());
            print("backward\n")
        elif self.dir == 1:
            chasis.moveY(chasis.getSpeed());
            print("forward\n")
        else:
            chasis.moveY(0);
            print("stop x\n")
