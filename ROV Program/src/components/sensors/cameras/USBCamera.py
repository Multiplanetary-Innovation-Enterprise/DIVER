from components.cameras.Camera import Camera

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
        self.__camera = VideoCapture(self.__id)

    #The implementation specific closing process
    def _close(self) -> None:
        self.__camera.release()

    #Gets the current frame from the camera in its native format
    def getRawFrame(self) -> Any:
        ret, frame = self.__camera.read()

        #Checks if a frame was successfully retrieved
        if not ret:
            frame = None

        return frame

    #Gets the current frame as a PIL image
    def getFrame(self) -> Image:
        frame = self.getRawFrame()

        #Checks if a frame was successfully retrieved
        if frame == None:
            return None

        #Converts the frame from a numpy array to an PIL image
        image = Image.fromarray(frame)

        return image

    #Updates the resolution of the camera
    def setResolution(self, width:int, height:int) -> None:
        camera.set(cv.CAP_PROP_FRAME_WIDTH, width)
        camera.set(cv.CAP_PROP_FRAME_HEIGHT, height)

    #Gets the resolution of the camera
    def getResolution(self) -> tuple:
        width = camera.get(cv.CAP_PROP_FRAME_WIDTH)
        height = camera.get(cv.CAP_PROP_FRAME_HEIGHT)

    #Updates the FPS of the camera
    def setFPS(self, fps:int) -> None:
        cap.set(cv2.CAP_PROP_FPS, fps)

    #Gets the FPS of the camera
    def getFPS(self) -> int:
        return cap.get(cv2.CAP_PROP_FPS) 

    #Gets the id used for the camera by OpenCV
    def getID(self) -> int:
        return self.__id
