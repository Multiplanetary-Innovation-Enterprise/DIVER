from ROVMessaging.MessageChannel import MessageChannel
from ROVMessaging.MessageType import MessageType

from collectors.DataCollector import DataCollector
from subsystems.Subsystem import Subsystem

#Represents a periodic sensor data collector that sends the data through the
#provided message channel
class SensorDataCollector(DataCollector):
    __subsystem:Subsystem = None #The rov itself that the sensors belong to

    def __init__(self, subsystem:Subsystem, messageChannel:MessageChannel):
        #Configures the data sender
        super().__init__(messageChannel, MessageType.SENSOR_DATA)

        self.__subsystem = subsystem

    #Gets the sensor data and returns it as a dict
    def getData(self) -> dict:
        #Get internal internal temperature of the electronics capsule
        tempSensor = self.__subsystem.getInternalTempSensor()
        imu = self.__subsystem.getIMU()

        #Formats the sensor data as key-value pairs
        sensorData = {
            'internalTemp': tempSensor.getTemperature(),
        }

        #Appends the IMU data to the rest of the sensor data
        sensorData.update(imu.getSensorData().toDict())
        
        return sensorData
