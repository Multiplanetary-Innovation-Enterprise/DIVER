import queue

from ObserverPattern import Observer, Observable
from Command import Command
from Chasis import Chasis

#Represents a queue processor for a queue of commands
class Processor(Observer):
    queueRunning = 0 #Whether of not the queue is being processed currently

    #Creates the queue
    def __init__(self, chasis: Chasis):
        self.queue = queue.Queue(maxsize=1000)
        self.chasis = chasis

    #Adds a command to the queue
    def enqueue(self, command: Command):
        self.queue.put(command)

    #Removes a command from the queue
    def dequeue(self):
        return self.queue.get()

    #Processes the queue of commands
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

    #Alerts the processor that a new command is available
    def update(self, command: Command):
        print("Updated!!!\n")

        #command.execute(self.chasis)
        self.enqueue(command)

        #Processes the queue if it not already being processed
        if not self.queueRunning:
            self.processQueue()
