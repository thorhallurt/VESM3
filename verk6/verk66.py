from Adafruit_IO import *
from gpiozero import PWMLED
from time import sleep

aio = Client('thorhallurt', 'aio_ybgq74X7UVstaUk6LfZO7r0bMar7')
led = PWMLED(12)

while True:
    data = aio.receive('light-toggle')
    print(data.value)
    print(led.value)

    if data.value == "1" and led.value < 0.9:
        print("Starting")
        for i in range(1, 10, 1):
            led.value = i / 10
            sleep(0.5)

    elif data.value == "0" and led.value >= 0.9:
        print("Starting dimming")
        for i in range(10, 1, -1):
            led.value = i /10
            sleep(0.5)

    sleep(3)
