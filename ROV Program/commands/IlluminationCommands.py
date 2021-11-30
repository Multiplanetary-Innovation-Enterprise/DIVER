from commands.Command import Command
from subsystems.IlluminationSubsystem import IlluminationSubsystem

class LightStateToggleCommand(Command):
    __illuminationSystem: IlluminationSubsystem = None

    def __init__(self, illuminationSystem:IlluminationSubsystem):
        self.__illuminationSystem = illuminationSystem

    def execute(self):
        light = self.__illuminationSystem.getLight()

        if(light.isOn()):
            light.turnOff()
        else:
            light.turnOn()

    def isRepeatable(self):
        return True

class LightIncreaseBrightnessCommand(Command):
    __illuminationSystem: IlluminationSubsystem = None

    def __init__(self, illuminationSystem:IlluminationSubsystem):
        self.__illuminationSystem = illuminationSystem

    def execute(self):
        light = self.__illuminationSystem.getLight()

        if not light.isOn():
            return

        brightness = light.getBrightness()

        if(brightness < 1):
            brightness += 0.1;

        light.setBrightness(brightness)

    def isRepeatable(self):
        return True

class LightDecreaseBrightnessCommand(Command):
    __illuminationSystem: IlluminationSubsystem = None

    def __init__(self, illuminationSystem:IlluminationSubsystem):
        self.__illuminationSystem = illuminationSystem

    def execute(self):
        light = self.__illuminationSystem.getLight()

        if not light.isOn():
            return

        brightness = light.getBrightness()

        if(brightness > 0):
            brightness -= 0.1;
    
        light.setBrightness(brightness)

    def isRepeatable(self):
        return True
