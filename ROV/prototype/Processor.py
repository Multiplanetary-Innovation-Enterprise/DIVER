import queue

from ObserverPattern import Observer, Observable

class Processor(Observer):
    def __init__(self):
        self.queue = queue.Queue(maxsize=1000)

    def enqueue(): pass

    def dequeue(): pass

    def processQueue(): pass

    def update(self, observable: Observable):
        print("Updated!!!\n")
