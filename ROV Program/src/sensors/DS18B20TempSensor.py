#from w1thermsensor import W1ThermSensor, Unit

from util.TempUnit import TempUnit
from sensors.TempSensor import TempSensor

class DS18B20TempSensor(TempSensor):
    __sensor = None

    def __init__(self, tempUnit:TempUnit = TempUnit.F):
        super().__init__(tempUnit)

        #self.__sensor = W1ThermSensor()

    def getTemperature(self) -> float:
        if self._tempUnit == TempUnit.F:
            temp = self.__sensor.get_temperature(Unit.DEGREES_F)
        elif self._tempUnit == TempUnit.C:
            temp = self.__sensor.get_temperature()

        temp = round(temp, 2)

        return temp
