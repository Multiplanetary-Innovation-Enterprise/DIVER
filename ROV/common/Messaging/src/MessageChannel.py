from MessageType import MessageType
from Subscriber import Subscriber

class MessageChannel:
    def subscribe(self, messageType: MessageType, subscriber:Subscriber) -> bool:
        return True
