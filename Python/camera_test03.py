from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180

camera.start_preview(fullscreen = False, window=(100,200,600,800))
camera.start_recording('/home/pi/Desktop/camera_photos/myVid.h264')
for i in range(1,10):
    camera.annotate_text = str(i)
    sleep(1)
camera.stop_recording()
camera.stop_preview()
