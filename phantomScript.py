import time
import RPi.GPIO as GPIO
import sys

# use the phantomFindServoDefs.py script to find required servo definitions
servoPIN = 17       # either plug the control wire into this pin or change this definition
PWM = 50            # adjust this to desired PWM
center = 7.6        # adjust this once a good PWM is found
servoMaxDelta = 4.7   # adjust this once center is found, adjust until servo arm goes 180 degrees


breathRate = int(input('Please enter desired breathing rate (10-30): '))
try:
    while breathRate > 30 or breathRate < 10:
        breathRate = int(input('Please enter desired breathing rate within range (10-30): '))
except TypeError:
    print('Invalid input - exiting')
    sys.exit()

chestDisplacement = int(input('Please enter desired chest displacment (10mm - 20mm): '))

try:
    while chestDisplacement > 20 or chestDisplacement < 10:
        chestDisplacement = int(input('Please enter desired chest displacment within range (10mm-20mm): '))
except TypeError:
    print('Invalid input - exiting')
    sys.exit()


# servoMaxDelta = servoMaxDelta*(2/3) + (chestDisplacement-10)*(servoMaxDelta/30)
# simplified version of the above equation 
servoMaxDelta = servoMaxDelta * ((10.0 + chestDisplacement)/30.0)

# timeDelta = (60/breathRate)/(2*servoMaxDelta/0.1)
# simplified version of the above equation 
timeDelta = 3.0/(breathRate*servoMaxDelta)



GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
pin = GPIO.PWM(servoPIN, PWM) 

currPOS = center - servoMaxDelta
pin.start(currPOS)
breathCount = 0
try:
    while True:
        while currPOS < (center + servoMaxDelta):
            #move motor towards other end
            pin.ChangeDutyCycle(currPOS) 
            time.sleep(timeDelta)
            currPOS = currPOS + 0.1
        time.sleep(timeDelta)
        breathCount += 1
        print('Breaths: '+ str(breathCount))
        while currPOS > (center - servoMaxDelta):
            # move servo towards other end
            pin.ChangeDutyCycle(currPOS) 
            time.sleep(timeDelta)
            currPOS = currPOS - 0.1
        time.sleep(timeDelta)
        breathCount += 1
        print('Breaths: '+ str(breathCount))
except KeyboardInterrupt:
        pin.ChangeDutyCycle(center) 
        time.sleep(1)
        pin.stop()
        GPIO.cleanup()

