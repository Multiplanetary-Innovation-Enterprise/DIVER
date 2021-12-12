import csv
from abc import ABC
from datetime import datetime

from ROVMessaging.Subscriber import Subscriber

#Represents a generic CSV logger
class CSVLogger(Subscriber, ABC):
    #Used for storing the data to a csv file
    _file = None
    _writer = None

    #Fixes ABC resolution errors
    def __init__(self):
        super(Subscriber, self).__init__()

    #Opens the file with the provided name as the prefix
    def openFile(self, fileName:str):
        #Gets the date to append to the file
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        #Opens the file with the provided name or creates a new one if it does
        #not exist
        self._file = open(fileName + str(" ") + str(now) + str(".csv"), "w+");
        self._writer = csv.writer(self._file)

    #Closes the cvs file
    def close(self):
        self._file.close()
