from ROVMessaging.Message import Message

from loggers.CSVLogger import CSVLogger

#Stores all of the recieved sensor data into a data csv log file
class DataLogger(CSVLogger):
    #Opens the file with the provided name as the prefix. Inserts columns header.
    def openFile(self, fileName:str) -> None:
        super().openFile(fileName);

        #Adds the header to the csv file
        header = [
            "time",
            "temperature",
            "externaltemp", #added 3/28/22
            'accel_x',
            'accel_y',
            'accel_z',
            'mag_x',
            'mag_y',
            'mag_z',
            'gyro_x',
            'gyro_y',
            'gyro_z',
            'acc_lin_x',
            'acc_lin_y',
            'acc_lin_z',
            'gravity_x',
            'gravity_y',
            'gravity_z',
            'heading',
            'pitch',
            'yaw',
            'quat_w',
            'quat_x',
            'quat_y',
            'quat_z'
        ];

        self._writer.writerow(header)

    def recieveMessage(self, message:Message) -> None:
        print("data")
        print(message.getContents())
        time = message.getContents()['time']

        #temperature data
        #temp = message.getContents()['internalTemp']

        externaltemp = message.getContents()['externalTemp'] #added 3/28/22

        #IMU data
        #TEMPORARILY commented out
        #acc = message.getContents()['acc']
        #magnetic = message.getContents()['magentic']
       # angV = message.getContents()['angularVelocity']
        #linAcc = message.getContents()['linAcc']
       # gravAcc = message.getContents()['gravAcc']
        #euler = message.getContents()['euler']
        #quaternion = message.getContents()['quaternion']

        #writes the entry to the csv file
        self._writer.writerow([
            time,
           # temp,
            externaltemp, #added 3/28/22
            #round(acc[0], 4),
            #round(acc[1], 4),
            #round(acc[2], 4),
            #round(magnetic[0], 4),
           # round(magnetic[1], 4),
            #round(magnetic[2], 4),
           # round(angV[0], 4),
            #round(angV[1], 4),
            #round(angV[2], 4),
           # round(linAcc[0], 4),
           # round(linAcc[1], 4),
            #round(linAcc[2], 4),
            #round(gravAcc[0], 4),
           # round(gravAcc[1], 4),
            #round(gravAcc[2], 4),
            #round(euler[0], 4),
            #round(euler[1], 4),
           # round(euler[2], 4),
           # round(quaternion[0], 4),
           # round(quaternion[1], 4),
            #round(quaternion[2], 4),
           # round(quaternion[3], 4)
        ])
