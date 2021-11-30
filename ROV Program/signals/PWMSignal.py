from signals.RaspberryPiIOSignal import RaspberryPiIOSignal

class PWMSignal(RaspberryPiIOSignal):
    __pinNum:int = None
    __pulseWidth:int = None

    def __init__(self, raspberryPi, pinNum:int):
        super().__init__(raspberryPi)
        self.__pinNum = pinNum

    def setPinNum(self, pinNum:int) -> None:
        self.__pinNum = pinNum

    def getPinNum(self) -> int:
        return self.__pinNum

    def setPulseWidth(self, pulseWidth:int) -> None:
        self.__pulseWidth = pulseWidth
        self.getRaspberryPi().set_servo_pulsewidth(self.__pinNum, self.__pulseWidth)

    def getPulseWidth(self):
        return self.__pulseWidth
