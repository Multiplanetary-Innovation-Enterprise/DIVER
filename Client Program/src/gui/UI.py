#The program creates a user interface for the Diver ROV Client 
#Last modified: 9/27/2022

import tkinter
from tkinter import ttk, Tk
import datetime

class UI(Tk):

    #Main method of the program. Calls other functions to create parts of the UI.
    def _init_(self, master):
        self.master = master
        master.title('ROV UI')

        #filler
        x = 0

        #set size
        self.geometry("1000x500")

        #set up grid so that there are 2 columns, the right is bigger than the left
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        #set up grid so that there are 3 rows on the left and one big row on the right
        self.rowconfigure(0, weight =1)
        self.rowconfigure(1, weight =1)
        self.rowconfigure(2, weight =1)

    #Gets data from external temperature sensor and displays it

        #create frame and set size
        extTempFrm = Tk.Frame(self)
        extTempFrm.columnconfigure(0, weight=1)

        #create header label
        exTTempLabel = ttk.Label(extTempFrm, text ="External Tempature").pack()

        #displays sensor data, displays an error if no data is found
        if x == 1 :
            #filler
            pass
        else :
            extTempFailLabel = ttk.Label(extTempFrm, text ="No External Tempature data", foreground = '#f00').pack()

        extTempFrm.grid(column = 0, row = 0, sticky=Tk.N)

        #create frame and set size
        inTempFrm = Tk.Frame(self)
        inTempFrm.columnconfigure(0, weight=1) 

        #create header label
        inTempLabel = ttk.Label(inTempFrm, text ="External Tempature").pack()

         #displays sensor data, displays an error if no data is found
        if x == 1 :
            #filler
            pass
        else :
            inTempFailLabel = ttk.Label(inTempFrm, text ="No External Tempature data", foreground = '#f00').pack()

        #return inTempFrm
        inTempFrm.grid(column = 0, row = 1,sticky=Tk.N)

    #Retrieves battery life from ?? and displays it

        #create frame and set size
        batFrm = Tk.Frame(root)
        batFrm.columnconfigure(0, weight=1)

        #create header label
        batteryLabel = ttk.Label(batFrm, text ="Battery Life").pack() 

        #displays sensor data, displays an error if no data is found
        if x == 1 :
            pass
            #filler
        else :
            batteryFailLabel = ttk.Label(batFrm, text ="No battery data", foreground = '#f00').pack()

        #return batFrm
        batFrm.grid(column = 0, row = 2, sticky=Tk.N)


    #Displays camera feed

        #create frame and sset size
        camFrm = Tk.Frame(root)
        camFrm.columnconfigure(0, weight=1) 

        #create header label
        cameraLabel = ttk.Label(camFrm, text ="Camera Feed").pack()

         #displays sensor data, displays an error if no data is found
        if x == 1:
            #filler
             pass
        else :
            camFailLabel = ttk.Label(camFrm, text ="No camera data", foreground = '#f00').pack() 

        #return camFrm
        camFrm.grid(column = 1, row = 0,rowspan = 3, sticky=Tk.N)
    
    def update_clock(self):
        #Update the label
        self.after(1000, self.update_clock) # run itself again after 1000 ms

root = Tk()
rov_UI = UI(root)
root.mainloop()
UI.update_clock()
