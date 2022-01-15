#import board
#import adafruit_bno055

class IMU:
#    __sensor:BNO055 = None
#    __accelerometerData:tuple = None

    def __init__(self):
        #i2c = board.I2C()
        #self.__sensor = adafruit_bno055.BNO055(i2c)
        pass

    def getAccelerationData(self):
        return self.__accelerometerData

    def getMagnetometerData(self):
        pass

    def getAngularVelocityData(self):
        pass

    def getEulerOrientation(self):
        pass

    def getQuaterionOrientation(self):
        pass

    def getLinearAccelerationData(self):
        pass

    def getGravityAccelerationData(self):
        pass

    def getTemperature(self):
        pass

    def updateValues(self):
        self.__accelerationData = self.__sensor.acceleration
        self.__magnetometerData = self.__sensor.magnetic
        self.__angularVelocityData = self.__sensor.gyro
        self.__eulerOrientation = self.__sensor.euler
        self.__quaternionOrientation = self.__sensor.quaternion
        self.__linearAccelerationData = self.__sensor.linear_acceleration
        self.__gravityAccelerationData = self.__sensor.gravity
        self.__temperature = self.__sensor.temperature
