from subsystems.Subsystem import Subsystem
from components.controllers.Controller import Controller

#Represents the subsystem responsible for computer vision
class VisionSubsystem(Subsystem):
    def __init__(self, controller:Controller, config):
        super().__init__(controller, config)

    #Performs any clean up on system shutdown
    def shutdown(self) -> None:
        pass
