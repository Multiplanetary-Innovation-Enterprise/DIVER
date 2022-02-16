from picamera import PiCamera
from PIL import *
from io import BytesIO
from tkinter import *

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate  = 30

window = Tk()
window.geometry("1000x500")
window.title("Vision Test 7")
window.configure(background="#F5F5F5")

#Makes the window a 1x1 grid
window.grid_columnconfigure(0, weight="1")
window.grid_rowconfigure(0, weight="1")

frame = Frame(master = window)
frame.configure(bg="#FF0000")
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

#Image Label
imageLabel = Label(master = frame, bg = "#00FF00")
imageLabel.grid(row = 0, column = 0, sticky = "nwes")

#Updates the image shown by the frame
def setImage(image:Image):
    global imageLabel
    #Converts the image to a format that tkinter can show
    image = ImageTk.PhotoImage(image)

    imageLabel.configure(image = image)
    imageLabel.image = image

    print("Image set")

while True:
    stream = BytesIO()

    camera.capture(stream, format="jpeg")

    stream.seek(0)

    #Converts the frame from a byte stream to a PIL image
    image = Image.open(stream)
    setImage(image)
