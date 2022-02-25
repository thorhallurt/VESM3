from bluedot import BlueDot, COLORS
from random import choice
from gpiozero import RGBLED
from signal import pause

led = RGBLED(red=4, green=17, blue=27)

def pressed(pos):
    if pos.col == 0 and pos.row == 0:
        led.blue = 1
    elif pos.col == 0 and pos.row == 1:
        led.red = 1
    elif pos.col == 1 and pos.row == 0:
        led.green = 1
    else:
        led.red = 1
        led.green = 1
        led.blue = 0


def unpress():
    led.red = 0
    led.blue = 0
    led.green = 0

bd = BlueDot(cols=2, rows=2)

bd.when_pressed = pressed
bd.when_released = unpress

bd[0,0].color = "blue"
bd[0,1].color = "red"
bd[1,0].color = "green"
bd[1,1].color = "yellow"

pause()
