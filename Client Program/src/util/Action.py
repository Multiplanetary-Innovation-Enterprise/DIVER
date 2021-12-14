from enum import Enum

#Actions that correspond to the commands that the ROV can perform
class Action(Enum):
    MOVE_XY_STOP = 0
    MOVE_XY_FORWARD = 1
    MOVE_XY_BACKWARD = 2
    MOVE_XY_LEFT = 3
    MOVE_XY_RIGHT = 4
    MOVE_Z_POS = 6
    MOVE_Z_NEG = 7
    MOVE_Z_STOP = 8
    SPEED_INCREASE = 9
    SPEED_DECREASE = 10
    ARM = 11
    TOGGLE_LIGHTS = 12
    BRIGHTNESS_INCREASE = 13
    BRIGHTNESS_DECREASE = 14