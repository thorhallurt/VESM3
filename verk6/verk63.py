from Adafruit_IO import *
from gpiozero import LED
from time import sleep

aio = Client('thorhallurt', 'aio_ybgq74X7UVstaUk6LfZO7r0bMar7')
led = LED(17)

while True:
    data = aio.receive('light-toggle')
    if data.value == "1":
        led.on()
    else:
        led.off()

    sleep(3)
