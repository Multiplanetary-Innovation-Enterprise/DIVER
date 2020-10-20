from Command import Command
from Chasis import Chasis

class MoveX(Command):
    def __init__(self, dir: int):
        self.dir = dir

    def execute(self, chasis: Chasis):
        print("Move X \n")

        if self.dir == -1:
            chasis.moveX(-chasis.getSpeed());
        elif self.dir == 1:
            chasis.moveX(chasis.getSpeed());
        else:
            chasis.moveX(0);
