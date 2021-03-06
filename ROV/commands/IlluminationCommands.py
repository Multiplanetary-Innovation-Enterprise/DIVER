from commands.Command import Command

class LightStateToggleCommand(Command):
    __illuminationSystem: IlluminationSystem = None

    def __init__(self, illuminationSystem:IlluminationSystem):
        self.__illuminationSystem = illuminationSystem

    def execute(self):
        light = self.__illuminationSystem.getLight()

        if(light.isOn()):
            light.turnOff()
        else:
            light.turnOn()

class LightIncreaseBrightnessCommand(Command):
    pass

class LightDecreaseBrightnessCommand(Command):
    pass
