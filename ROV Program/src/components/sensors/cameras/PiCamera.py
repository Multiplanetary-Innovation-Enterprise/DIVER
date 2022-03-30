from picamera import PiCamera as PC
from PIL import Image
import numpy as np

from components.sensors.cameras.Camera import Camera

#A wrapper for the picamera library to be consistent with out camera interface.
#It represents a Raspberry Pi camera that connects over the Camera Serial Interface(CSI)
class PiCamera(Camera):
    __camera:PC = None      #The underylying Raspberry Pi camera
    __frameWidth:int = 0
    __frameHeight:int = 0

    #Creates and configures the camera
    def _setup(self) -> None:
        self.__camera = PC()

    #Closes the camera and releases its resources
    def _close(self) -> None:
        self.__camera.close()

    #Gets the current frame from the camera in its native format
    def getRawFrame(self) -> np.array:
        #Creates a numpy array to store the frame in
        frame = np.empty((self.__frameHeight, self.__frameWidth, 3), dtype=np.uint8)

        #Captures a frame and stores it in the stream using the JPEG format
        self.__camera.capture(frame, format="rgb", use_video_port=True)

        return frame

    #Gets the current frame as a PIL image
    def getFrame(self) -> Image:
        #Gets the current frame in the raw format
        frame = self.getRawFrame()

        #Converts the frame fram a numpy array to a PIL image
        image = Image.fromarray(frame)

        return image

    #Updates the resolution of the camera
    def setResolution(self, width:int, height:int) -> None:
        self.__camera.resolution = (width, height)

        self.__frameWidth = width
        self.__frameHeight = height

    #Gets the resolution of the camera
    def getResolution(self) -> tuple:
        return self.__camera.resolution

    #Updates the FPS of the camera
    def setFPS(self, fps:int) -> None:
        self.__camera.framerate  = fps

    #Gets the FPS of the camera
    def getFPS(self) -> int:
        return self.__camera.fps
