# adafruit_mcp9808.py


class MCP9808:
    def __init__(self, i2c, address=0x18):
        self._i2c = i2c
        self._address = address
        print(f"[MCP9808] Initialized dummy MCP9808 at address 0x{address:X}")

    @property
    def temperature(self):
        # return dummy sensor value
        return 0
