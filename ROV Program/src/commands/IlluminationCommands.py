from commands.Command import Command
from subsystems.IlluminationSubsystem import IlluminationSubsystem

#The command for toggling the ROV's lights
class ToggleLightStateCommand(Command):
    __illuminationSystem:IlluminationSubsystem = None #The ROV's illumination system

    def __init__(self, illuminationSystem:IlluminationSubsystem):
        self.__illuminationSystem = illuminationSystem

    #Executes the command
    def execute(self) -> None:
        light = self.__illuminationSystem.getLight()

        #Checks the light's current state
        if(light.isActive()):
            light.turnOff()
        else:
            light.turnOn()

    #Whether or not the command can be repeated back to back
    def isRepeatable(self) -> bool:
        return True

    #The action code associated with this command
    def getActionCode() -> int:
        return 11

#The command for increasing the ROV's light's brightness
class IncreaseLightBrightnessCommand(Command):
    __illuminationSystem:IlluminationSubsystem = None #The ROV's illumination system

    def __init__(self, illuminationSystem:IlluminationSubsystem):
        self.__illuminationSystem = illuminationSystem

    #Executes the command
    def execute(self) -> None:
        light = self.__illuminationSystem.getLight()

        #Gets the current brighness value of the light and increments it by 10%
        brightness = light.getBrightness() + 0.1

        #Updates the brightness of the light
        light.setBrightness(brightness)

    #Whether or not the command can be repeated back to back
    def isRepeatable(self) -> bool:
        return True

    #The action code associated with this command
    def getActionCode() -> int:
        return 12

#The command for decreasing the ROV's light's brightness
class DecreaseLightBrightnessCommand(Command):
    __illuminationSystem:IlluminationSubsystem = None #The ROV's illumination system

    def __init__(self, illuminationSystem:IlluminationSubsystem):
        self.__illuminationSystem = illuminationSystem

    #Executes the command
    def execute(self) -> None:
        light = self.__illuminationSystem.getLight()

        #Gets the current brighness value of the light and decrements it by 10%
        brightness = light.getBrightness() - 0.1

        #Updates the brightness of the light
        light.setBrightness(brightness)

    #Whether or not the command can be repeated back to back
    def isRepeatable(self) -> bool:
        return True

    #The action code associated with this command
    def getActionCode() -> int:
        return 13
