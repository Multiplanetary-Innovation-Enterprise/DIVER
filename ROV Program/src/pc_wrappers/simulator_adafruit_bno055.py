

class BNO055:
    def __init__(self, i2c, address=0x28):
        self._i2c = i2c
        self._address = address
        self.magnetic = [0] * 3
        self.gyro = [0] * 3
        self.acceleration = [0] * 3
        self.linear_acceleration = [0] * 3
        self.gravity = [0] * 3
        self.quaternion = [0] * 4
        self.euler = [0] *3
        print(f"[BNO055] Initialized dummy BNO055 at address 0x{address:X}")


# ✅ Add this convenience wrapper
def BNO055_I2C(i2c, address=0x28):
    return BNO055(i2c, address)
