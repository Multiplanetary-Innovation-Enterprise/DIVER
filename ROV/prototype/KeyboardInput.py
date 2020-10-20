import keyboard

from Input import Input

class KeyboardInput(Input):
    def __init__(self):
        #Move forward controls
        keyboard.on_press_key('w', self.forward, True)
        keyboard.on_release_key('w', self.stopX, True)

        #Move backwards controls
        keyboard.on_press_key('s', self.backward, True)
        keyboard.on_release_key('s', self.stopX, True)

        #Speed controls
        keyboard.on_press_key('up', self.increaseSpeed, True)
        keyboard.on_press_key('down', self.decreaseSpeed, True)
