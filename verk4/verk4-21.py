from gpiozero import Button, LED
from gpiozero.pins.pigpio import PiGPIOFactory
from signal import pause

factory = PiGPIOFactory(host='10.11.46.126')

button = Button(21)
led = LED(17, pin_factory=factory)

led.source = button

pause()
