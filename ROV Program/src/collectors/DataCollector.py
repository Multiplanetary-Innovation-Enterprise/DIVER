import time
import threading
from abc import ABC, abstractmethod

from ROVMessaging.MessageChannel import MessageChannel
from ROVMessaging.MessageType import MessageType
from ROVMessaging.Message import Message
from ROVMessaging.Publisher import Publisher

#Represents a periodic data collector that sends the data through the provided message channel
class DataCollector(Publisher, ABC):
    __dataType:MessageType = None           #The type of data that is being collected
    __messageChannel:MessageChannel = None  #The message channel to send the data on
    __samplePeriod:float = None             #How often to collect the data
    __isRunning:bool = False                #The state of the data collector
    __thread = None                         #The thread that the data is collected on

    def __init__(self, messageChannel:MessageChannel, dataType:MessageType, sampleFrequency:float=1):
        super(Publisher, self).__init__()

        self.__messageChannel = messageChannel
        self.__dataType = dataType

        self.setSampleFrequency(sampleFrequency)

    #Starts the data collector
    def start(self) -> None:
        if not self.__isRunning:
            self.__thread = threading.Thread(target=self.__run)
            self.__thread.start()

    #The main data collection loop
    def __run(self) -> None:
        self.__isRunning = True

        #When the data collection started
        startTime = time.time_ns()

        #Continue collecting data until stopped
        while self.__isRunning:
            #Get the data
            data = self.getData()

            #Checks if no data was retrieved
            if not data:
                #Nothing was collectd, so something went wrong. Stop data collection
                self.stop()

            #The amount of elapsed time since the data collection was started
            elapsedTime = round((time.time_ns() - startTime) / 1000000000, 2)

            #The data to send starting with the timestamp
            messageData = {
                'time': elapsedTime
            }

            #Merges the collected data with the timestamp
            messageData.update(data)

            #Sends the data to the provided message channel
            message = Message(self.__dataType, messageData)
            self.sendMessage(message, self.__messageChannel)

            #Determines how long to wait until the next round of data collection, based on the provided
            #sample frequency. This first calulates the elapsed time and converts it to seconds. Next the reaminder
            #is found by taking the mod of the sample period. This will return a number from [0, samplePeriod]. This
            #tells us how much time has already elapsed compared to the desired data collection period. Lastly, the
            #diffrence between the desired sample period and the time already spent collecting the data is found
            delay = self.__samplePeriod - (((time.time_ns() - startTime) / 1000000000) % self.__samplePeriod)
            time.sleep(delay)

    #Stops the data collection process
    def stop(self) -> None:
        #Checks if the data collector has already been stopped
        if not self.__isRunning:
            return

        self.__isRunning = False

        #Checks if trying to stop the data collector internally or externally. If
        #internal, then the thread is done, so don't wait for it  to end (hangs forever)
        if not threading.get_ident() == self.__thread.ident:
            self.__thread.join()

    #Sends the colleted data over the provided message channel
    def sendMessage(self, message:Message, messageChannel:MessageChannel) -> None:
        messageChannel.broadcast(message)

    #The data that was collected as a dict
    @abstractmethod
    def getData(self) -> dict:
        pass

    #Updates the sample period based on the provided new sample frequency
    def setSampleFrequency(self, frequency:float) -> None:
        self.__samplePeriod = 1 / frequency

    #Gets the data collection sample frequency
    def getSampleFrequency(self) -> float:
        return 1 / self.__samplePeriod

    #Updates the sample period based on the provided new sample period
    def setSamplePeriod(self, period:float) -> None:
        self.__samplePeriod = period

    #Gets the data collection sample period
    def getSamplePeriod(self) -> float:
        return self.__samplePeriod
