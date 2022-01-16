import board
import adafruit_bno055

from components.sensors import IMUData
from components.sensors.IMU import IMU

#Move sensors to components

#Represents the BNO055 IMU sensor from Adafruit
#url:https://www.adafruit.com/product/2472
class BNO055IMU(IMU):
     __sensor:BNO055 = None #The IMU sensor

    def __init__(self):
        i2c = board.I2C()
        self.__sensor = adafruit_bno055.BNO055(i2c)

    #Gets all of the data from the IMU sensor
    def getSensorData(self) -> IMUData:
        #All of the IMU data
        data = {
            "acc": sensor.acceleration(),
            "magentic": sensor.magnetic(),
            "angularVelocity": sensor.gyro(),
            "linAcc": sensor.linear_acceleration(),
            "gravAcc": sensor.gravity(),
            "euler": sensor.euler(),
            "quaternion": sensor.quaternion(),
        };

        return IMUData(data)

    #Gets the temperature of the IMU sensor
    def getTemperature(self) -> float:
        return self.__sensor.temperature()
