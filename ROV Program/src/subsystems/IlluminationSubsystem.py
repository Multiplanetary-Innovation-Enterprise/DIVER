from subsystems.Subsystem import Subsystem
from components.illumination.Light import Light
from components.illumination.SubseaLight import SubseaLight
from components.controllers.Controller import Controller

#Represents the subsystem for controlling the lights
class IlluminationSubsystem(Subsystem):
    __light:Light = None #The dual LED lights (placement TBD)

    def __init__(self, controller:Controller, config):
        super().__init__(controller, config)

        #Gets the light GPIO pin from the config file
        lightPin = int(config['Illumination']['SubseaLightPin'])

        #Sets up the light
        self.__light = SubseaLight(controller, lightPin)
        self.__light.setBrightness(0.1)

    #Gets the light
    def getLight(self) -> Light:
        return self.__light

    #Performs any clean up on system shutdown
    def shutdown(self) -> None:
        pass
