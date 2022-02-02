import pigpio
import os
import time

os.system ("sudo pigpiod")
time.sleep(1)

pi = pigpio.pi()
pi.set_PWM_frequency(17, 50)

print("180!")
pi.set_PWM_dutycycle(17, 0.105 * 255)
time.sleep(2)

print("90!")
pi.set_PWM_dutycycle(17, 0.005 * 255)
time.sleep(2)

# print("0!")
# pi.set_PWM_dutycycle(17, 0.11 * 255)
# time.sleep(2)
