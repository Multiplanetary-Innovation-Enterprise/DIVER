from tkinter import Tk
from gui.Frame import Frame

#Represents the window the houses all GUI frames
class Window(Tk):
    __frame:Frame = None #The current frame that is being displayed

    #Creates the window and configures it
    def create(self) -> None:
        self.geometry("1000x500")
        self.title("ROV Client")
        self.configure(background="#F5F5F5")

        #Makes the window a 1x1 grid
        self.grid_columnconfigure(0, weight="1")
        self.grid_rowconfigure(0, weight="1")

    #Updates the currently shown frame to the provided frame
    def switchFrame(self, frame:Frame) -> None:
        if not self.__frame == None:
            #Removes the old frame
            self.__frame.destroy()

        #Replaces and shows the new frame
        self.__frame = frame
        self.__frame.show()

    #Gets the currently displayed frame
    def getCurrentFrame(self) -> Frame:
        return self.__frame
