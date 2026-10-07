# busio.py

class I2C:
    def __init__(self, scl, sda, frequency=100000):
        self.scl = scl
        self.sda = sda
        self.frequency = frequency
        print(f"[I2C] Initialized dummy I2C with SCL={scl}, SDA={sda}, freq={frequency}")

    def scan(self):
        print("[I2C] scan() called")
        return [0x18]  # example: simulate one device at 0x18

    def writeto(self, address, buffer, *, stop=True):
        print(f"[I2C] writeto() -> address=0x{address:X}, buffer={list(buffer)}, stop={stop}")

    def readfrom(self, address, num_bytes, *, stop=True):
        print(f"[I2C] readfrom() -> address=0x{address:X}, num_bytes={num_bytes}, stop={stop}")
        return bytes([0x00] * num_bytes)

    def writeto_then_readfrom(self, address, out_buffer, in_buffer, *, out_start=0, out_end=None, in_start=0, in_end=None):
        print(f"[I2C] writeto_then_readfrom() -> address=0x{address:X}")
        for i in range(in_start, in_end or len(in_buffer)):
            in_buffer[i] = 0x00  # simulate dummy data
