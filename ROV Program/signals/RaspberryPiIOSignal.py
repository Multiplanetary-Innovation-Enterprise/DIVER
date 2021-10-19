from abc import ABC, abstractmethod

#Represents a signal that the raspberry Pi can read or write
class RaspberryPiIOSignal(ABC):
    __raspberryPi = None

    def __init__(self, pi):
        self.__raspberryPi = pi

    def getRaspberryPi(self):
        return self.__raspberryPi
