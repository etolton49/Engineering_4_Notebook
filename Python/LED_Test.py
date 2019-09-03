GPIO.cleanup()#making sure no warnings are thrown
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)#specify number system used
#setup pins
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

for i in range(0,10):
    GPIO.output(20, GPIO.HIGH)
    GPIO.output(21, GPIO.HIGH)
    sleep(.2)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    sleep(.2)
GPIO.cleanup()
