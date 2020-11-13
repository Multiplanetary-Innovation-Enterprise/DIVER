import keyboard

from Input import Input

#Represents a keyboard input
class KeyboardInput(Input):
    def __init__(self):
        #X axis
        #Move forward controls
        keyboard.on_press_key('w', self.forward, True)
        keyboard.on_release_key('w', self.stopX, True)

        #Move backwards controls
        keyboard.on_press_key('s', self.backward, True)
        keyboard.on_release_key('s', self.stopX, True)

        #Y axis
	    #Move forward controls
        keyboard.on_press_key('a', self.left, True)
        keyboard.on_release_key('a', self.stopY, True)

        #Move backwards controls
        keyboard.on_press_key('d', self.right, True)
        keyboard.on_release_key('d', self.stopY, True)


        #Speed controls
        keyboard.on_press_key('up', self.increaseSpeed, True)
        keyboard.on_press_key('down', self.decreaseSpeed, True)
