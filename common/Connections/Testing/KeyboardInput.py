import keyboard
from ROVMessaging.Publisher import *
from ROVMessaging.Message import *
from ROVMessaging.MessageChannel import *
from ROVMessaging.MessageType import *

class KeyboardInput(Publisher):
    __messageChannel = None
    __stop = None
    def __init__(self, messageChannel:MessageChannel):
        self.__messageChannel = messageChannel

        #start keyboard listener
        listener = keyboard.Listener(on_press=on_press)
        listener.start()  # start to listen on a separate thread
        self.__stop = False

        # keyboard.on_release_key('l', self.toggleLight, True)
        #
        # keyboard.on_press_key(']', self.increaseBrightness, True)
        # keyboard.on_press_key('[', self.decreaseBrightness, True)

    def on_press(key):
        # if key == keyboard.Key.esc:
        #     return False  # stop listener
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys
        if (key == 'space'):
            self.arm()
        elif (key == 'w'):
            self.forward()
        elif (key == 'a'):
            self.backward()
        elif (key == 's'):
            self.left()
        elif (key == 'd'):
            self.right()
        elif (key == 'up'):
            self.up()
        elif (key == 'down'):
            self.down()
        elif (key == 'left'):
            self.increaseSpeed()
        elif (key == 'right'):
            self.decreaseSpeed()

    def on_release(key):
        # if key == keyboard.Key.esc:
        #     return False  # stop listener
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys
        if (key == 'w'):
            self.stopXY()
        elif (key == 'a'):
            self.stopXY()
        elif (key == 's'):
            self.stopXY()
        elif (key == 'd'):
            self.stopXY()
        elif (key == 'up'):
            self.stopZ()
        elif (key == 'down'):
            self.stopZ()
        elif (key == 'esc'):
            self.__stop = True

    def acceptingInput(self):
        if (self.__stop):
            return False
        else:
            return True

    #Sends move forward action
    def forward(self):
        message = Message(MessageType.ACTION, Action.MOVE_XY_FORWARD)
        self.sendMessage(message, self.__messageChannel)

    #Send move backward action
    def backward(self):
        message = Message(MessageType.ACTION, Action.MOVE_XY_BACKWARD)
        self.sendMessage(message, self.__messageChannel)

    def stopXY(self):
        message = Message(MessageType.ACTION, Action.MOVE_XY_STOP)
        self.sendMessage(message, self.__messageChannel)

    #Send move up action
    def up(self):
        message = Message(MessageType.ACTION, Action.MOVE_Z_POS)
        self.sendMessage(message, self.__messageChannel)

    #Send move down action
    def down(self):
        message = Message(MessageType.ACTION, Action.MOVE_Z_NEG)
        self.sendMessage(message, self.__messageChannel)

    def stopZ(self):
        message = Message(MessageType.ACTION, Action.MOVE_Z_STOP)
        self.sendMessage(message, self.__messageChannel)

    #Sends a move right command
    def right(self):
        message = Message(MessageType.ACTION, Action.MOVE_XY_LEFT)
        self.sendMessage(message, self.__messageChannel)

    #Sends a move left command
    def left(self):
        message = Message(MessageType.ACTION, Action.MOVE_XY_RIGHT)
        self.sendMessage(message, self.__messageChannel)

    def arm(self):
        message = Message(MessageType.ACTION, Action.ARM)
        self.sendMessage(message, self.__messageChannel)

    def increaseSpeed(self):
        message = Message(MessageType.ACTION, Action.SPEED_INCREASE)
        self.sendMessage(message, self.__messageChannel)

    def decreaseSpeed(self):
        message = Message(MessageType.ACTION, Action.SPEED_DECREASE)
        self.sendMessage(message, self.__messageChannel)

    def sendMessage(self, message:Message, messageChannel:MessageChannel) -> None:
        messageChannel.broadcast(message)
    #
    # def toggleLight(self, event):
    #     print("Toggle light")
    #     message = Message(MessageType.ACTION, Action.TOGGLE_LIGHTS)
    #     self.sendMessage(message, self.__messageChannel)
    #
    # def increaseBrightness(self, event):
    #     message = Message(MessageType.ACTION, Action.BRIGHTNESS_INCREASE)
    #     self.sendMessage(message, self.__messageChannel)
    #
    # def decreaseBrightness(self, event):
    #     message = Message(MessageType.ACTION, Action.BRIGHTNESS_DECREASE)
    #     self.sendMessage(message, self.__messageChannel)
