import time
import threading

from ROVMessaging.MessageChannel import MessageChannel
from ROVMessaging.MessageType import MessageType
from ROVMessaging.Message import Message
from ROVMessaging.Action import Action
from ROVMessaging.Publisher import Publisher

#Temporary until integrated into command system
class DataSender(Publisher):
    __messageChannel:MessageChannel = None
    __isRunning = False
    __thread = None

    def __init__(self, messageChannel:MessageChannel):
        self.__messageChannel = messageChannel

    def start(self):
        print("Sending data start")
        if not self.__isRunning:
            self.__thread = threading.Thread(target=self.__run)
            self.__thread.start()

    def __run(self):
        self.__isRunning = True
        #print("Doesn't run without this print statement because python")
        # while self.__isRunning:
        #     print("data sending")
        #
        #     #Get temperature
        #     sensorSystem = rov.getSensorSystem()
        #     #tempSensor = sensorSystem.getInternalTempSensor()
        #
        #     #Convert time to seconds
        #     elapsedTime = round((time.time_ns() - startTime) / 1000000000, 2)
        #
        #     #Only sensor data is temp data so far
        #     sensorData = {
        #         'internalTemp': tempSensor.getTemperature(),
        #         'time': elapsedTime
        #     }
        #
        #     message = Message(MessageType.SENSOR_DATA, sensorData)
        #
        #     self.sendMessage(message, self.__messageChannel)
        #
        #     time.sleep(1)
        pass


    def stop(self):
        self.__isRunning = False


    #Creates the action message and sends it over the message channel
    def sendMessage(self, message:Message, messageChannel:MessageChannel):
        print(message)
        messageChannel.broadcast(message)

startTime = time.time_ns()
