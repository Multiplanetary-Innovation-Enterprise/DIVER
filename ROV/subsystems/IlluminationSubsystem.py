from components.illumination.Light import Light
from components.illumination.SubseaLight import SubseaLight

class IlluminationSubsystem():
    __light: Light = None

    def __init__(self, pi):
        self.__light = SubseaLight(pi, 5)
        self.__light.setLastBrightness(0.1)

    def getLight(self) -> Light:
        return self.__light