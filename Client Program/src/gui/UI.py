from tkinter import *
from PIL import Image,ImageTk
import cv2
from loggers.ActionLogger import externaltemp,battery,cameraframe,action
FakeHardware = False

#Notes:
#Resolution: 640x480

root = Tk(baseName="test")

#TODO: hook up real hardware instead of using the stuff below
temp = 65
battery = "100%"
camfeed = cv2.VideoCapture(0)
logtext = "Test"

#puts info in labels
batterydisplay = Label(root,text=battery)
tempdisplay = Label(root,text=str(temp) + "F")
camdisplay = Label()
log = Label(bg="black",fg="white",text=logtext,height=10,anchor=W)

button1 = Button(text="hotpockets")
button1.grid(row=2,column=2,sticky=N)

#aligning things to grid
batterydisplay.grid(row=1,column=1,sticky=N)
tempdisplay.grid(row=1,column=2,sticky=N)
camdisplay.grid(row=1,column=3)
#control panel in bottom row
log.grid(row=2,column=3,sticky=EW)


#starts showing video
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

startVideo()
root.mainloop()