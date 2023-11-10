from tkinter import *
from PIL import Image,ImageTk
import cv2

from ROVMessaging.Subscriber import *

#Notes:
#Resolution: 640x480
class UI(Subscriber):
    Window = Tk()
    FakeHardware = False
    
    def __init__(self) -> None:
        self.Window.configure(bg="Dark Gray",padx=0)
        self.Window.title("ROV Control Panel")

        self.internaltemp = "NOT DETECTED"
        self.externaltemp = "NOT DETECTED"
        self.battery = "NOT DETECTED"
        self.camfeed = cv2.VideoCapture(0)
        self.logtext = "NOT DETECTED"
        self.pressure = "NOT DETECTED"

        #creates label for info to be put in
        self.infolabel = Label(self.Window,width=155,anchor=W,bg="Light Gray")

        self.log = Label(bg="black",fg="white",text=self.logtext,height=10,anchor=SW)
        self.ImageFrame = Label(self.Window)

        #configures buttons that use imported functions for use with the FakeHardware variable
        self.startbutton = Button(self.Window,text="Start ROV program",height=5,width=30)
        self.endbutton = Button(self.Window,text="End ROV program",height=5,width=30)
            
        #aligning things to grid

        self.infolabel.grid(row=1,columnspan=6,sticky=N)
        self.infolabel.grid_rowconfigure(1)

        self.ImageFrame.grid(row=2,column=4)
        self.startbutton.grid(row=3,column=2,sticky=SW)
        self.endbutton.grid(row=3,column=3,sticky=SW)

        #control panel in bottom row
        self.log.grid(row=3,column=4,sticky=EW)

    def startMainLoop(self):
        self.startVideo()
        self.startTrackingDisplays()
        self.Window.mainloop()


    #adds log
    def addLog(self,text) -> None:
        self.logtext += str(text)

#starts showing video from client's camera
    def startVideo(self) ->  None:
        
        #pulls a frame as an image
        if self.FakeHardware:
            _, self.frame = self.camfeed.read()
        #Converts image to the proper colors for display
        self.displayableImage = cv2.cvtColor(self.frame,cv2.COLOR_BGR2RGBA)

        #converts image to format readable by tkinter
        self.Arrayimage = Image.fromarray(self.displayableImage)
        self.photo_image = ImageTk.PhotoImage(image=self.Arrayimage)

        #sets image in label to frame
        self.ImageFrame.photo_image = self.photo_image
        self.ImageFrame.configure(image=self.photo_image)

        #repeats this process every 1ms
        self.Window.after(1,self.startVideo)

    #Checks for updates
    def startTrackingDisplays(self):
        self.infolabel.configure(text=(str(self.internaltemp) + "°C") + (" " * 20) + (str(self.temp) + "°C") + (" " * 20) + (str(self.pressure) + "psi"))
        self.log.configure(text=self.logtext)

        self.Window.after(1,self.startTrackingDisplays)


    def recieveMessage(self, message):
        self.time = message.getContents()['time']
        self.externaltemp = message.getContents()['externalTemp']
        self.pressure = message.getContents()['pressure']
        self.internaltemp = message.getContents()['internalTemp']
        self.action = message.getContents()['action']
        self.frame = message.getContents()['Frame']
        

