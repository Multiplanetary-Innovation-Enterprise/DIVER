
# this class mimics the interface of the pigpio library
# currently it only returns dummy values to get it stable on pc

class pi:
    def __init__(self):
        print("[Mock pigpio] Initialized mock Pi object")
        # create array of pinmodes with 40 indicies
        self.pinMode = [0] * 40
        # create array of pin levels with 40 indecies
        self.pinLevel = [0] * 40
        # create array of pwm pulse witdths for 40 indecies
        self.pulseWidth = [0] * 40

    def set_mode(self, gpio, mode):
        self.pinMode[gpio] = mode

    def get_mode(self, gpio):
        return self.pinMode[gpio]

    def write(self, gpio, level):
        print(f"[Mock pigpio] write({gpio}, {level})")
        self.pinLevel[gpio] = level

    def read(self, gpio):
        print(f"[Mock pigpio] read({gpio})")
        return self.pinLevel[gpio]

    def stop(self):
        print("[Mock pigpio] stop()")

    def set_servo_pulsewidth(self, gpio, pulseWidth):
        #print(f"[Mock pigpio] pulseWidth set({gpio}, {pulseWidth})")
        self.pulseWidth[gpio] = pulseWidth

# Constants
INPUT = 0
OUTPUT = 1
HIGH = 1
LOW = 0