from ObserverPattern import Event

class MessageEvent(Event):
    message = None

    def __init__(self, message):
        self.message = message

    def getMessage(self):
        return self.message
