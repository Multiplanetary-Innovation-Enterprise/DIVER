from PIL import Image
from datetime import datetime

from commands.Command import Command
from subsystems.VisionSubsystem import VisionSubsystem

#The command for capturing an image
class CaptureImageCommand(Command):
    __visionSystem:VisionSubsystem = None #The ROV's propulsion system

    def __init__(self, visionSystem:VisionSubsystem):
        self.__visionSystem =visionSystem

    #Executes the command
    def execute(self) -> None:
        print("Capturing image")

        camera = self.__visionSystem.getCamera()

        # camera.setResolution(2592, 1944)

        image = camera.getFrame()
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        #camera.setResolution(640, 480)

        image.save('Image capture ' + timestamp + '.png')

    #Whether or not the command can be repeated back to back
    def isRepeatable(self) -> bool:
        return True

    #The action code associated with this command
    def getActionCode() -> int:
        return 14
