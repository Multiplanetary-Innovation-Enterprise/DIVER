from components.illumination.SubseaLight import SubseaLight

import pigpio
import os
import time

#Pi connection setup
os.system ("sudo pigpiod")
time.sleep(1)

pi = pigpio.pi();

light = SubseaLight(pi, 5)
light.setBrightness(0.1)
