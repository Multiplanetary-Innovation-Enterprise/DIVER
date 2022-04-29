from abc import ABC

from commands.Command import Command
from subsystems.PropulsionSubsystem import PropulsionSubsystem

#Represents a generic command that uses the propulsion subsystem
class PropulsionCommand(Command, ABC):
    __propSystem:PropulsionSubsystem = None #The ROV's illumination system

    def __init__(self, propSystem:PropulsionSubsystem):
        self.__propSystem = propSystem
