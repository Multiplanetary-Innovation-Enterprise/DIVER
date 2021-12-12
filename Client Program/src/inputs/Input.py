from abc import ABC

from ROVMessaging.Publisher import Publisher
from ROVMessaging.Message import Message
from ROVMessaging.MessageChannel import MessageChannel
from ROVMessaging.MessageType import MessageType
from ROVMessaging.Action import Action

#Represents the base for all input devices
class Input(Publisher, ABC):
    #The message channel to send input update messages on
    __messageChannel:MessageChannel = None

    def __init__(self, messageChannel:MessageChannel):
        super(Publisher, self).__init__()
        self.__messageChannel = messageChannel

    #Creates the action message and sends it over the message channel
    def sendMessage(self, message:Message, messageChannel:MessageChannel) -> None:
        messageChannel.broadcast(message)

    #Sends the move forward action message
    def forward(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_XY_FORWARD)
        self.sendMessage(message, self.__messageChannel)

    #Sends the move backward action message
    def backward(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_XY_BACKWARD)
        self.sendMessage(message, self.__messageChannel)

    #Sends the move right action message
    def right(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_XY_LEFT)
        self.sendMessage(message, self.__messageChannel)

    #Sends the move left action message
    def left(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_XY_RIGHT)
        self.sendMessage(message, self.__messageChannel)

    #Sends the stop XY action message
    def stopXY(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_XY_STOP)
        self.sendMessage(message, self.__messageChannel)

    #Sends the move up action message
    def up(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_Z_POS)
        self.sendMessage(message, self.__messageChannel)

    #Sends the move down action message
    def down(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_Z_NEG)
        self.sendMessage(message, self.__messageChannel)

    #Sends the stop vertical movement action message
    def stopZ(self, event):
        message = Message(MessageType.ACTION, Action.MOVE_Z_STOP)
        self.sendMessage(message, self.__messageChannel)

    #Sends the arm thrusters action message
    def arm(self, event):
        message = Message(MessageType.ACTION, Action.ARM)
        self.sendMessage(message, self.__messageChannel)

    #Sends the increase speed action message
    def increaseSpeed(self, event):
        message = Message(MessageType.ACTION, Action.SPEED_INCREASE)
        self.sendMessage(message, self.__messageChannel)

    #Sends the decrease speed action message
    def decreaseSpeed(self, event):
        message = Message(MessageType.ACTION, Action.SPEED_DECREASE)
        self.sendMessage(message, self.__messageChannel)

    #Sends the toggle lights action message
    def toggleLight(self, event):
        message = Message(MessageType.ACTION, Action.TOGGLE_LIGHTS)
        self.sendMessage(message, self.__messageChannel)

    #Sends the increase lights brightness action message
    def increaseBrightness(self, event):
        message = Message(MessageType.ACTION, Action.BRIGHTNESS_INCREASE)
        self.sendMessage(message, self.__messageChannel)

    #Sends the decrease lights brightness action message
    def decreaseBrightness(self, event):
        message = Message(MessageType.ACTION, Action.BRIGHTNESS_DECREASE)
        self.sendMessage(message, self.__messageChannel)
