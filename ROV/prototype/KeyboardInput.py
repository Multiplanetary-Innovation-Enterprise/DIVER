import keyboard
from typing import List

from ObserverPattern import Observer, Observable
from Command import Command
from MoveX import MoveX
from IncreaseSpeed import IncreaseSpeed

class KeyboardInput(Observable):
    observers: List[Observer] = []

    def __init__(self):
        keyboard.on_press_key('w', self.forward, True)
        keyboard.on_release_key('w', self.stopX, True)
        keyboard.on_press_key('up', self.increaseSpeed, True)

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

    def increaseSpeed(self, e):
        self.notify(IncreaseSpeed())
        print("increaseSpeed X\n")

    def decreaseSpeed(self, e):
        pass

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self, command: Command):
        print("notify\n")
        for observer in self.observers:
            observer.update(command)
