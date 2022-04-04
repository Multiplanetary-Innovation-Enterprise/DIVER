import pygame
import threading

from ROVMessaging.MessageChannel import MessageChannel

from inputs.Input import Input

#Represents an implmentation of an input using a xbox one controller
class ControllerInput(Input):
    __isRunning:bool = False #Whether or not the the controller listener is running
    __thread = None          #The thread that the listener is running on

    #Registers both joysticks moving and provides the message channel to
    #send the input change messages in
    def __init__(self, messageChannel:MessageChannel):
        super().__init__(messageChannel)

        pygame.init()

    def listen(self) -> None:
        if not self.__isRunning:
            self.__thread = threading.Thread(target=self.__run)
            self.__thread.start()

    def __run(self):
        self.__isRunning = True

        # Used to manage how fast the screen updates.
        clock = pygame.time.Clock()

        # Initialize the joysticks.
        pygame.joystick.init()

        while self.__isRunning:
            for event in pygame.event.get(): # User did something.
                if event.type == pygame.QUIT: # If user clicked close.
                    self.__isRunning = False # Flag that we are done so we exit this loop.

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

                print("controller loop")

                print("Joy: " + str(joystick.get_axis(3)))

                #bottom right joystick controls forward and backward
                if joystick.get_axis(3) > .5:
                    self.backward(None);
                elif joystick.get_axis(3) < -.5:
                    print("Forward-------------------------------------------")
                    self.forward(None);

                #The upper left joystick controls the Z-axis
                if joystick.get_axis(1) > .5:
                    self.down(None);
                elif joystick.get_axis(1) < -.5:
                    self.up(None);
                else:
                    self.stopZ(None);

                # #either joystick can move the vechile left and right
                # if joystick.get_axis(0) > .5:
                #     print("right-------------------------------")
                #     self.right(None);
                # elif joystick.get_axis(0) < -.5:
                #     print("LEFT -----------------------------")
                #     self.left(None);
                # else:
                #     self.stopXY(None);

                if joystick.get_axis(2) > .5:
                    self.right(None);
                elif joystick.get_axis(2) < -.5:
                    self.left(None);

                if not ((joystick.get_axis(3) > .5 or joystick.get_axis(3) < -.5) or (joystick.get_axis(2) > .5 or joystick.get_axis(2) < -.5)):
                    self.stopXY(None);



            #controls how fast the controller gives input
            clock.tick(5);

        print("pyame stop")

        # Close the window and quit.
       # pygame.quit()

        print("pygame stopped")

    def stop(self) -> None:
        self.__isRunning = False
