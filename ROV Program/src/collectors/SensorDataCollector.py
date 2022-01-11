from ROVMessaging.MessageChannel import MessageChannel
from ROVMessaging.MessageType import MessageType

from collectors.DataCollector import DataCollector
from ROV import ROV

#Represents a periodic sensor data collector that sends the data through the
#provided message channel
class SensorDataCollector(DataCollector):
    __rov:ROV = None #The rov itself that the sensors belong to

    def __init__(self, rov:ROV, messageChannel:MessageChannel):
        #Configures the data sender
        super().__init__(messageChannel, MessageType.SENSOR_DATA)

        self.__rov = rov

    #Gets the sensor data and returns it as a dict
    def getData(self) -> dict:
        #Get internal internal temperture of the electronics capsule
        sensorSystem = self.__rov.getSensorSystem()
        tempSensor = sensorSystem.getInternalTempSensor()

        #Formats the sensor data as key-value pairs
        sensorData = {
            'internalTemp': tempSensor.getTemperature(),
        }

        return sensorData
