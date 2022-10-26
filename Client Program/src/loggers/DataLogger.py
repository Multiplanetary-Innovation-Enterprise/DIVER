from ROVMessaging.Message import Message

from loggers.CSVLogger import CSVLogger

#Stores all of the recieved sensor data into a data csv log file
class DataLogger(CSVLogger):
    def recieveMessage(self, message:Message) -> None:
        #The incoming sensor data and the actual data being saved to the file
        sensorData = message.getContents()

        #Saves the sensor data to the CSV file. If a sensor stops working or is
        #disconnected, it will use the default value of "X" to indicate this
        self.writeRow(sensorData, "X")
