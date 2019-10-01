from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180
effects = ['none', 'negative', 'sketch','denoise','emboss','oilpaint','gpen','pastel','film']
photo_counter = 0
camera.start_preview(fullscreen = False, window=(100,200,600,800))


for i in effects:
    camera.image_effect = i
    camera.annotate_text_size = 160
    camera.annotate_text = "Check out " + i + "!!!!"
    if photo_counter < 5:
        camera.capture('/home/pi/Desktop/camera_photos/photo_effect0'+str(photo_counter)+'.jpg')
        photo_counter += 1
    else:
        camera.start_preview(fullscreen = False, window=(100,200,600,800))
    sleep(5)
    

camera.stop_preview()
