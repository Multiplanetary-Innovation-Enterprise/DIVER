import tkinter as tk

class Display:
    #Make good GUI TODO
    def construct(self):
        window = tk.Tk()

        label = tk.Label(text="ROV GUI")
        label.pack()
        print("Ready!\n")
        tk.mainloop()
