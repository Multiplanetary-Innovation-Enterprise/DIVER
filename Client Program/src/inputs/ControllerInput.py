import pygame
import pygame._sdl2.controller

import threading

from ROVMessaging.MessageChannel import MessageChannel

from inputs.Input import Input

#Represents an implementation of an input using a game controller
#Confirmed to work with xbox and Nintendo Pro Controller
class ControllerInput(Input):
    __isRunning:bool = False #Whether or not the the controller listener is running
    __thread = None          #The thread that processes the controller input

    MAX_JOYSTICK = 32767    # Maximum value of a pygame controller stick
    MIN_JOYSTICK = -32768   # Minimum value of a pygame controller stick (NOTE: Min value of triggers is 0)

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

        # Initialize the controller
        pygame._sdl2.controller.init()

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
                print("[ControllerInput.py] Controller NOT FOUND")
                self.__isRunning = False
            else:
                #Setup controller
                controller = pygame._sdl2.controller.Controller(0)
                controller.init()

                #kills program if you hit the 'A' button (CURRENTLY DISABLED)
                #if controller.get_button(pygame.CONTROLLER_BUTTON_A):
                    #self.__isRunning = False

                #Setup joysticks (CURRENTLY DISABLED IN FAVOR OF CONTROLLER)
                #controller = pygame.controller.Joystick(0)
                #controller.init()

                #DEBUG: Prints controller joystick values
                #print(controller.get_axis(pygame.CONTROLLER_AXIS_LEFTY))

                #DPAD_UP increases thrust
                if controller.get_button(pygame.CONTROLLER_BUTTON_DPAD_UP):
                    self.increaseSpeed(None)
                #DPAD_DOWN decreases thrust
                if controller.get_button(pygame.CONTROLLER_BUTTON_DPAD_DOWN):
                    self.decreaseSpeed(None)
    
                elif controller.get_axis(pygame.CONTROLLER_AXIS_RIGHTX) > self.MAX_JOYSTICK * .5:
                    self.cw(None)
                    #isMoveXY = True
                elif controller.get_axis(pygame.CONTROLLER_AXIS_RIGHTX) < self.MIN_JOYSTICK * .5:
                    self.ccw(None)
                    #isMoveXY = True
                #The upper left joystick controls for XY-axis
                elif controller.get_axis(pygame.CONTROLLER_AXIS_LEFTX) > self.MAX_JOYSTICK * .5:
                    self.right(None)
                    #isMoveXY = True
                elif controller.get_axis(pygame.CONTROLLER_AXIS_LEFTX) < self.MIN_JOYSTICK * .5:
                    self.left(None)
                    #isMoveXY = True
                elif controller.get_axis(pygame.CONTROLLER_AXIS_LEFTY) > self.MAX_JOYSTICK * .5:
                    self.backward(None)
                    #isMoveXY = True
                elif controller.get_axis(pygame.CONTROLLER_AXIS_LEFTY) < self.MIN_JOYSTICK * .5:
                    self.forward(None)
                    #isMoveXY = True
                else:
                    self.stopXY(None)
                    #isMoveXY = False

                #Checks if a movement in the XY axis message has been sent, if so,
                #the ROV is no longer stopped in that direction
                #if isMoveXY:
                #    isStoppedXY = False

                #Sends the stop XY plane movement message if no movement command has been sent
                #and if the stop XY message has not been sent yet
                #if not isMoveXY and not isStoppedXY:
                    #The stop XY message was sent
                #    isStoppedXY = True
                #    self.stopXY(None)

                #Bottom right joystick controls attitude
                if controller.get_axis(pygame.CONTROLLER_AXIS_RIGHTY) > self.MAX_JOYSTICK * .5:
                    self.pitchUp(None)
                    isMoveZ = True
                elif controller.get_axis(pygame.CONTROLLER_AXIS_RIGHTY) < self.MIN_JOYSTICK * .5:
                    self.pitchDown(None)
                    isMoveZ = True
                else:
                    isMoveZ = False

                #The bumpers control surface and dive
                if controller.get_button(pygame.CONTROLLER_BUTTON_LEFTSHOULDER):
                    self.down(None)
                    isMoveZ = True
                elif controller.get_button(pygame.CONTROLLER_BUTTON_RIGHTSHOULDER):
                    self.up(None)
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

                    self.stopZ(None)


                #Illumination Controls

                #DPAD_RIGHT Increases brightness
                if controller.get_button(pygame.CONTROLLER_BUTTON_DPAD_RIGHT):
                    self.increaseBrightness(None)
                #DPAD_LEFT decreases brightness
                if controller.get_button(pygame.CONTROLLER_BUTTON_DPAD_LEFT):
                    self.decreaseBrightness(None)
                #'A' Button toggles light
                if controller.get_button(pygame.CONTROLLER_BUTTON_A):
                    self.toggleLight(None)

            #controls how fast the controller gives input
            clock.tick(5)

        # Close the window and quit.
       # pygame.quit()

    #Stops the controller input processor
    def stop(self) -> None:
        self.__isRunning = False
