import requests
from gpiozero import Button
from signal import pause

button = Button(21)
ledStatus = False

url = 'http://192.168.1.1'

def on_press(ledStatus):
    
    if ledStatus == False:
        x = requests.post(url, data = None)
        return True
    else:
        x = requests.post(url, data = None)
        return False

    print(ledStatus)
    print(x)

button.when_pressed = on_press

pause()
