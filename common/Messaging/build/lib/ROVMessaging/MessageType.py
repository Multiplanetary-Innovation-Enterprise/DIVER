from enum import Enum

#The different message types
class MessageType(Enum):
    ACTION = 0
    SYSTEM_STATUS = 1
    SENSOR_DATA = 2
    VISION_DATA = 3
