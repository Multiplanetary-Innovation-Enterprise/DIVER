from ROVMessaging.Message import Message

from loggers.CSVLogger import CSVLogger

#Stores acitons from input
class ActionLogger(CSVLogger):
    #Opens the file with the provided name as the prefix. Inserts columns header.
    def openFile(self, fileName:str) -> None:
        super().openFile(fileName)

        #Adds the header to the csv file
        header = [ "time", 'input']

        self._writer.writerow(header)

    def recieveMessage(self, message:Message) -> None:

        time = message.getContents()['time']
      #  externaltemp = message.getContents()['externalTemp'] #added 3/28/22

        #IMU data
        action = message.getContents()['action']


        #writes the entry to the csv file
        self._writer.writerow([
            time,
            round(action[1], 4),
            round(action[2], 4),
        ])
