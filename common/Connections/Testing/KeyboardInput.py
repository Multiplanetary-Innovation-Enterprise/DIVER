from pynput import keyboard
from ROVMessaging.Publisher import *
from ROVMessaging.Message import *
from ROVMessaging.MessageChannel import *
from ROVMessaging.MessageType import *
from ROVMessaging.Action import *
import time
import queue
import threading

class KeyboardInput(Publisher):
    __messageChannel = None
    __stop = None
    __queue = None
    __isRunning = False
    __keyReleased = True
    # lastMessage = None
    def __init__(self, messageChannel:MessageChannel):
        self.__messageChannel = messageChannel

        #start keyboard listener
        listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        listener.start()  # start to listen on a separate thread
        self.__stop = False

        # keyboard.on_release_key('l', self.toggleLight, True)
        #
        # keyboard.on_press_key(']', self.increaseBrightness, True)
        # keyboard.on_press_key('[', self.decreaseBrightness, True)
        self.__queue = queue.Queue()
        thread = threading.Thread(target=self.processMessages)
        thread.start()

    def on_press(self, key):
        # if key == keyboard.Key.esc:
        #     return False  # stop listener
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys
        print(f"press: {k}")
        if (self.__keyReleased):
            if (k == 'space'):
                self.arm()
            elif (k == 'w'):
                self.forward()
            elif (k == 'a'):
                self.backward()
            elif (k == 's'):
                self.left()
            elif (k == 'd'):
                self.right()
            elif (k == 'up'):
                self.up()
            elif (k == 'down'):
                self.down()
            elif (k == 'left'):
                self.increaseSpeed()
            elif (k == 'right'):
                self.decreaseSpeed()
            self.__keyReleased = False

    def on_release(self, key):
        # if key == keyboard.Key.esc:
        #     return False  # stop listener
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys
        print(f"release: {k}")
        if (k == 'w'):
            self.stopXY()
        elif (k == 'a'):
            self.stopXY()
        elif (k == 's'):
            self.stopXY()
        elif (k == 'd'):
            self.stopXY()
        elif (k == 'up'):
            self.stopZ()
        elif (k == 'down'):
            self.stopZ()
        elif (k == 'esc'):
            self.__stop = True
        self.__keyReleased = True

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

    def isRunning(self) -> bool:
        return self.__isRunning

    def enqueue(self, message) -> None:
        self.__queue.put(message)

    def dequeue(self):
        return self.__queue.get()

    def processMessages(self) -> None:
        # self.__isRunning = True
        # lastMessage = None
        while True:
            if not self.__queue.empty():
                message = self.dequeue()
                print(f"sending message: {message.getContents()}")
                self.__messageChannel.broadcast(message)
                time.sleep(0.5)

        # self.__isRunning = False

    def sendMessage(self, message:Message, messageChannel:MessageChannel) -> None:
        #Checks if the current command is the same as the last command
        # if not self.__isRunning:
        self.enqueue(message)
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
