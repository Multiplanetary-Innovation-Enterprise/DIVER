# from adafruit_blinka.microcontroller.generic_linux.i2c import I2C
import board
import adafruit_bno055

from components.sensors.IMUData import IMUData
from components.sensors.IMU import IMU

#Represents the BNO055 IMU sensor from Adafruit
#url:https://www.adafruit.com/product/2472
class BNO055IMU(IMU):
    __sensor = None #The IMU sensor

    def __init__(self):
        # i2c = I2C(0, mode=I2C.MASTER, baudrate=1000000)
        # self.__sensor = adafruit_bno055.BNO055_I2C(i2c)

        i2c = board.I2C()

        try:
            self.__sensor = adafruit_bno055.BNO055_I2C(i2c)
        except:
            print("Failed to detect the IMU sensor")
    #Gets all of the data from the IMU sensor
    def getSensorData(self) -> IMUData:
        #All of the IMU data
        data = {
            "acc": self.__sensor.acceleration,
            "magentic": self.__sensor.magnetic,
            "angularVelocity": self.__sensor.gyro,
            "linAcc": self.__sensor.linear_acceleration,
            "gravAcc": self.__sensor.gravity,
            "euler": self.__sensor.euler,
            "quaternion": self.__sensor.quaternion,
        };

        return IMUData(data)

    #Gets the temperature of the IMU sensor
    def getTemperature(self) -> float:
        return self.__sensor.temperature()
