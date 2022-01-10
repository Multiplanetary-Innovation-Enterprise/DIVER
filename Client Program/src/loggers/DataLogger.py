from ROVMessaging.Message import Message

from loggers.CSVLogger import CSVLogger

#Stores all of the recieved sensor data into a data csv log file
class DataLogger(CSVLogger):
    #Opens the file with the provided name as the prefix. Inserts columns header.
    def openFile(self, fileName:str):
        super().openFile(fileName);

        #Adds the header to the csv file
        header = ["time", "temperature"];
        self._writer.writerow(header)

    def recieveMessage(self, message:Message) -> None:
        temp = message.getContents()['internalTemp']
        time = message.getContents()['time']

        #print("Temp: " + str(temp) + " F @ Time: " + str(time) + "sec")

        #write entry to csv file
        self._writer.writerow([time, temp])
