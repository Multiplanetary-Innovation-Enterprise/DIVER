from abc import ABC, abstractmethod
import tkinter as tk

#Represents a wrapper for a tkinter frame
class Frame(tk.Frame, ABC):
    __parent = None #The parent of the frame

    #Sets the parent of this frame
    def __init__(self, parent) -> None:
        self.__parent = parent
        super().__init__(master=parent)

    #Displays the frame
    @abstractmethod
    def show(self) -> None:
        pass

    #Hides the frame
    @abstractmethod
    def hide(self) -> None:
        pass

    #Gets the parent of this frame
    def getParent(self):
        return self.__parent

    #Destroys the frame by releasing the resources that it uses
    def destroy(self) -> None:
        self.hide()
        super().destroy()
