from typing import Any
from abc import ABC, abstractmethod

from PIL import Image

#Represents a generic camera
class Camera(ABC):
    _isActive:bool = False #Whether or not the camera is on

    #Runs the camera setup
    def __init__(self):
        self.setup()

    #Whether or not the camera is currently on
    def isActive(self) -> bool:
        return self._isActive

    #Sets the cameras up to begin capturing frames
    def setup(self) -> None:
        #Checks if the camera is already setup
        if self._isActive:
            return

        self._isActive = True
        self._setup()

    #The implementation specific setup process
    @abstractmethod
    def _setup(self) -> None:
        pass

    #Stops the camera and releases its resources
    def close(self) -> None:
        #Checks if the camera was already closed
        if not self._isActive:
            return

        self._isActive = False
        self._close()

    #The implementation specific closing process
    @abstractmethod
    def _close(self) -> None:
        pass

    #Gets the current frame from the camera in its native format
    @abstractmethod
    def getRawFrame(self) -> Any:
        pass

    #Gets the current frame as a PIL image
    @abstractmethod
    def getFrame(self) -> Image:
        pass

    #Updates the resolution of the camera
    @abstractmethod
    def setResolution(self, width:int, height:int) -> None:
        pass

    #Gets the resolution of the camera
    @abstractmethod
    def getResolution(self) -> tuple:
        pass

    #Updates the FPS of the camera
    @abstractmethod
    def setFPS(self, fps:int) -> None:
        pass

    #Gets the FPS of the camera
    @abstractmethod
    def getFPS(self) -> int:
        pass
