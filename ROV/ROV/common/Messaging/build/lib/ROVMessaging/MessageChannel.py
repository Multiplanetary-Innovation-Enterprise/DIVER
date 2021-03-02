import concurrent.futures

from ROVMessaging.Message import Message
from ROVMessaging.MessageType import MessageType
from ROVMessaging.Subscriber import Subscriber
from ROVMessaging.HashMap import HashMap

#Represents the message channel which acts as the intermediate for publishing and
#recieving messages
class MessageChannel:
    #The list of subscribers mapped to their subscribed message type
    __messageTypesToSubscribers: HashMap = None
    #Determines if the recieved messages will be processed in parallel or not
    __isProcessingInParallel: bool = False

    #Creates the message type to subscribers hashmap
    def __init__(self):
        self.__messageTypesToSubscribers = HashMap[MessageType, list]()

    #Allows a subscriber to listen for certain message types by subscribing to them
    def subscribe(self, messageType: MessageType, subscriber:Subscriber) -> bool:
        #Retrieves all of the subscribers listening to the provided message type
        subscribers = self.__messageTypesToSubscribers.get(messageType)
        #Whether or not the subscriber was added to the subscribers list
        wasAdded = False

        #Creates the subscriber list if it does not already exist
        if subscribers == None:
            subscribers = list()

        #Add the subsciber to list if it is not already in it
        if not subscriber in subscribers:
            subscribers.append(subscriber)
            wasAdded = True

        #Updates the hashmap with the new subscribers list
        self.__messageTypesToSubscribers.put(messageType, subscribers)

        return wasAdded

    #Allows a subscriber to stop listening to certain message types by unsubscribing from them
    def unsubscribe(self, messageType: MessageType, subscriber:Subscriber) -> bool:
        #Whether or not the subscriber was removed to the subscribers list
        wasRemoved = False

        #Retrieves all of the subscribers listening to the provided message type
        subscribers = self.__messageTypesToSubscribers.get(messageType)

        #Checks if the subscribers list exists and that the provided subsriber is in it
        if not subscribers == None and subscriber in subscribers:
            subscribers.remove(subscriber)
            wasRemoved = True

        #Updates hashmap with the new subscribers list
        self.__messageTypesToSubscribers.put(messageType, subscribers)

        return wasRemoved

    #Sends the provided message to all suscribers listening for that message's message type
    def broadcast(self, message:Message) -> None:
        #Retrieves all of the subscribers listening to the provided message type
        subscribers = self.__messageTypesToSubscribers.get(message.getType())

        #Checks if there are any subscribers listening for the provided messages' type
        if subscribers == None:
            return

        #Checks whether to send the message to all of the subscribers in parallel or sequentially
        if self.__isProcessingInParallel:
            self.proccessInParallel(subscribers, message)
        else:
            self.processSequentially(subscribers, message)

    #Sends the provided message to all of the subscribers in parallel using multithreading
    def proccessInParallel(self, subscribers:list, message:Message) -> None:
        #Creates a thread pool which created one thread per subscriber and starts each thread
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(subscribers)) as executor:
            for subscriber in subscribers:
                executor.submit(subscriber.recieveMessage, message)

    #Sends the provided message to all of the subscribers sequentially
    def processSequentially(self, subscribers:list, message:Message) -> None:
        for subscriber in subscribers:
            subscriber.recieveMessage(message)

    #Checks whether the message channel has been set to process send messages in parallel
    def isProcessingInParallel(self) -> bool:
        return self.__isProcessingInParallel

    #Updates the processing status of the message channel based on the provided boolean
    #True = Processing in parallel, False = Processing sequentially
    def setProcessInParallel(self, runInParallel:bool) -> None:
        self.__isProcessingInParallel = runInParallel
