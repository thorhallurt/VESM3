import time
import board
import adafruit_bh1750
from gpiozero import LED

led = LED(17)
i2c = board.I2C()
sensor = adafruit_bh1750.BH1750(i2c)

while True:
    light = sensor.lux
    print("%.2f Lux" % light)

    if light < 200:
        led.on()
    else:
        led.off()

    time.sleep(1)
