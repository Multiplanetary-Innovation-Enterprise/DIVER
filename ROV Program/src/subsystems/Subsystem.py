from abc import ABC, abstractmethod

from components.controllers.Controller import Controller

#Represents a generic subsytem
class Subsystem(ABC):
    _config = None              #The configuration file
    _controller:Controller = None #The controlling controller

    def __init__(self, controller:Controller, config):
        self._controller = controller
        self._config = config

    #Performs any clean up on system shutdown
    @abstractmethod
    def shutdown(self) -> None:
        pass
