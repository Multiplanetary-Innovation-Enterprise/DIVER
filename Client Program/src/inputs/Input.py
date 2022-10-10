from abc import ABC

from ROVMessaging.Publisher import Publisher
from ROVMessaging.Message import Message
from ROVMessaging.MessageChannel import MessageChannel
from ROVMessaging.MessageType import MessageType

from inputs.Action import Action

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

    #Sends the arm thrusters action message
    def arm(self, event) -> None:
        message = Message(MessageType.ACTION, Action.ARM.value)
        self.sendMessage(message, self.__messageChannel)

    #Sends the move forward action message
    def forward(self, event) -> None:
        message = Message(MessageType.ACTION, Action.MOVE_XY_FORWARD.value)
        self.sendMessage(message, self.__messageChannel)

    #Sends the move backward action message
    def backward(self, event) -> None:
        message = Message(MessageType.ACTION, Action.MOVE_XY_BACKWARD.value)
        self.sendMessage(message, self.__messageChannel)

    #Sends the move right action message
    def right(self, event) -> None:
        message = Message(MessageType.ACTION, Action.TURN_XY_RIGHT.value)
        self.sendMessage(message, self.__messageChannel)

    #Sends the move left action message
    def left(self, event) -> None:
        message = Message(MessageType.ACTION, Action.TURN_XY_LEFT.value)
        self.sendMessage(message, self.__messageChannel)

    #Sends the stop XY action message
    def stopXY(self, event) -> None:
        message = Message(MessageType.ACTION, Action.MOVE_XY_STOP.value)
        self.sendMessage(message, self.__messageChannel)

    #Sends the move up action message
    def up(self, event) -> None:
        message = Message(MessageType.ACTION, Action.MOVE_Z_UP.value)
        self.sendMessage(message, self.__messageChannel)

    #Sends the move down action message
    def down(self, event) -> None:
        message = Message(MessageType.ACTION, Action.MOVE_Z_DOWN.value)
        self.sendMessage(message, self.__messageChannel)

    #Sends the stop vertical movement action message
    def stopZ(self, event) -> None:
        message = Message(MessageType.ACTION, Action.MOVE_Z_STOP.value)
        self.sendMessage(message, self.__messageChannel)

    #Sends the increase speed action message
    def increaseSpeed(self, event) -> None:
        message = Message(MessageType.ACTION, Action.SPEED_INCREASE.value)
        self.sendMessage(message, self.__messageChannel)

    #Sends the decrease speed action message
    def decreaseSpeed(self, event) -> None:
        message = Message(MessageType.ACTION, Action.SPEED_DECREASE.value)
        self.sendMessage(message, self.__messageChannel)

    #Sends the toggle lights action message
    def toggleLight(self, event) -> None:
        message = Message(MessageType.ACTION, Action.TOGGLE_LIGHTS.value)
        self.sendMessage(message, self.__messageChannel)

    #Sends the increase lights brightness action message
    def increaseBrightness(self, event) -> None:
        message = Message(MessageType.ACTION, Action.BRIGHTNESS_INCREASE.value)
        self.sendMessage(message, self.__messageChannel)

    #Sends the decrease lights brightness action message
    def decreaseBrightness(self, event) -> None:
        message = Message(MessageType.ACTION, Action.BRIGHTNESS_DECREASE.value)
        self.sendMessage(message, self.__messageChannel)

    #Sends the capture image action message
    def captureImage(self, event) -> None:
        message = Message(MessageType.ACTION, Action.CAPTURE_IMAGE.value)
        self.sendMessage(message, self.__messageChannel)
