from tkinter import *
from PIL import Image,ImageTk
import cv2
FakeHardware = True

#Notes:
#Resolution: 640x480

Window = Tk()
Window.configure(bg="Dark Gray",padx=0)
Window.title("ROV Control Panel")
if FakeHardware:
    icon = PhotoImage(file=r"C:\\Users\\notch\\OneDrive\\Documents\\GitHub\\DIVER\\Client Program\\src\\gui\\MINE.png")
Window.iconphoto(False,icon)

#TODO: hook up real hardware instead of using the stuff below
if FakeHardware:
    temp = "NOT DETECTED"
    battery = "NOT DETECTED"
    camfeed = cv2.VideoCapture(0)
    logtext = "NOT DETECTED"
    pressure = "NOT DETECTED"
else:
    from loggers.ActionLogger import externaltemp,battery,cameraframe,action

#creates label for info to be put in
infolabel = Label(Window,width=155,anchor=W,bg="Light Gray")

log = Label(bg="black",fg="white",text=logtext,height=10,anchor=SW)
ImageFrame = Label(Window)

#configures buttons that use imported functions for use with the FakeHardware variable
if FakeHardware:
    startbutton = Button(Window,text="Start ROV program",height=5,width=30)
    endbutton = Button(Window,text="End ROV program",height=5,width=30)
else:
    from ClientApp import closepipython
    from ClientApp import startpipython
    startbutton = Button(Window,text="Start ROV program",command=startpipython)
    endbutton = Button(Window,text="End ROV program",command=closepipython)
    
#aligning things to grid

infolabel.grid(row=1,columnspan=6,sticky=N)
infolabel.grid_rowconfigure(1)

ImageFrame.grid(row=2,column=4)
startbutton.grid(row=3,column=2,sticky=SW)
endbutton.grid(row=3,column=3,sticky=SW)

#control panel in bottom row
log.grid(row=3,column=4,sticky=EW)

#adds log
def addLog(text) -> None:
    logtext += str(text)

#starts showing video from client's camera
def startVideo() ->  None:
    
    #pulls a frame as an image
    _, frame = camfeed.read()

    #Converts image to the proper colors for display
    displayableImage = cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA)

    #converts image to format readable by tkinter
    Arrayimage = Image.fromarray(displayableImage)
    photo_image = ImageTk.PhotoImage(image=Arrayimage)

    #sets image in label to frame
    ImageFrame.photo_image = photo_image
    ImageFrame.configure(image=photo_image)

    #repeats this process every 1ms
    Window.after(1,startVideo)

#Checks for updates
def updateDisplays():
    infolabel.configure(text=(str(battery) + "%") + (" " * 20) + (str(temp) + "°C") + (" " * 20) + (str(pressure) + "psi"))
    log.configure(text=logtext)

    Window.after(1,updateDisplays)

startVideo()
updateDisplays()
Window.mainloop()