import pygame
import threading
from ROVMessaging.MessageChannel import MessageChannel

from inputs.Input import Input

#Represents an implementation of an input using a game controller
#Confirmed to work with xbox and Nintendo Pro Controller
class ControllerInput(Input):
    __isRunning:bool = False #Whether or not the the controller listener is running
    __thread = None          #The thread that processes the controller input

    #Registers both joysticks moving and provides the message channel to
    #send the input change messages in
    def __init__(self, messageChannel:MessageChannel):
        super().__init__(messageChannel)

        pygame.init()

    #Starts the controller input listener thread if it is not already running
    def listen(self) -> None:
        if not self.__isRunning:
            self.__thread = threading.Thread(target=self.__run)
            self.__thread.start()

    #Continuously processes the controller input
    def __run(self) -> None:
        self.__isRunning = True

        # Used to manage how fast the screen updates.
        clock = pygame.time.Clock()

        # Initialize the joysticks.
        pygame.joystick.init()

        isMoveXY:bool = False   #Whether or not there is movement in the XY plane
        isMoveZ:bool = False    #Whether or not there is movement in Z axis
        isStoppedXY:bool = True #Whether or not the stop XY message was sent
        isStoppedZ:bool = True  #Whether or not the stop Z message was sent

        #Continuously processes the controller input until stopped
        while self.__isRunning:
            for event in pygame.event.get(): # User did something.
                if event.type == pygame.QUIT: # If user clicked close.
                    self.__isRunning = False # Flag that we are done so we exit this loop.

            #Checks if the controller was found
            if pygame.joystick.get_count() == 0:
                self.__isRunning = False
            else:
                #Setup joysticks
                joystick = pygame.joystick.Joystick(0)
                joystick.init()

                #kills program if you hit the 'A' button
                if joystick.get_button(0) == 1:
                    self.__isRunning = False

                #Setup joysticks
                joystick = pygame.joystick.Joystick(0)
                joystick.init()

                #top left joystick controls for forward, backward, left, and right translation
                if joystick.get_axis(1) > .5:
                    self.backward(None)
                    isMoveXY = True
                elif joystick.get_axis(1) < -.5:
                    self.forward(None)
                    isMoveXY = True

                if joystick.get_axis(0) > .5:
                    self.right(None);
                    isMoveXY = True
                elif joystick.get_axis(0) < -.5:
                    self.left(None);
                    isMoveXY = True

                #bottom right joystick controls for rotation
                if joystick.get_axis(3) > 0.5:
                    self.cw(None)
                    isMoveXY = True

                elif joystick.get_axis(3) < -0.5:
                    self.ccw(None)
                    isMoveXY = True
                
                
                if joystick.get_axis(0) < 0.5 and joystick.get_axis(0) > -0.5 and joystick.get_axis(1) < 0.5 and joystick.get_axis(1) > -0.5:
                    leftStickMove = False
                else:
                    leftStickMove = True

                if joystick.get_axis(3) < 0.5 and joystick.get_axis(3) > -0.5 and joystick.get_axis(4) < 0.5 and joystick.get_axis(4) > -0.5:
                    rightStickMove = False
                else:
                    rightStickMove = True

                

                #Checks if a movement is the XY plane messgae has been  sent, if so,
                #the ROV is no longer stopped
                if isMoveXY:
                    isStoppedXY = False

                #Sends the stop XY plane movement message if no movement command has been sent
                #and if the stop XY message has not been sent yet
                if not isMoveXY and not isStoppedXY:
                    #The stop XY message was sent
                    isStoppedXY = True
                    self.stopXY(None);

                #The right bumper controls for the Z-axis (right(down) takes priority)
                if joystick.get_button(5) > .5:
                    self.up(None);
                    isMoveZ = True
                elif joystick.get_button(4) > .5:
                    self.down(None);
                    isMoveZ = True
                else:
                    isMoveZ = False


                #Checks if a movement in the Z axis message has been sent, if so,
                #the ROV is no longer stopped in that direction
                if isMoveZ:
                    isStoppedZ = False

                #Sends the stop Z movement message if no Z axis movement command has been sent
                #and if the stop Z message has not been sent yet
                if not isMoveZ and not isStoppedZ:
                    #The stop XY message was sent
                    isStoppedZ = True

                    self.stopZ(None);

            #controls how fast the controller gives input
            clock.tick(5);

        # Close the window and quit.
       # pygame.quit()

    #Stops the controller input processor
    def stop(self) -> None:
        self.__isRunning = False
        pygame.joystick.quit()
        pygame.quit()
