# dummy_i2c.py

class I2C:
    def __init__(self, bus_id=1):
        self._bus_id = bus_id
        print(f"[I2C] Initialized dummy I2C on bus {bus_id}")

    def scan(self):
        print("[I2C] scan() called")
        return []  # Return empty list or mock addresses like [0x3C, 0x40]

    def writeto(self, address, buffer, *, stop=True):
        print(f"[I2C] writeto() called with address=0x{address:X}, buffer={list(buffer)}, stop={stop}")

    def readfrom(self, address, num_bytes, *, stop=True):
        print(f"[I2C] readfrom() called with address=0x{address:X}, num_bytes={num_bytes}, stop={stop}")
        return bytes([0x00] * num_bytes)  # Return dummy data

    def writeto_then_readfrom(
        self, address, out_buffer, in_buffer, *,
        out_start=0, out_end=None,
        in_start=0, in_end=None
    ):
        out_data = out_buffer[out_start:out_end]
        in_length = (in_end - in_start) if in_end else len(in_buffer)
        print(f"[I2C] writeto_then_readfrom() called with address=0x{address:X}, "
              f"out_data={list(out_data)}, in_length={in_length}")

        # Fill in_buffer with dummy data
        for i in range(in_start, in_start + in_length):
            in_buffer[i] = 0x00

    def __del__(self):
        print("[I2C] Dummy I2C bus closed")
