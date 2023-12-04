from ROVApp import *

#Python equivalent of main function
def main():
    #Starts the ROV program
    rovApp = ROVApp()
    rovApp.start()
    pass

#Checks that the code is being executed and not imported
if __name__ == "__main__":
    main()
