import tkinter as tk

#Represents the GUI for the ROV
class Display:
    #Creates the display
    def construct(self):
        window = tk.Tk()

        label = tk.Label(text="ROV GUI")
        label.pack()
        print("Ready!\n")
        tk.mainloop()
