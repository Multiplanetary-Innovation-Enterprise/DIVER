from subsystems.PropulsionSubsystem import PropulsionSubsystem

class ROV:
    __propSystem = None

    def __init__(self):
        self.__propSystem = PropulsionSubsystem()

    def getPropSystem(self) -> PropulsionSubsystem:
        return self.__propSystem
