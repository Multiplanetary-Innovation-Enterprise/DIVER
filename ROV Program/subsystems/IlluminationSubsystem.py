from components.illumination.Light import Light
from components.illumination.SubseaLight import SubseaLight

import configparser

class IlluminationSubsystem():
    __light: Light = None

    def __init__(self, pi):
        config = configparser.ConfigParser()

        config.read('config.ini')
        lightPin = int(config['Illumination']['SubseaLightPin'])

        self.__light = SubseaLight(pi, lightPin)
        self.__light.setLastBrightness(0.1)

    def getLight(self) -> Light:
        return self.__light
