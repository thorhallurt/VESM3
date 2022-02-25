from gpiozero import LED, Button
from signal import pause

button = Button(2)
led = LED(17)

led.source = button

pause()
