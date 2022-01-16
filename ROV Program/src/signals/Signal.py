from abc import ABC

from components.controllers.Controller import Controller

#Represents a generic signal that can be sent from the associated controller
class Signal(ABC):
    _controller:Controller = None #The device that can send the signal

    def __init__(self, controller:Controller):
        self._controller = controller

    #Gets the controller associated with the signal
    def getController(self) -> Controller:
        return self._controller
