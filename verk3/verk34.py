import json
import gpiozero
from mfrc522 import SimpleMFRC522
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from board import SDA, SCL
from time import sleep
import busio

i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C, reset=None)
reader = SimpleMFRC522()

disp.fill(1)
disp.show()

width = disp.width
height = disp.height
image = Image.new("1", (width, height))
draw = ImageDraw.Draw(image)
padding = -2
top = padding
bottom = height - padding
x = 0
font = ImageFont.load_default()

def _clear():
    disp.fill(0)
    draw.rectangle(

def _appendToID(new_data, id, location = None, jsonFile='attendance.json'):
    with open(jsonFile, 'r+') as file:
        file_data = json.load(file)
        if location != None:
            file_data["users"][id][0]["logs"].append(new_data)
        else:
            file_data["users"][id][0]["in"] = new_data
        file.seek(0)
        json.dump(file_data, file, indent = 4)

while True:
    try:
        disp.fill(1)
        disp.show()
        draw.text((x + 3, top + 16), "Place key", font=font, fill=255)
        disp.image(image)
        disp.show()
        id, text = reader.read()
        id = str(id)
        f = open('attendance.json', 'r')
        data = json.load(f)
        if id in data["users"]:
            
            _appendToID(str(datetime.now()), id, 1)
            if data["users"][id][0]["in"] == 1:
                _appendToID(0, id)
                disp.fill(1)
                disp.show()
                draw.text((x + 3, top + 8), "Welcome back,", font=font, fill=255)
                draw.text((x + 3, top + 16), id, font=font, fill=255)
                disp.image(image)
                disp.show()
            else:
                _appendToID(1, id)
                disp.fill(1)
                disp.show()
                draw.text((x + 3, top + 8), id, font=font, fill=255)
                draw.text((x + 3, top + 16), "declined", font=font, fill=255)
                disp.image(image)
                disp.show()
            sleep(3)

        else:
            temp_string = "Allow new id:", id, "y/n: "
            temp_input = input(temp_string)
            if temp_input.upper() == "Y":
                print("Added new for", id)
                new_data = [{'perm': 1,
                    'in': 1,
                    "logs": [str(datetime.now())]}]
                disp.fill(1)
                disp.show()
                draw.text((x + 3, top + 8), "Welcome,", font=font, fill=255)
                draw.text((x + 3, top + 16), id, font=font, fill=255)
                disp.image(image)
                disp.show()

            else:
                print("Denied entry for", id)
                new_data = [{'perm': 0,
                    'in': 0,
                    "logs": [str(datetime.now())]}]
                disp.fill(1)
                disp.show()
                draw.text((x + 3, top + 8), id, font=font, fill=255)
                draw.text((x + 3, top + 16), "declined", font=font, fill=255)
                disp.image(image)
                disp.show()

            with open("attendance.json", "r+") as outfile:
                file_data = json.load(outfile)
                file_data["users"][id] = new_data
                outfile.seek(0)
                json.dump(file_data, outfile, indent = 4)
            sleep(3)
            disp.fill(1)
            disp.show()
        f.close()
        sleep(1)

    except KeyboardInterrupt:
        print("Exiting")
        break
