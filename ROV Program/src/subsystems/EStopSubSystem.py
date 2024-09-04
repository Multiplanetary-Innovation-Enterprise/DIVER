from subsystems.Subsystem import Subsystem
from components.controllers.Controller import Controller



class EStopSubsystem(Subsystem):
    __isEnabled = False
    def __init__(self, controller:Controller, config):
        super().__init__(controller, config)

    def getEnabled(self):
        return self.isEnabled
    
    def setEnabled(self,enabled:bool):
        self.__isEnabled = enabled

    def triggerEStop():
        #TRIGGER ESTOP PINS HERE
        pass
        