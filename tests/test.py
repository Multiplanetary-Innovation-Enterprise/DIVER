from components.illumination.SubseaLight import SubseaLight

import pigpio
import os
import time

#Pi connection setup
os.system ("sudo pigpiod")
time.sleep(1)

pi = pigpio.pi();
# pi.set_servo_pulsewidth(4, 3000)
# print(pi.get_servo_pulsewidth(4))

light = SubseaLight(pi, 4)

print("Last: " +  str(light.getLastBrightness()))
print("Current: " +  str(light.getBrightness()))
time.sleep(1)

light.setBrightness(0.1)
print("Last: " +  str(light.getLastBrightness()))
print("Current: " +  str(light.getBrightness()))
time.sleep(1)

light.setBrightness(0.5)
print("Last: " +  str(light.getLastBrightness()))
print("Current: " +  str(light.getBrightness()))
time.sleep(1)

light.setBrightness(0)
print("Last: " +  str(light.getLastBrightness()))
print("Current: " +  str(light.getBrightness()))
time.sleep(1)
