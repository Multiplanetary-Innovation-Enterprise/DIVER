import time
import queue
import threading
import keyboard

from ROVMessaging.MessageChannel import MessageChannel

from input.Input import Input

#Represents an implmentation of an input using a keyboard
class KeyboardInput(Input):
    __messageChannel:MessageChannel = None

    #Registers all of the key bindings and provides the message channel to
    #send the input change messages in
    def __init__(self, messageChannel:MessageChannel):
        super().__init__(messageChannel)

        keyboard.on_press_key('space', self.arm, True)

        keyboard.on_press_key('w', self.forward, True)
        keyboard.on_release_key('w', self.stopXY, True)

        keyboard.on_press_key('s', self.backward, True)
        keyboard.on_release_key('s', self.stopXY, True)

        keyboard.on_press_key('a', self.left, True)
        keyboard.on_release_key('a', self.stopXY, True)

        keyboard.on_press_key('d', self.right, True)
        keyboard.on_release_key('d', self.stopXY, True)

        keyboard.on_press_key('up', self.up, True)
        keyboard.on_release_key('up', self.stopZ, True)

        keyboard.on_press_key('down', self.down, True)
        keyboard.on_release_key('down', self.stopZ, True)

        keyboard.on_press_key('right', self.increaseSpeed, True)
        keyboard.on_press_key('left', self.decreaseSpeed, True)

        keyboard.on_release_key('l', self.toggleLight, True)

        keyboard.on_press_key(']', self.increaseBrightness, True)
        keyboard.on_press_key('[', self.decreaseBrightness, True)
