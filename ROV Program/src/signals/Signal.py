from abc import ABC

from signals.devices.SignalDevice import SignalDevice

#Represents a generic signal that can be sent from the associated signal device
class Signal(ABC):
    __device: SignalDevice = None #The device that can send the signal

    def __init__(self, device:SignalDevice):
        self.__device = device

    #Gets the device associated with the signal
    def getDevice(self) -> SignalDevice:
        return self.__device