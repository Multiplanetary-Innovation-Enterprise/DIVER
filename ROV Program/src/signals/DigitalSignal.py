from signals.RaspberryPiIOSignal import RaspberryPiIOSignal

class DigitalSignal(RaspberryPiIOSignal):
    __internalResisorType = None
    __pinNum:int = None
    __mode = None

    def __init__(self, raspberryPi, pinNum:int, mode):
        super().__init__(raspberryPi)
        self.__pinNum = pinNum

        self.setMode(mode)

    def setHigh(self) -> None:
        self.getRaspberryPi().write(self.__pinNum, 1)

    def setLow(self) -> None:
        self.getRaspberryPi().write(self.__pinNum, 0)

    def getValue(self) -> int:
        return self.getRaspberryPi().read(self.__pinNum)

    def setInternalResistorType(self, type):
        self.__internalResisorType = type
        self.getRaspberryPi().set_pull_up_down(self.__pinNum, type)

    def getInternalResistorType(self):
        return self.__internalResisorType

    def setMode(self, mode):
        self.getRaspberryPi().set_mode(self.__pinNum, mode)

    def getMode(self):
        return self.__mode
