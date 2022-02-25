import requests
from gpiozero import Button
from signal import pause

button = Button(12)

url = 'https://maker.ifttt.com/trigger/button_pressed/with/key/nv7Iz6H-kxwr33POxhJsoZZKQmqNIDhzyBr_QW3tWZJ'

def on_press():
    x = requests.post(url)
    print(x)

button.when_pressed = on_press

pause()
