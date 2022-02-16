from picamera import PiCamera as PC
from PIL import Image
from io import BytesIO

from components.sensors.cameras.Camera import Camera

#A wrapper for the picamera library to be consistent with out camera interface.
#It represents a Raspberry Pi camera that connects over the Camera Serial Interface(CSI)
class PiCamera(Camera):
    __camera:PC = None      #The underylying Raspberry Pi camera
    __stream:BytesIO = None #Holds the captured frames

    #Creates and configures the camera
    def _setup(self) -> None:
        self.__camera = PC()

    #Closes the camera and releases its resources
    def _close(self) -> None:
        self.__camera.close()
        self.__stream.close()

    #Gets the current frame from the camera in its native format
    def getRawFrame(self) -> BytesIO:
        #Creates a new byte stream to store the frame in
        self.__stream = BytesIO()

        #Captures a frame and stores it in the stream using the JPEG format
        self.__camera.capture(self.__stream, format="jpeg")

        return self.__stream

    #Gets the current frame as a PIL image
    def getFrame(self) -> Image:
        #Gets the current frame and moves to the begining of the data
        frame = self.getRawFrame()
        frame.seek(0)

        #Converts the frame from a byte stream to a PIL image
        image = Image.open(frame)

        return image

    #Updates the resolution of the camera
    def setResolution(self, width:int, height:int) -> None:
        self.__camera.resolution = (width, height)

    #Gets the resolution of the camera
    def getResolution(self) -> tuple:
        return self.__camera.resolution

    #Updates the FPS of the camera
    def setFPS(self, fps:int) -> None:
        self.__camera.framerate  = fps

    #Gets the FPS of the camera
    def getFPS(self) -> int:
        return self.__camera.fps
