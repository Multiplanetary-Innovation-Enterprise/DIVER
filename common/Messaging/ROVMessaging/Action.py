from enum import Enum

class Action(Enum):
    MOVE_X_POS = 0
    MOVE_X_NEG = 1
    MOVE_X_STOP = 2
    MOVE_Y_POS = 3
    MOVE_Y_NEG = 4
    MOVE_Y_STOP = 5
    MOVE_Z_POS = 6
    MOVE_Z_NEG = 7
    MOVE_Z_STOP = 8
    SPEED_INCREASE = 9
    SPEED_DECREASE = 10
    ARM = 11
    TOGGLE_LIGHTS = 12
    BRIGHTNESS_INCREASE = 13
    BRIGHTNESS_DECREASE = 14
