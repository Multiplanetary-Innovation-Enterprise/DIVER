from tkinter import Label
from PIL import Image, ImageTk
import time

from ROVMessaging.Subscriber import Subscriber
from ROVMessaging.Message import Message
from ROVMessaging.MessageType import MessageType

from gui.Frame import Frame

#NOTE: This class is a temporary placeholder until the new UI is implemented
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
        #self.grid_rowconfigure(0, weight=1)
        #self.grid_columnconfigure(0, weight=1)
        
        #set up grid so that there are 2 columns, the right is bigger than the left
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        #set up grid so that there are 3 rows on the left and one big row on the right
        self.rowconfigure(0, weight =1)
        self.rowconfigure(1, weight =1)
        self.rowconfigure(2, weight =1)

        #Image Label
        self.__imageLabel = Label(self, bg = "#00FF00")
        self.__imageLabel.grid(row = 0, column = 1, sticky = "nwes")

	#External Temp label
	self.__extTempLabel = Label(self, text ="External Tempature: No Data")
	self.__extTempLabel.grid(column = 0, row = 0, sticky=Tk.N)

	#Internal Temp label
	self.__inTempLabel = Label(self, text ="Internal Tempature: No Data")
	self.__inTempLabel.grid(column = 0, row = 1, sticky=Tk.N)

	#Pressure label
	self.__pressureLabel = Label(self, text ="Pressure: No Data")
	self.__pressureLabel.grid(column = 0, row = 2, sticky=Tk.N)

    #Displays the frame
    def show(self) -> None:
        self.grid(row = 0, column = 1, rowspan = 1, columnspan = 1)

    #Hides the frame
    def hide(self) -> None:
        self.grid_forget()

    def recieveMessage(self, message:Message) -> None:
        #Checks if the message is new camera frame to display
        if  message.getType() == MessageType.VISION_DATA:

		#Gets the camera frame from the message
        	frame = message.getContents()["camera"];

		self.setImage(frame)

	#Checks if the message is new sensor data to display
        if  message.getType() == MessageType.SENSOR_DATA:

		#Get internal temp value and add it to the label
		inTempValue = message.getContents()["internalTemp"];
		self.__inTempLabel = Label(self, text ="Internal Tempature: " + str(inTempValue))

		#Get external temp value and add it to the label
		extTempValue = message.getContents()["externalTemp"];
		self.__extTempLabel = Label(self, text ="External Tempature: " + str(extTempValue))

		#Get pressure value and add it to the label
		pressureValue = message.getContents()[""pressure""];
		self.__pressureLabel = Label(self, text ="Pressure: " + str(pressureValu))
       

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
