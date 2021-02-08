from Message import Message
from MessageType import MessageType
from Subscriber import Subscriber
from HashMap import HashMap

class MessageChannel:
    __messageTypesToSubscribers: HashMap = None
    __isProcessingInParallel = False

    def __init__(self):
        self.__messageTypesToSubscribers = HashMap[MessageType, list]()

    def subscribe(self, messageType: MessageType, subscriber:Subscriber) -> bool:
        subscribers = self.__messageTypesToSubscribers.get(messageType)
        wasAdded = False

        #Creates the subscriber list if it does not already exist
        if subscribers == None:
            subscribers = list()

        #Add subsciber to list
        if not subscriber in subscribers:
            subscribers.append(subscriber)
            wasAdded = True

        #Update HashMap
        self.__messageTypesToSubscribers.put(messageType, subscribers)

        return wasAdded

    def unsubscribe(self, messageType: MessageType, subscriber:Subscriber) -> bool:
        wasRemoved = False

        subscribers = self.__messageTypesToSubscribers.get(messageType)

        if not subscribers == None and subscriber in subscribers:
            subscribers.remove(subscriber)
            wasRemoved = True

        self.__messageTypesToSubscribers.put(messageType, subscribers)

        return wasRemoved

    def broadcast(self, message:Message) -> None:
        subscribers = self.__messageTypesToSubscribers.get(message.getType())

        if subscribers == None:
            return

        for subscriber in subscribers:
            print(subscriber)
            subscriber.recieveMessage(message)

    def isProcessingInParallel(self) -> bool:
        return self.__isProcessingInParallel

    def setProcessInParallel(self, runInParallel:bool) -> None:
        self.__isProcessingInParallel = runInParallel
