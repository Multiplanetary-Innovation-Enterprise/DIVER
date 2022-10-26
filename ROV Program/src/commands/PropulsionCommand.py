from abc import ABC

from commands.Command import Command
from subsystems.PropulsionSubsystem import PropulsionSubsystem

#Represents a generic command that uses the propulsion subsystem
class PropulsionCommand(Command, ABC):
    _propSystem:PropulsionSubsystem = None #The ROV's propulsion system

    def __init__(self, propSystem:PropulsionSubsystem):
        self._propSystem = propSystem
