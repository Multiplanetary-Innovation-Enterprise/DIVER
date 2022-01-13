import time

from signals.PinMode import PinMode
from signals.PWMSignal import PWMSignal
from signals.devices.SignalDevice import SignalDevice
from components.rotation.Motor import Motor
from components.rotation.RotDirection import RotDirection

#Represents the T200 thruster used on the ROV from bluerobotics
#url: https://www.bluerobotics.com/store/thrusters/t100-t200-thrusters/t200-thruster-r2-rp/
class Thruster(Motor):
    __MAX_REVERSE:int = 1100     #The PWM pulse width of the maximum reverse speed
    __MAX_FORWARD:int = 1900     #The PWM pulse width of the maximum forward speed
    __STOPPED:int = 1500         #The PWM pulse width when the motor is not running
    __pwmSignal:PWMSignal = None #The PWM signal used to control the thruster

    #Creates the thruster
    def __init__(self, device:SignalDevice, pinNum:int, rotDirection:RotDirection):
        super().__init__(rotDirection)

        self.__pwmSignal = PWMSignal(device, pinNum, PinMode.PIN_OUT)

    #Performs the arming sequence for the thruster
    def arm(self) -> None:
        self.__pwmSignal.setPulseWidth(0)
        time.sleep(1)

        self.__pwmSignal.setPulseWidth(self.__STOPPED)
        time.sleep(1)

    #Performs the speed update using the PWM interface
    def _updateSpeed(self) -> None:
        pulseWidth = self.__convertSpeedToPulsewidth(self.__speed)
        self.__pwmSignal.setPulseWidth(pulseWidth)

    #Performs the speed conversion from the range [-1,1] to [MAX_REVERSE,MAX_FORWARD]
    #STOPPED is the reference point with the total range being the difference between the max
    #reverse speed(MAX_REVERSE) and the max forward speed(MAX_FORWARD). The provided speed is then used
    #as a scalar for that range
    def __convertSpeedToPulsewidth(self, speed:float) -> int:
        #Determines the direction the thruster should rotate based on its current
        #rotational direction and the sign of the provided speed value
        speed = self.getRotDirection().value * speed

        #Converts the range [-1,1] to the actual PWM range
        pulseWidth = round(self__.STOPPED + ((self.__MAX_FORWARD - self.__.MAX_REVERSE) / 2) * speed)

        return pulseWidth

    #Stops the thruster
    def stop(self) -> None:
        self.setSpeed(self.__STOPPED)
