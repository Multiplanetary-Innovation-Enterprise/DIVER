from typing import List

from ObserverPattern import Observer, Observable
from Command import Command
from MoveCommands  import MoveX
from SpeedCommands import IncreaseSpeed, DecreaseSpeed

class Input(Observable):
    def increaseSpeed(self, e):
        self.notify(IncreaseSpeed())

    def decreaseSpeed(self, e):
        self.notify(DecreaseSpeed())

    def forward(self, e):
        self.notify(MoveX(1))
        print("forward\n")

    def backward(self, e):
        self.notify(MoveX(-1))
        print("backward\n")

    def stopX(self, e):
        self.notify(MoveX(0))
        print("Stop X\n")

    def right(self, e):pass

    def stopY(self, e):pass

    def up(self, e):pass

    def down(self, e):pass

    def stopZ(self, e):pass

    def left(self, e):pass

    def notify(self, command: Command):
        for observer in self.observers:
            observer.update(command)
