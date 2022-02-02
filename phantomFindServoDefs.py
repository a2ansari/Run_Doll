# script to help find servo definitions

import time
import RPi.GPIO as GPIO

servoPIN = 17  
PWM = 50 
center = 7.6 # change this until the servo initilizes in the center of its 180 motion
servoMaxDelta = 4.7 #change this until the servo moves to 90 degrees from center

GPIO.setupmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
pin = GPIO.PWM(servoPIN, PWM) 

pin.start(center)

try:
    # this loop will make the motor move between 90 degrees, 180 degrees and 0 degrees, adjust values until it does
    while True:
        pin.ChangeDutyCycle(center) # duty cycle should be 7.5
        time.sleep(1)
        pin.ChangeDutyCycle(center + servoMaxDelta) # duty cycle should be 12.5
        time.sleep(1)
        pin.ChangeDutyCycle(center - servoMaxDelta) # duty cycle should be 2.5
        time.sleep(1)
except KeyboardInterrupt:
    pin.stop()
    GPIO.cleanup()

