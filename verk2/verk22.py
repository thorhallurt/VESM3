from picamera import PiCamera
from gpiozero import Button
from signal import pause
from datetime import datetime
from time import sleep

camera = PiCamera()
button = Button(12)
camera.resolution = (1024, 768)

def capture():
    sleep(3)
    timestamp = datetime.now().isoformat()
    print("Taking picture %s" % timestamp)
    camera.capture('/home/pi/Desktop/images/%s.jpg' % timestamp)

button.when_pressed = capture
pause()
