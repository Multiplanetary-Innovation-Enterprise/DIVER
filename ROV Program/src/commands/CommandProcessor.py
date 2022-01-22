import queue
import threading

from ROVMessaging.Subscriber import Subscriber
from ROVMessaging.Message import Message
from ROVMessaging.MessageType import MessageType

from commands.Command import Command
from commands.CommandFactory import CommandFactory

#Processes all commands that it receives from the message channel that it listens to
class CommandProcessor(Subscriber):
    __isRunning:bool = False               #Whether or not the processor is currently running
    __isShutdown:bool = False              #Whether or not it is time for shutdown
    __queue = None                         #Stores the received commands that have not beenn processed yet
    __commandFactory:CommandFactory = None #Creates commands from an acion code
    __lastCommand:Command = None           #The last command that was executed

    def __init__(self, commandFactory:CommandFactory):
        self.__queue = queue.Queue()
        self.__commandFactory = commandFactory

    #Adds a command to the its processing queue
    def enqueueCommand(self, command:Command) -> None:
        self.__queue.put(command)

    #Removes the next command in its processing queue
    def dequeueCommand(self) -> Command:
        return self.__queue.get()

    #Process all the commands until the command queue is empty
    def __processCommands(self) -> None:
        self.__isRunning = True

        #Continues executing instructions until the queue is empty
        while not self.__queue.empty() and not self.__isShutdown:
            command = self.dequeueCommand()
            command.execute()

        self.__isRunning = False

    #Whether or not commands are currently being processed
    def isRunning(self) -> bool:
        return self.__isRunning

    #Stops processing commands
    def stop(self) -> None:
        self.__isShutdown = True

    #Listens for action messages, so that they can be converted to commands and processed
    def recieveMessage(self, message:Message) -> None:
        #Ignore messages that are not actions
        if not message.getType() == MessageType.ACTION:
            return

        #Converts the recieved action to command
        action = message.getContents()
        command = self.__commandFactory.createCommand(action)

        #If the command was invalid, so ignore it
        if command is None:
            return

        #Checks if the current command is the same as the last command
        if self.__lastCommand is None or command != self.__lastCommand or command.isRepeatable():
            self.enqueueCommand(command)
            self.__lastCommand = command

            #If the processor has stopped, start it up again
            if not self.__isRunning:
                thread = threading.Thread(target=self.__processCommands)
                thread.start()
