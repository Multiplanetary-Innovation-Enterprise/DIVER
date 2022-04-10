from ROVMessaging.Message import Message

from loggers.CSVLogger import CSVLogger

#Stores all of the recieved sensor data into a data csv log file
class DataLogger(CSVLogger):
    __isHeaderCreated:bool = False #Whether or not the csv header has been created
    __header:list #The header containing the data labels

    #Opens the file with the provided name as the prefix. Inserts columns header.
    def openFile(self, fileName:str) -> None:
        super().openFile(fileName);

        # #Adds the header to the csv file
        # header = [
        #     "time",
        #     "temperature",
        #    # "externaltemp", #added 3/28/22
        #     "pressure",
        #     'accel_x',
        #     'accel_y',
        #     'accel_z',
        #     'mag_x',
        #     'mag_y',
        #     'mag_z',
        #     'gyro_x',
        #     'gyro_y',
        #     'gyro_z',
        #     'acc_lin_x',
        #     'acc_lin_y',
        #     'acc_lin_z',
        #     'gravity_x',
        #     'gravity_y',
        #     'gravity_z',
        #     'heading',
        #     'pitch',
        #     'yaw',
        #     'quat_w',
        #     'quat_x',
        #     'quat_y',
        #     'quat_z'
        # ];

        # self._writer.writerow(header)

    def recieveMessage(self, message:Message) -> None:
        #The incoming sensor data and the actual data being saved to the file
        sensorData = message.getContents()
        data = []

        print("DATA")
        print(sensorData)

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

      #   #temperature data
      #   temp = message.getContents()['internalTemp']
      #
      # #  externaltemp = message.getContents()['externalTemp'] #added 3/28/22
      #   pressure = message.getContents()['pressure'] #added 4/8/22
      #
      #   #IMU data
      #   acc = message.getContents()['acc']
      #   magnetic = message.getContents()['magentic']
      #   angV = message.getContents()['angularVelocity']
      #   linAcc = message.getContents()['linAcc']
      #   gravAcc = message.getContents()['gravAcc']
      #   euler = message.getContents()['euler']
      #   quaternion = message.getContents()['quaternion']
      #
      #   #writes the entry to the csv file
      #   self._writer.writerow([
      #       time,
      #       temp,
      #    #  externaltemp, #added 3/28/22
      #       pressure, #added 4/8/22
      #       round(acc[0], 4),
      #       round(acc[1], 4),
      #       round(acc[2], 4),
      #       round(magnetic[0], 4),
      #       round(magnetic[1], 4),
      #       round(magnetic[2], 4),
      #       round(angV[0], 4),
      #       round(angV[1], 4),
      #       round(angV[2], 4),
      #       round(linAcc[0], 4),
      #       round(linAcc[1], 4),
      #       round(linAcc[2], 4),
      #       round(gravAcc[0], 4),
      #       round(gravAcc[1], 4),
      #       round(gravAcc[2], 4),
      #       round(euler[0], 4),
      #       round(euler[1], 4),
      #       round(euler[2], 4),
      #       round(quaternion[0], 4),
      #       round(quaternion[1], 4),
      #       round(quaternion[2], 4),
      #       round(quaternion[3], 4)
      #   ])
