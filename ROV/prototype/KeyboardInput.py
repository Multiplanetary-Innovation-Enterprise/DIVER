import keyboard
from typing import List

from ObserverPattern import Observer, Observable

class KeyboardInput(Observable):
    observers: List[Observer] = []

    def __init__(self):
        print("SEtup\n")
        keyboard.on_press_key('w', self.forward, True)


    def forward(self, e):
        self.notify()
        print("forward\n")

    def backward(self):pass

    def up(self):pass

    def down(self):pass

    def left(self):pass

    def right(self):pass

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self):
        print("notify\n")
        for observer in self.observers:
            observer.update(self)
