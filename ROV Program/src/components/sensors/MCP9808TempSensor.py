try:
    from adafruit_blinka.microcontroller.generic_linux.i2c import I2C
except ImportError:
    from pc_wrappers.simulator_adafruit_blinka import I2C

try:
    import board
except ImportError:
    import pc_wrappers.simulator_board as board

try:    
    import busio
except ImportError:
    import pc_wrappers.simulator_busio as busio

try:
    import adafruit_mcp9808
except ImportError:
    import pc_wrappers.simulator_adafruit_mcp9808 as adafruit_mcp9808

from components.sensors.TempUnit import TempUnit
from components.sensors.TempSensor import TempSensor

#Represents the MCP9808 Temp Sensor sensor from Adafruit
#url:https://cdn-learn.adafruit.com/downloads/pdf/adafruit-mcp9808-precision-i2c-temperature-sensor-guide.pdf
class MCP9808TempSensor(TempSensor):
    __sensor = None #The Temp Sensor sensor

    def __init__(self, tempUnit:TempUnit = TempUnit.C):
        super().__init__(tempUnit)
        #Attempts to connect to the Temp Sensor
        try:
            #BEFORE YOU TRY EDITING THIS: The other pair of I2C pins on the Pi is burnt out, so do not use it
            board.SDA = 0
            board.SCL = 1
            i2c = busio.I2C(board.SCL,board.SDA)
            self.__sensor = adafruit_mcp9808.MCP9808(i2c)
            self._isConnected = True
        except ValueError:
            self._isConnected = False
            print("Failed to Detect Tempature sensor")


    #Gets the temperature reading from the sensor
    def getTemperature(self) -> float:
        #Skips the temperature reading if the sensor was not found
        if not self._isConnected:
            return None

        #Performs the temperature reading, probably unnecessary
        #tempC = self.__sensor.temperature

        return super().getTemperature()

    #Returns the current temperature value in celsius
    def _getTemperatureC(self) -> float:
        return self.__sensor.temperature

    #Returns the current temperature value in fahrenheit
    def _getTemperatureF(self) -> float:
        return (self.__sensor.temperature * 9/5) + 32

    #Returns the current temperature value in kelvin
    def _getTemperatureK(self) -> float:
        return self.__sensor.temperature + 273.15

