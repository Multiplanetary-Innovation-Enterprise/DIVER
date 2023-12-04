import sys
import subprocess

class CoreTempSensor:
    
    
    def __init__(self):
        pass

    
    def getCoreTemp(self):
        x=subprocess.run(['vcgencmd',' measure_temp'],capture_output=True)
        y=x.stdout.decode()
        CoreTemp=y[5:9]
        return CoreTemp
