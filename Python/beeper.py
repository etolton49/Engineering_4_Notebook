import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
for i in range(10):
    GPIO.output(21, GPIO.HIGH)
    print("High")
    sleep(.1)
    GPIO.output(21, GPIO.LOW)
    print("Low")
    sleep(1)
GPIO.cleanup()
