import queue

from ObserverPattern import Observer, Observable
from Command import Command
from Chasis import Chasis

class Processor(Observer):
    queueRunning = 0
    
    def __init__(self, chasis: Chasis):
        self.queue = queue.Queue(maxsize=1000)
        self.chasis = chasis

    def enqueue(self, command: Command):
        self.queue.put(command)

    def dequeue(self):
        return self.queue.get()


    #Run queue in seperate thread TODO
    def processQueue(self):
        self.queueRunning = 1
        print("Processing Queue!\n")
        while not self.queue.empty():
            command = self.dequeue()
            command.execute(self.chasis)

        self.queueRunning = 0

        #command = queue.get()
        #command.execute(self.chasis)

    def update(self, command: Command):
        print("Updated!!!\n")
        #command.execute(self.chasis)
        self.enqueue(command)

        if not self.queueRunning:
            self.processQueue()
