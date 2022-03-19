#The program creates a user interface for the Diver ROV Client 
#Last modified: 3/19/2022

import tkinter as tk
from tkinter import ttk

class UI(Tk, Window):
    #creates root
    root = tk.Tk()
    root.title('ROV UI')

    #filler value for sensor data
    x = 0

    """
    Is the main method of the program. Calls other functions to create parts of the UI.
    """
    def start():

        #set size
        root.geometry("1000x500")

        #set up grid so that there are 2 columns, the right is bigger than the left
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=3)

        #set up grid so that there are 3 rows on the left and one big row on the right
        root.rowconfigure(0, weight =1)
        root.rowconfigure(1, weight =1)
        root.rowconfigure(2, weight =1)

        #creates the external tempature frame and adds it to the root
        inputExtTemp = extTemp(root)
        inputExtTemp.grid(column = 0, row = 0, sticky=tk.N)

        #creates the internal tempature frame and adds it to the root
        inputInTemp = inTemp(root)
        inputInTemp.grid(column = 0, row = 1,sticky=tk.N)

         #creates the battery frame and adds it to the root
        inputBat = batteryDisplay(root)
        inputBat.grid(column = 0, row = 2, sticky=tk.N)

         #create the  tempature frame and adds it to the root
        inputCam = cameraFeed(root)
        inputCam.grid(column = 1, row = 0,rowspan = 3, sticky=tk.N)

        #runs root
        root.mainloop()

    """
    Gets data from external temperature sensor and displays it
    """
    def extTemp(container):

        #create frame and set size
        extTempFrm = tk.Frame(root)
        extTempFrm.columnconfigure(0, weight=1)

        #create header label
        exTTempLabel = ttk.Label(extTempFrm, text ="External Tempature").pack()

        #displays sensor data, displays an error if no data is found
        if x == 1 :
            #filler
            pass
        else :
            extTempFailLabel = ttk.Label(extTempFrm, text ="No External Tempature data", foreground = '#f00').pack()

        #returns frame
        return extTempFrm

    """
    Retirieves internal temperature and displays it
    """
    def inTemp(container):

        #create frame and set size
        inTempFrm = tk.Frame(root)
        inTempFrm.columnconfigure(0, weight=1) 

        #create header label
        inTempLabel = ttk.Label(inTempFrm, text ="External Tempature").pack()

         #displays sensor data, displays an error if no data is found
        if x == 1 :
            #filler
            pass
        else :
            inTempFailLabel = ttk.Label(inTempFrm, text ="No External Tempature data", foreground = '#f00').pack()

        return inTempFrm

    """
    Retrieves battery life from ?? and displays it
    """
    def batteryDisplay(container):

        #create frame and set size
        batFrm = tk.Frame(root)
        batFrm.columnconfigure(0, weight=1)

        #create header label
        batteryLabel = ttk.Label(batFrm, text ="Battery Life").pack() 

        #displays sensor data, displays an error if no data is found
        if x == 1 :
            pass
            #filler
        else :
            batteryFailLabel = ttk.Label(batFrm, text ="No battery data", foreground = '#f00').pack()

        return batFrm

    """
    Displays camera feed
    """
    def cameraFeed(container):

        #create frame and sset size
        camFrm = tk.Frame(root)
        camFrm.columnconfigure(0, weight=1) 

        #create header label
        cameraLabel = ttk.Label(camFrm, text ="Camera Feed").pack()

         #displays sensor data, displays an error if no data is found
        if x == 1:
            #filler
             pass
        else :
            camFailLabel = ttk.Label(camFrm, text ="No camera data", foreground = '#f00').pack() 

        return camFrm

    #control to make sure mehtods are called in the right order
    if __name__ == "__main__":
        start()
