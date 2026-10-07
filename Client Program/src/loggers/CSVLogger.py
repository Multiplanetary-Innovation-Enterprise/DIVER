import csv
import os
from abc import ABC
from datetime import datetime

from ROVMessaging.Subscriber import Subscriber

#Represents a generic CSV logger
class CSVLogger(Subscriber, ABC):
    __file = None                  #The file to save the data to
    __writer = None                #The writer used to save the data to the csv file
    __isHeaderCreated:bool = False #Whether or not the csv header has been created
    __header:list = []             #The header containing the data labels

    #Fixes ABC resolution errors
    def __init__(self):
        super(Subscriber, self).__init__()

    #Opens the file with the provided name as the prefix
    #def openFile(self, fileName:str) -> None:
     #   #Creates the logs directory if it does not exist
      #  dir = "../logs/data/"
       # os.makedirs(dir, exist_ok = True)

        ##Gets the date to append to the file
        #now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        ##Opens the file with the provided name or creates a new one if it does
        ##not exist
        #self.__file = open(str(fileName) + str(" ") + str(now) + str(".csv"), "w+");
        #self.__writer = csv.writer(self.__file)

    def openFile(self, fileName: str) -> None:
        # 1. Sanitize fileName to prevent accidental subdirectories
        # This replaces slashes with underscores so Linux doesn't look for non-existent folders
        safe_file_name = str(fileName).replace("/", "_").replace("\\", "_")

        # 2. Safely get the absolute directory of this script file
        script_dir = os.path.dirname(os.path.realpath(__file__))
        
        # 3. Form absolute path to the logs directory and create it
        dir_path = os.path.abspath(os.path.join(script_dir, "../logs/data/"))
        os.makedirs(dir_path, exist_ok=True)
        
        # 4. Get the current date and time
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        # 5. Build final file path safely
        file_name = f"{safe_file_name}_{now}.csv"
        file_path = os.path.join(dir_path, file_name)
        
        # 6. Open the file securely
        # This is the line that was crashing.
        self.__file = open(file_path, "w+", newline='')
        self.__writer = csv.writer(self.__file)


    #Writes the next row to the csv file using the provided data in dict form
    def writeRow(self, data:dict, missingVal:str="X") -> None:
        #Creates the header if it has not already been created
        if not self.__isHeaderCreated:
            #Gets all of the keys from the dict that label the sensor data
            self.__header = list(data.keys())

            #Writes the header to the data file
            self.__writer.writerow(self.__header)
            self.__isHeaderCreated = True

        #The next row of data to output as a list
        row = []

        #Iterates through all of the data labels in the header
        for dataLabel in self.__header:
            #Checks if the current data label is in the set of new received data
            if dataLabel in data:
                value = data[dataLabel]
            else:
                #The data label was not found in the current set of data, so use
                #the missing value placeholder
                value = missingVal

            #Add the value to the next row to save to the file
            row.append(value)

        self.__writer.writerow(row)

    #Closes the CSV file
    def close(self) -> None:
        self.__file.close()
