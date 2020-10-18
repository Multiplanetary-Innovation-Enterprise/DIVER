import queue

from ObserverPattern import Observer, Observable
from Command import Command
from Chasis import Chasis

class Processor(Observer):
    def __init__(self, chasis: Chasis):
        self.queue = queue.Queue(maxsize=1000)
        self.chasis = chasis

    def enqueue(): pass

    def dequeue(): pass

    def processQueue(): pass

    def update(self, command: Command):
        print("Updated!!!\n")
        command.execute(self.chasis)
