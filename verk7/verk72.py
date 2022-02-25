from Adafruit_IO import *
from gpiozero import Button
import time

aio = Client('thorhallurt', 'aio_ybgq74X7UVstaUk6LfZO7r0bMar7')

button = Button(12)
lastButtonPress = False

while True:
    if button.is_pressed == True and lastButtonPress == False:
        data = 1
        print("Pressed button")
        aio.send('hello', data)
    elif button.is_pressed == False and lastButtonPress == True:
        data = 0
        print("Released button")
        aio.send('hello', data)
