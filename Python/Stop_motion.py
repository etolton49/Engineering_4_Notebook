#
from time import sleep
from picamera import PiCamera
from gpiozero import Button

button = Button(21                                                                                                                                                                                                                                            )
camera = PiCamera()

camera.rotation = 180
camera.start_preview(fullscreen = False, window=(100,200,600,800))

counter = 0    
while True:
    try:

        button.wait_for_press()
        camera.capture('/home/pi/Desktop/Animation/Button_capture%03d.jpg' % counter)
        counter += 1

    except KeyboardInterrupt:
        camera.stop_preview()
        break
