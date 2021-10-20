from ROVMessaging.Publisher import Publisher
from ROVMessaging.Message import Message
from ROVMessaging.MessageChannel import MessageChannel
from ROVMessaging.MessageType import MessageType
from ROVMessaging.Action import Action

class Input(Publisher):
    __messageChannel:MessageChannel = None

    def __init__(self, messageChannel:MessageChannel):
        self.__messageChannel = messageChannel

    #Sends move forward action
    def forward(self, event):
        print("Forward")
        message = Message(MessageType.ACTION, Action.MOVE_XY_FORWARD)
        self.sendMessage(message, self.__messageChannel)

    #Send move backward action
    def backward(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_XY_BACKWARD)
        self.sendMessage(message, self.__messageChannel)

    def stopXY(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_XY_STOP)
        self.sendMessage(message, self.__messageChannel)

    #Send move up action
    def up(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_Z_POS)
        self.sendMessage(message, self.__messageChannel)

    #Send move down action
    def down(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_Z_NEG)
        self.sendMessage(message, self.__messageChannel)

    def stopZ(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_Z_STOP)
        self.sendMessage(message, self.__messageChannel)

    #Sends a move right command
    def right(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_XY_LEFT)
        self.sendMessage(message, self.__messageChannel)

    #Sends a move left command
    def left(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_XY_RIGHT)
        self.sendMessage(message, self.__messageChannel)

    def arm(self, event):
        message = Message(MessageType.ACTION, Action.ARM)
        self.sendMessage(message, self.__messageChannel)

    def increaseSpeed(self, event):
        message = Message(MessageType.ACTION, Action.SPEED_INCREASE)
        self.sendMessage(message, self.__messageChannel)

    def decreaseSpeed(self, event):
        message = Message(MessageType.ACTION, Action.SPEED_DECREASE)
        self.sendMessage(message, self.__messageChannel)

    def sendMessage(self, message:Message, messageChannel:MessageChannel) -> None:
        messageChannel.broadcast(message)

    def toggleLight(self, event):
        print("Toggle light")
        message = Message(MessageType.ACTION, Action.TOGGLE_LIGHTS)
        self.sendMessage(message, self.__messageChannel)

    def increaseBrightness(self, event):
        message = Message(MessageType.ACTION, Action.BRIGHTNESS_INCREASE)
        self.sendMessage(message, self.__messageChannel)

    def decreaseBrightness(self, event):
        message = Message(MessageType.ACTION, Action.BRIGHTNESS_DECREASE)
        self.sendMessage(message, self.__messageChannel)

    #Creates the action message and sends it over the message channel
    def sendMessage(self, message:Message, messageChannel:MessageChannel):
        #Check if duplicate

        messageChannel.broadcast(message)
