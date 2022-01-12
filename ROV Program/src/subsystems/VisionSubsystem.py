import configparser

from signals.devices.SignalDevice import SignalDevice

class VisionSubsystem:
    __device:SignalDevice = None

    def __init__(self, device:SignalDevice):
        self.__device = device
