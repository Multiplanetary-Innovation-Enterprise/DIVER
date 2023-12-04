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
        #Attempts to connect to the IMU: modified 11/11/23
        try:
            i2c = board.I2C()
            #^ formally I2C(0, mode=I2C.MASTER, baudrate=1000000), but this doesn't work since
            #the libraries got updated
            self.__sensor = adafruit_bno055.BNO055_I2C(i2c)
            self._isConnected = True
        Except ValueError:
            self._isConnected = False
            print("Failed to Detect IMU sensor")


    #Gets all of the data from the IMU sensor
    def getSensorData(self) -> IMUData:
        #Skips data collection if the sensor is not connected
        if not self._isConnected:
            return None

        acc = self.__sensor.acceleration
        magentic = self.__sensor.magnetic
        gyro = self.__sensor.gyro
        linAcc = self.__sensor.linear_acceleration
        gravAcc = self.__sensor.gravity
        euler = self.__sensor.euler
        quaternion = self.__sensor.quaternion

        #All of the IMU data
        data = {
            "acc_x": acc[0],
            "acc_y": acc[1],
            "acc_z": acc[2],
            "magentic_x": magentic[0],
            "magentic_y": magentic[1],
            "magentic_z": magentic[2],
            "gyro_x": gyro[0],
            "gyro_y": gyro[1],
            "gyro_z": gyro[2],
            "linAcc_x": linAcc[0],
            "linAcc_y": linAcc[1],
            "linAcc_z": linAcc[2],
            "gravAcc_x": gravAcc[0],
            "gravAcc_y": gravAcc[1],
            "gravAcc_z": gravAcc[2],
            "heading": euler[0],
            "roll": euler[1],
            "pitch": euler[2],
            "quaternion_x": quaternion[0],
            "quaternion_y": quaternion[1],
            "quaternion_z": quaternion[2],
            "quaternion_z": quaternion[3],
        };

        return IMUData(data)

    #Gets the temperature of the IMU sensor
    def getTemperature(self) -> float:
        return self.__sensor.temperature()
