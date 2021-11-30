import queue
import threading

from ROVMessaging.Subscriber import Subscriber
from ROVMessaging.Message import Message
from ROVMessaging.MessageType import MessageType

from commands.Command import Command
from commands.CommandFactory import CommandFactory

class CommandProcessor(Subscriber):
    __isRunning = False
    __queue = None
    __commandFactory = None
    lastCommand = None

    def __init__(self, commandFactory:CommandFactory):
        self.__queue = queue.Queue()
        self.__commandFactory = commandFactory

    def isRunning(self) -> bool:
        return self.__isRunning

    def enqueueCommand(self, command:Command) -> None:
        self.__queue.put(command)

    def dequeueCommand(self) -> Command:
        return self.__queue.get()

    def processCommands(self) -> None:
        self.__isRunning = True

        while not self.__queue.empty():
            command = self.dequeueCommand()
            command.execute()

        self.__isRunning = False

    def recieveMessage(self, message:Message) -> None:
        #Ignore messages that are not actions
        if not message.getType() == MessageType.ACTION:
            return

        action = message.getContents()
        command = self.__commandFactory.createCommand(action)

        #Checks if the current command is the same as the last command
        if (self.lastCommand is None or (self.lastCommand is not None and command != self.lastCommand)) or command.isRepeatable():
            if not self.__isRunning:
                self.enqueueCommand(command)
                thread = threading.Thread(target=self.processCommands)
                thread.start()

        self.lastCommand = command
