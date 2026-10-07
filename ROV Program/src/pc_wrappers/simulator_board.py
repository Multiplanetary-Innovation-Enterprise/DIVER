# board.py

class Pin:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Pin {self.name}>"

# Define dummy I2C pins
SCL = Pin("SCL")
SDA = Pin("SDA")
