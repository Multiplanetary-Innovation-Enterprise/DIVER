from ROVMessaging.MessageChannel import MessageChannel
from ROVMessaging.MessageType import MessageType
from ROVMessaging.Message import Message
from ROVMessaging.Action import Action

from commands.CommandProcessor import CommandProcessor
from commands.CommandFactory import CommandFactory

from ROV import ROV

messageChannel = MessageChannel()

rov = ROV()

commandFactory = CommandFactory(rov, messageChannel)

commandProcessor = CommandProcessor(commandFactory)

messageChannel.subscribe(MessageType.ACTION, commandProcessor)

messageChannel.broadcast(Message(MessageType.ACTION, Action.MOVE_X_POS))
