#Represents a collection of IMU data
class IMUData:
    __data:dict = None #All of the data collected from the IMU sensor

    def __init__(self, data:dict):
        self.__data = data

    #Gets the 3 axis acceleration values
    def getAcc(self) -> list:
        return self.__data['acc']

    #Gets the 3 axis magenetic values
    def getMagnetic(self) -> list:
        return self.__data['magentic']

    #Gets the 3 axis angular velocity values
    def getAngularVelocity(self) -> list:
        return self.__data['angularVelocity']

    #Gets the 3 axis linear acceleration values
    def getLinearAcc(self) -> list:
        return self.__data['linAcc']

    #Gets the 3 axis gravity acceleration values
    def getGravityAcc(self) -> list:
        return self.__data['gravAcc']

    #Gets the orientation as euler angles
    def getOrientation(self) -> list:
        return self.__data['euler']

    #Gets the orientation as quaternions
    def getQuaternion(self) -> list:
        return self.__data['quaternion']

    #Gets the yaw value
    def getHeading(self) -> list:
        return self.__data['euler'][0]

    #Gets the roll value
    def getRoll(self) -> list:
        return self.__data['euler'][1]

    #Gets the pitch value
    def getPitch(self) -> list:
        return self.__data['euler'][2]

    #Gets all the data as a dict
    def toDict(self) -> dict:
        return self.__data
