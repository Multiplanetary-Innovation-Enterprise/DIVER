import pygame

from ROVMessaging.MessageChannel import MessageChannel

from inputs.Input import Input

#Represents an implmentation of an input using a xbox one controller
class ControllerInput(Input):
    #Registers both joysticks moving and provides the message channel to
    #send the input change messages in
    def __init__(self, messageChannel:MessageChannel):
        super().__init__(messageChannel)

    pygame.init()

    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates.
    clock = pygame.time.Clock()

    # Initialize the joysticks.
    pygame.joystick.init()

    while not done:
        for event in pygame.event.get(): # User did something.
            if event.type == pygame.QUIT: # If user clicked close.
                done = True # Flag that we are done so we exit this loop.

       if pygame.joystick.get_count() == 0:
            done = True
        else:
            #Setup joysticks
            joystick = pygame.joystick.Joystick(0)
            joystick.init()

            #kills program if you hit the 'A' button
            if joystick.get_button(0) == 1:
                done = True

            
            #Setup joysticks
            joystick = pygame.joystick.Joystick(0)
            joystick.init()
        
            #bottom right joystick controls forward and backward
            if joystick.get_axis(3) > .5:
                self.backward;
                self.stopXY;

            if joystick.get_axis(3) < -.5:
                self.forward;
                self.stopXY;

            #The upper left joystick controls the Z-axis
            if joystick.get_axis(1) > .5:
                self.down;
                self.stopZ;

            if joystick.get_axis(1) < -.5:
                self.up;
                self.stopZ;

            #either joystick can move the vechile left and right
            if joystick.get_axis(0) > .5:
                self.right;
                self.stopXY;

            if joystick.get_axis(0) < -.5:
                self.left;
                self.stopXY;

            if joystick.get_axis(2) > .5:
                 self.right;
                self.stopXY;

            if joystick.get_axis(2) < -.5:
                self.left;
                self.stopXY;

           #controls how fast the controller gives input
           clock.tick(5);
        
    # Close the window and quit.
    pygame.quit()

