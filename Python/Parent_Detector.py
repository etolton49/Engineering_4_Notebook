#
from picamera import PiCamera
from time import sleep
from gpiozero import MotionSensor

camera = PiCamera()
camera.rotation = 180



pir = MotionSensor(4)

while True:
    pir.wait_for_motion()
    camera.start_preview(fullscreen = False, window=(100,200,600,800))
    camera.start_recording("/home/pi/Desktop/camera_photos/Intruder.h264")
    print("move")
    pir.wait_for_no_motion()
    camera.stop_preview()
    camera.stop_recording()
    print(" ")
