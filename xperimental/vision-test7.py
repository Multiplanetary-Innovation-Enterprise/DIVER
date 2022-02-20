from picamera import PiCamera
import PIL.Image
from PIL import ImageTk
from io import BytesIO
from tkinter import *

import threading
import time
import numpy as np

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate  = 30

window = Tk()
window.geometry("1000x500")
window.title("Vision Test 7")
window.configure(background="#00FF00")

#Makes the window a 1x1 grid
window.grid_columnconfigure(0, weight="1")
window.grid_rowconfigure(0, weight="1")

frame = Frame(master = window)
frame.configure(bg="#FF0000")
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid(row = 0, column = 0, sticky = "nwes")

#Image Label
imageLabel = Label(master = frame, bg = "#0000FF")
imageLabel.grid(row = 0, column = 0, sticky = "nwes")

cTime = 0
lastTime = 0

#Updates the image shown by the frame
def setImage(image:Image):
    global imageLabel
    #Converts the image to a format that tkinter can show
    #image = ImageTk.PhotoImage(image)

    #imageLabel.configure(image = image)
    #imageLabel.image = image

    print("Image set")

def update():
    global lastTime
    global cTime
    
    print("Update")
    while True:
        lastTime = cTime
        cTime = time.time_ns()
        
        print("Elapsed: " + str((cTime - lastTime) / 1000000000))
        
        #stream = BytesIO()
        output = np.empty((480,640, 3), dtype=np.uint8)
        
        camera.capture(output, format="rgb", use_video_port=True)

        #stream.seek(0)

        #Converts the frame from a byte stream to a PIL image
        #image = PIL.Image.fromarray("RGB", (640, 480), stream, "raw", "RGB", 0, 1)
       
        image = PIL.Image.fromarray(output)
        setImage(image)

thread = threading.Thread(target=update)
thread.start()

print("main loop")
window.mainloop()

