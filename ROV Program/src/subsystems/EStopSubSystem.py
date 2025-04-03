from subsystems.Subsystem import Subsystem
from components.controllers.Controller import Controller
from PropulsionSubsystem import PropulsionSubsystem


class EStopSubsystem(Subsystem):
    __isEnabled = False
    def __init__(self, controller:Controller, config,propSys:PropulsionSubsystem):
        super().__init__(controller, config)
        self.__propSys = propSys



    def getEnabled(self):
        return self.isEnabled
    
    def setEnabled(self,enabled:bool):
        self.__isEnabled = enabled

    #Temporarily setting these to do E-stop level 1 to appease paul (just shuts off thrusters)
    def triggerEStop(self):
        #TRIGGER ESTOP PINS HERE
        if self.__isEnabled:
            self.__propSys.shutdown()
        