from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)

camera.capture('/home/pi/Desktop/image.jpg')
