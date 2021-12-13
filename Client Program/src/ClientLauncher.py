from ROVClient import *

#Python equivalent of main function
def main():
    #Starts the ROV client program
    rovClient = ROVClient()
    rovClient.start()

#Checks that the code is being executed and not imported
if __name__ == "__main__":
    main()
