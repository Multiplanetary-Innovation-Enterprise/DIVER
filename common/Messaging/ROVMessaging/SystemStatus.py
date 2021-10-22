from enum import Enum

#The different message types
class SystemStatus(Enum):
    INITIALIZING = 0
    ARMED = 1
    RUNNING = 2
    SHUT_DOWN = 3
