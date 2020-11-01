from typing import List

from ObserverPattern import Observer, Observable
from Command import Command
from MoveCommands  import MoveX
from SpeedCommands import IncreaseSpeed, DecreaseSpeed

#Represents a generic input device
class Input(Observable):
    lastCommand = None

    #Increases the speed of the chasis by sending an increase speed command
    def increaseSpeed(self, event):
        self.notify(IncreaseSpeed())

    #Decreases the speed of the chasis by sending a decrease speed command
    def decreaseSpeed(self, event):
        self.notify(DecreaseSpeed())

    #Sends a move forward command
    def forward(self, event):
        self.notify(MoveX(1))
        #print("forward\n")

    #Sends a move backwards command
    def backward(self, event):
        self.notify(MoveX(-1))
        #print("backward\n")

    #Sends a stop moving in x-axis command
    def stopX(self, event):
        self.notify(MoveX(0))
        #print("Stop X\n")

    #Sends a move right command
    def right(self, event):pass

    #Sends a move left command
    def left(self, event):pass

    #Sends a stop moving in y-axis command
    def stopY(self, event):pass

    #Sends a move up command
    def up(self, event):pass

    #Sends a move down command
    def down(self, event):pass

    #Sends a stop moving in z-axis command
    def stopZ(self, event):pass

    #Sends a command to all observers
    def notify(self, command: Command):
        print("Same class: " + str(type(command) is type(self.lastCommand)) + "\n");


        if self.lastCommand is not None:
             print("Same values: " + str(command == self.lastCommand) + "\n");

        if type(command) is type(self.lastCommand):
            print("Same same \n")

        #Checks if the command is not the same as the last command. Checks if the commands contain the same attributes and then
        #checks if the command and last command are of the same class
        if not ((self.lastCommand is not None and command == self.lastCommand) and (type(command) is type(self.lastCommand))):
            for observer in self.observers:
                observer.update(command)

        #
        # print("command: " + str(type(command)) + "\n");
        # print("last: " + str(type(self.lastCommand)) + "\n");
        #
        # for observer in self.observers:
        #     observer.update(command)

        self.lastCommand = command
