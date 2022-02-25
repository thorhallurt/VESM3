from gpiozero import LED
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory(host='10.11.46.135')
red = LED(17, pin_factory=factory)

while True:
    red.on()
    sleep(1)
    red.off()
    sleep(1)
