from ROVMessaging.MessageChannel import MessageChannel
from ROVMessaging.MessageType import MessageType

from collectors.DataCollector import DataCollector
from subsystems.SensorSubsystem import SensorSubsystem

#Represents a periodic sensor data collector that sends the data through the
#provided message channel
class SensorDataCollector(DataCollector):
    __subsystem:SensorSubsystem = None #The subsystem that the sensors belong to

    def __init__(self, subsystem:SensorSubsystem, messageChannel:MessageChannel):
        #Configures the data sender
        super().__init__(messageChannel, MessageType.SENSOR_DATA)

        self.__subsystem = subsystem

    #Gets the sensor data and returns it as a dict
    def getData(self) -> dict:
        #Get internal internal temperature of the electronics capsule
        tempSensor = self.__subsystem.getInternalTempSensor()
        imu = self.__subsystem.getIMU()
        exTempSensor = self.__subsystem.getExternalTempSensor() #added 4/6/22
        pressureSensor = self.__subsystem.getPressureSensor()             # added 4/8/22

        #The collected sensor data
        sensorData = {}

        #Checks if the temperature sensor is connected
        if tempSensor.isConnected():
            sensorData["internalTemp"] = tempSensor.getTemperature()

        #Checks if the imu sensor is connected
        if imu.isConnected():
            #Appends the IMU data to the rest of the sensor data
            sensorData.update(imu.getSensorData().toDict())

        #Checks if the external temperature sensor is connected
        if exTempSensor.isConnected():
            sensorData["externalTemp"] = exTempSensor.getTemperature() #added 4/6/22

        #Checks if the external pressure sensor is connected
        if pressureSensor.isConnected():
            pressureSensor._read()  #added 4/8/22
            sensorData["pressure"]=pressureSensor._getPressure()

        return sensorData
