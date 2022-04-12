from ROVMessaging.Message import Message

from loggers.CSVLogger import CSVLogger

#Stores all of the recieved sensor data into a data csv log file
class DataLogger(CSVLogger):
    __isHeaderCreated:bool = False #Whether or not the csv header has been created
    __header:list #The header containing the data labels

    def recieveMessage(self, message:Message) -> None:
        #The incoming sensor data and the actual data being saved to the file
        sensorData = message.getContents()
        data = []

        #Creates the header if it has not already been created
        if not self.__isHeaderCreated:
            #Gets all of the keys from the dict that label the sensor data
            self.__header = list(sensorData.keys())

            #Writes the header to the data file
            self._writer.writerow(self.__header)
            self.__isHeaderCreated = True

        #Iterates through all of the data labels in the header
        for dataLabel in self.__header:
            #Checks if the current data label is in the set of new received data
            if dataLabel in sensorData:
                value = sensorData[dataLabel]
            else:
                #The data label was not found in the current set of data. This could be
                #caused by a sensor malfunctioning or getting disconnected
                value = "X"

            #Add the value to the next row to save to the file
            data.append(value)

        #Outputs the current processed data to the file
        self._writer.writerow(data)
