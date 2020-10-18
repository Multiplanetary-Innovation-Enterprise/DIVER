import tkinter as tk

class Display:
    def construct(self):
        window = tk.Tk()

        label = tk.Label(text="ROV GUI")
        label.pack()

        tk.mainloop()
