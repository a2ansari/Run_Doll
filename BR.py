import pigpio
import time
import numpy as np
import os

#os.system('sudo pigpiod')
gpio = pigpio.pi()
servo = 12
slow = 1
fast = 5

#maximum 1250000
#minimum 250000

upperlim = int(input("Enter the highest arc point(S-90000 M-105000 L-90000):"))
lowerlim = int(input("Enter the lowest arc point(S-75000 M-90000 L-75000):"))
speed = int(input("Enter the speed(1 and above):"))

sum = 0
count = 0

    while True:
        t0 = time.time()
        for dc in np.arange(lowerlim,upperlim,speed):
            gpio.hardware_PWM(servo,50,dc)
        for dc in np.arange(upperlim,lowerlim,-1*speed):
            gpio.hardware_PWM(servo,50,dc)
        duration = time.time() - t0
        print("Time taken for one revolution: " + str(duration))
        sum +=duration
        print("THE BPM is:" + str(60/duration))

