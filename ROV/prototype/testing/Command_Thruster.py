# This program will let you test your ESC and brushless motor.
# Make sure your battery is not connected if you are going to calibrate it at first.
# Since you are testing your motor, I hope you don't have your propeller attached to it otherwise you are in trouble my friend...?
# This program is made by AGT @instructable.com. DO NOT REPUBLISH THIS PROGRAM... actually the program itself is harmful                                             pssst Its not, its safe.

import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio #importing GPIO library

ESC=4  #Connect the ESC in this GPIO pin

pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC, 0)

max_value = 2000 #change this if your ESC's max value is different or leave it be
min_value = 700  #change this if your ESC's min value is different or leave it be

def arm(): #This is the arming procedure of an ESC
    print "Connect the battery and press Enter"
    inp = raw_input()
    if inp == '':
        pi.set_servo_pulsewidth(ESC, max_value)
        print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
        inp = raw_input()
        if inp == '':
            pi.set_servo_pulsewidth(ESC, min_value)
            print "Wierd eh! Special tone"
            time.sleep(7)
            print "Wait for it ...."
            time.sleep (5)
            print "Im working on it, DONT WORRY JUST WAIT....."
            pi.set_servo_pulsewidth(ESC, 0)
            time.sleep(2)
            print "Arming ESC now..."
            pi.set_servo_pulsewidth(ESC, min_value)
            time.sleep(1)

def forward():
    pi.set_servo_pulsewidth(ESC, 1600)

def backward():
    pi.set_servo_pulsewidth(ESC, -1560)

def stop(): #This will stop every action your Pi is performing for ESC ofcourse.
    pi.set_servo_pulsewidth(ESC, 1500)

def quit():
    pi.stop()

arm()

print "Commands: forward, backward, stop, quit."

#This is the start of the program actually, to start the function it needs to be initialized before calling... stupid python.
pi.set_servo_pulsewidth(ESC, 1500)
while True:
    inp = raw_input()
    if inp == "forward":
        forward()
    elif inp == "backward":
        backward()
    elif inp == "stop":
        stop()
    elif inp == "quit":
        quit()
