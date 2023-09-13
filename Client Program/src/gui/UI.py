from tkinter import *
from PIL import Image,ImageTk
import cv2
FakeHardware = True

#Notes:
#Resolution: 640x480

root = Tk(baseName="test")

#TODO: hook up real hardware instead of using the stuff below
if FakeHardware:
    temp = 65
    battery = "100%"
    camfeed = cv2.VideoCapture(0)
    logtext = "Test"
    pressure = 0
else:
    from loggers.ActionLogger import externaltemp,battery,cameraframe,action

#puts info in labels
batterydisplay = Label(root,text=battery)
tempdisplay = Label(root,text=(str(temp) + "F"))
camdisplay = Label(root)
pressuredisplay = Label(root,text=(str(pressure) + "psi"))
log = Label(bg="black",fg="white",text=logtext,height=10,anchor=W)

if FakeHardware:
    startbutton = Button(root,text="Start ROV program")
    endbutton = Button(root,text="End ROV program")
else:
    from ClientApp import closepipython
    from ClientApp import startpipython
    startbutton = Button(root,text="Start ROV program",command=startpipython)
    endbutton = Button(root,text="End ROV program",command=closepipython)
    
#aligning things to grid
batterydisplay.grid(row=1,column=1,sticky=N)
tempdisplay.grid(row=1,column=2,sticky=N)
pressuredisplay.grid(row=1,column=3,sticky=N)
camdisplay.grid(row=1,column=4)
startbutton.grid(row=2,column=2,sticky=N)
endbutton.grid(row=3,column=2,sticky=N)

#control panel in bottom row
log.grid(row=2,column=4,sticky=EW)


#starts showing video from client's camera
def startVideo():
    
    #pulls a frame as an image
    _, frame = camfeed.read()

    #Converts image to the proper colors for display
    displayableImage = cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA)

    #converts image to format readable by tkinter
    Arrayimage = Image.fromarray(displayableImage)
    photo_image = ImageTk.PhotoImage(image=Arrayimage)

    #sets image in label to frame
    camdisplay.photo_image = photo_image
    camdisplay.configure(image=photo_image)

    #repeats this process every 1ms
    root.after(1,startVideo)

#Checks for updates
def updateDisplays():
    batterydisplay.configure(text=battery)
    tempdisplay.configure(text=temp)
    
    root.after(1,updateDisplays)

startVideo()
updateDisplays()
root.mainloop()