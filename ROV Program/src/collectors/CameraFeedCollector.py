from ROVMessaging.MessageChannel import MessageChannel
from ROVMessaging.MessageType import MessageType

from collectors.DataCollector import DataCollector
from subsystems.VisionSubsystem import VisionSubsystem

#Represents a periodic camera feed collector that sends the frames through
#provided message channel
class CameraFeedCollector(DataCollector):
    __subsystem:VisionSubsystem = None #The subsystem that the camera belongs to

    def __init__(self, subsystem:VisionSubsystem, messageChannel:MessageChannel):
        #Configures the data sender
        super().__init__(messageChannel, MessageType.VISION_DATA)

        self.__subsystem = subsystem

    #Gets the current frame from the camera and returns it in a dict
    def getData(self) -> dict:
        #Gets the camera from the subsystem
        camera = self.__subsystem.getCamera()

        #Formats the vision data as key-value pairs
        visionData = {
            'camera': camera.getFrame()
        }

        return visionData
