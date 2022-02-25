import picamera
from datetime import datetime

with picamera.PiCamera() as camera:
    camera.resolution = (680, 480)
    now = datetime.now()
    camera.start_recording('/home/pi/Videos/%s.h264' % now)
    print("started recording")
    camera.wait_recording(60)
    camera.stop_recording()
