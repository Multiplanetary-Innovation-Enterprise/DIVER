import keyboard

from ROVMessaging.MessageChannel import MessageChannel

from inputs.Input import Input

#Represents an implementation of a generic input device using a keyboard
class KeyboardInput(Input):
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

        keyboard.on_press_key('left', self.ccw, True)
        keyboard.on_release_key('left', self.stopXY, True)
        
        keyboard.on_press_key('right', self.cw, True)
        keyboard.on_release_key('right', self.stopXY, True)

        keyboard.on_press_key('up', self.up, True)
        keyboard.on_release_key('up', self.stopZ, True)

        keyboard.on_press_key('down', self.down, True)
        keyboard.on_release_key('down', self.stopZ, True)

        keyboard.on_press_key('.', self.increaseSpeed, True)
        keyboard.on_press_key(',', self.decreaseSpeed, True)

        keyboard.on_release_key('l', self.toggleLight, True)

        keyboard.on_press_key(']', self.increaseBrightness, True)
        keyboard.on_press_key('[', self.decreaseBrightness, True)

        keyboard.on_press_key('c', self.captureImage, True)

        keyboard.on_press_key('E', self.Estop, True)
