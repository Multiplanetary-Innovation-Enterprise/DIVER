from abc import ABC

from commands.Command import Command
from subsystems.IlluminationSubsystem import IlluminationSubsystem

#Represents a generic illumination command
class IlluminationCommand(Command, ABC):
    _illuminationSystem:IlluminationSubsystem = None #The ROV's illumination system

    def __init__(self, illuminationSystem:IlluminationSubsystem):
        self._illuminationSystem = illuminationSystem

    #Whether or not the command can be repeated back to back
    def isRepeatable(self) -> bool:
        return True

#The command for toggling the ROV's lights
class ToggleLightStateCommand(IlluminationCommand):
    #Executes the command
    def execute(self) -> None:
        light = self._illuminationSystem.getLight()

        print("Lights toggle")

        #Checks the light's current state
        if(light.isActive()):
            light.turnOff()
        else:
            light.turnOn()

    #The action code associated with this command
    @staticmethod
    def getActionCode() -> int:
        return 11

#The command for increasing the ROV's light's brightness
class IncreaseLightBrightnessCommand(IlluminationCommand):
    #Executes the command
    def execute(self) -> None:
        light = self._illuminationSystem.getLight()

        #Gets the current brighness value of the light and increments it by 10%
        brightness = light.getBrightness() + 0.1
        print("Brightness inc: " + str(brightness))

        #Updates the brightness of the light
        light.setBrightness(brightness)

    #The action code associated with this command
    @staticmethod
    def getActionCode() -> int:
        return 12

#The command for decreasing the ROV's light's brightness
class DecreaseLightBrightnessCommand(IlluminationCommand):
    #Executes the command
    def execute(self) -> None:
        light = self._illuminationSystem.getLight()

        #Gets the current brighness value of the light and decrements it by 10%
        brightness = light.getBrightness() - 0.1
        print("Brightness dec: " + str(brightness))

        #Updates the brightness of the light
        light.setBrightness(brightness)

    #The action code associated with this command
    @staticmethod
    def getActionCode() -> int:
        return 13
