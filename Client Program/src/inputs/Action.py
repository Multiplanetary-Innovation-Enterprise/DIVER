from enum import Enum

#Actions that correspond to the commands that the ROV can perform
class Action(Enum):
    ARM = 0
    MOVE_XY_STOP = 1
    MOVE_XY_FORWARD = 2
    MOVE_XY_BACKWARD = 3
    MOVE_XY_LEFT = 4
    MOVE_XY_RIGHT = 5
    MOVE_Z_STOP = 6
    MOVE_Z_UP = 7
    MOVE_Z_DOWN = 8
    SPEED_INCREASE = 9
    SPEED_DECREASE = 10
    TOGGLE_LIGHTS = 11
    BRIGHTNESS_INCREASE = 12
    BRIGHTNESS_DECREASE = 13
    CAPTURE_IMAGE = 14
    TURN_XY_CW = 15
    TURN_XY_CCW = 16
    E_STOP = 17

