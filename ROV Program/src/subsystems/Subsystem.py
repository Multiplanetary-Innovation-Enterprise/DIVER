from abc import ABC, abstractmethod

from signals.devices.SignalDevice import SignalDevice

#Represents a generic subsytem
class Subsystem(ABC):
    _config = None              #The configuration file
    _device:SignalDevice = None #The controlling device

    def __init__(self, device:SignalDevice, config):
        self._device = device
        self._config = config

    #Performs any clean up on system shutdown
    @abstractmethod
    def shutdown(self) -> None:
        pass
