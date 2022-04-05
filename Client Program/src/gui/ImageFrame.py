from tkinter import Label
from PIL import Image, ImageTk
import time

from ROVMessaging.Subscriber import Subscriber
from ROVMessaging.Message import Message
from ROVMessaging.MessageType import MessageType

from gui.Frame import Frame

#Represents a frame for showing the camera feed
class ImageFrame(Frame, Subscriber):
    __imageLabel:Label = None #The label containing the image

    lastTime = 0
    currTime = 0

    def __init__(self, parent) -> None:
        super().__init__(parent)

        #Configurations for this frame
        self.configure(bg="#FF0000")

        #Configures the grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #Image Label
        self.__imageLabel = Label(self, bg = "#00FF00")
        self.__imageLabel.grid(row = 0, column = 0, sticky = "nwes")

    #Displays the frame
    def show(self) -> None:
        self.grid(row = 0, column = 0, rowspan = 1, columnspan = 1)

    #Hides the frame
    def hide(self) -> None:
        self.grid_forget()

    def recieveMessage(self, message:Message) -> None:
        #Checks if the message is new camera frame to display
        if not message.getType() == MessageType.VISION_DATA:
            return

        #Gets the camera frame from the message
        frame = message.getContents()["camera"];

        self.setImage(frame)

    #Updates the image shown by the frame
    def setImage(self,image:Image) -> None:
        #Converts the image to a format that tkinter can show
        image = ImageTk.PhotoImage(image)

        self.__imageLabel.configure(image = image)
        self.__imageLabel.image = image

        self.lastTime = self.currTime
        self.currTime = time.time_ns()

        elapsed = (self.currTime - self.lastTime) / 1000000000

        print("Elapsed: " + str(elapsed) + " or " + str(round(1 / elapsed, 2)) + " FPS")
