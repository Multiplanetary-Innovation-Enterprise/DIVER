from subsystems.Subsystem import Subsystem
from signals.devices.SignalDevice import SignalDevice

#Represents the subsystem responsible for computer vision
class VisionSubsystem(Subsystem):
    def __init__(self, device:SignalDevice, config):
        super().__init__(device, config)

    #Performs any clean up on system shutdown
    def shutdown(self) -> None:
        pass
