from subsystems.Subsystem import Subsystem
from components.controllers.Controller import Controller



class AutonomySubsystem(Subsystem):
    __isEnabled = False
    def __init__(self, controller:Controller, config):
        super().__init__(controller, config)

    def makeDecision(self,sensorData:dict):
        if self.__isEnabled:
            pass

    def getEnabled(self):
        return self.isEnabled
    
    def setEnabled(self,enabled:bool):
        self.__isEnabled = enabled