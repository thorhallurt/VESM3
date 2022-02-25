import gpiozero
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import subprocess
from time import sleep

disp = Adafruit_SSD1306.SSD1306_128_32(rst=None)

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new("1", (width, height))
img = Image.open('happycat_oled_32.ppm').convert("1")
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)

padding = -2
top = padding
bottom = height-padding
x = 0

font = ImageFont.load_default()

while True:

    draw.rectangle((0,0,width,height), outline=0, fill=0)

    draw.text((x + 3, top+8), "Thorhallur", font=font, fill=255)
    draw.text((x + 3, top+16), "Tryggvason", font=font, fill=255)

    disp.image(image)
    disp.display()

    sleep(5)

    draw.rectangle((0,0,width,height), outline=0, fill=0)
    disp.image(img)
    disp.display()

    sleep(5)
