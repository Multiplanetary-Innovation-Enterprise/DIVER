from subsystems.Subsystem import Subsystem
from components.controllers.Controller import Controller
from components.sensors.cameras.Camera import Camera
from components.sensors.cameras.PiCamera import PiCamera

#Represents the subsystem responsible for computer vision
class VisionSubsystem(Subsystem):
    __camera:Camera = None #The main navigation camera on the ROV

    def __init__(self, controller:Controller, config):
        super().__init__(controller, config)

        self.__camera = PiCamera()
        self.__camera.setResolution(640, 480)
        self.__camera.setFPS(60)

        print(self.__camera.getResolution())

    #Gets the main navigational camera of the ROV
    def getCamera(self) -> Camera:
        return self.__camera

    #Performs any clean up on system shutdown
    def shutdown(self) -> None:
        pass
