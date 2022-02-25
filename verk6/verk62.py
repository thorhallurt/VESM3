from Adafruit_IO import *
from gpiozero import Button
import time

aio = Client('thorhallurt', 'aio_ybgq74X7UVstaUk6LfZO7r0bMar7')

button = Button(12)

while True:
    if button.is_pressed == True:
        data = 1
    else:
        data = 0

    aio.send('button-state', data)
    time.sleep(3)
