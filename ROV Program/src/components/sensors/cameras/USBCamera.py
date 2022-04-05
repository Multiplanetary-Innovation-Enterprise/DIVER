import numpy as np
from PIL import Image
import cv2 as cv

from components.sensors.cameras.Camera import Camera

#Represents a camera that operates over the Universal Serial Bus(USB)
class USBCamera(Camera):
    __id:int = -1   #The id of the camera in OpenCV
    __camera = None #The OpenCV instance of the camera

    #Runs the camera setup
    def __init__(self, id:int):
        self.__id = id

        self.setup()

    #The implementation specific setup process
    def _setup(self) -> None:
        self.__camera = cv.VideoCapture(self.__id)

    #The implementation specific closing process
    def _close(self) -> None:
        self.__camera.release()

    #Gets the current frame from the camera in its native format
    def getRawFrame(self) -> np.array:
        ret, frame = self.__camera.read()

        #Checks if a frame was successfully retrieved
        if not ret:
            print("Not Frame")
            frame = None
        else:
            #Convert the frame to the RGB format
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        return frame

    #Gets the current frame as a PIL image
    def getFrame(self) -> Image:
        frame = self.getRawFrame()

        #Checks if a frame was successfully retrieved
        if not np.any(frame):
            return None
        #Converts the frame from a numpy array to an PIL image
        image = Image.fromarray(frame)

        return image

    #Updates the resolution of the camera
    def setResolution(self, width:int, height:int) -> None:
        self.__camera.set(cv.CAP_PROP_FRAME_WIDTH, width)
        self.__camera.set(cv.CAP_PROP_FRAME_HEIGHT, height)

    #Gets the resolution of the camera
    def getResolution(self) -> tuple:
        width = self.__camera.get(cv.CAP_PROP_FRAME_WIDTH)
        height = self.__camera.get(cv.CAP_PROP_FRAME_HEIGHT)

    #Updates the FPS of the camera
    def setFPS(self, fps:int) -> None:
        self.__camera.set(cv.CAP_PROP_FPS, fps)

    #Gets the FPS of the camera
    def getFPS(self) -> int:
        return self.__camera.get(cv.CAP_PROP_FPS)

    #Gets the id used for the camera by OpenCV
    def getID(self) -> int:
        return self.__id
