import paho.mqtt.client as mqtt
from gpiozero import LED
import time
import board
import adafruit_bh1750
import json

led = LED(17)
i2c = board.I2C()
sensor = adafruit_bh1750.BH1750(i2c)

id = 'thorhallurt'
client_name = id + 'nightlight_client'
client_telemetry_topic = id + '/telemetry'
client_command_topic = id + '/commands'

mqtt_client = mqtt.Client(client_name)
mqtt_client.connect('test.mosquitto.org')

def handle_commands(client, userdata, message):

    payload = json.loads(message.payload.decode())
    print("Message received:", payload)
    if payload == {'led_on': True}:
        led.on()
    else:
        led.off()

mqtt_client.loop_start()
mqtt_client.subscribe(client_command_topic)
mqtt_client.on_message = handle_commands

print("MQTT connected!")

while True:

    light = round(sensor.lux)
    telemetry = json.dumps({'light' : light})
    print("Sending telemetry ", telemetry)

    mqtt_client.publish(client_telemetry_topic, telemetry)

    time.sleep(5)
