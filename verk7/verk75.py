import os
from picamera import PiCamera
import requests

camera = PiCamera()
camera.resolution = (1920, 1080)
LOCATION = '/home/pi/temp.jpg'

ENDPOINT = "https://verk75.cognitiveservices.azure.com/"
KEY = ""
#client = ComputerVisionClient(ENDPOINT,CognitiveServicesCredentials(KEY))
analyze_url = ENDPOINT + "vision/v3.1/analyze" 

def capture(loc):
    print("Taking Picture")
    camera.capture(loc)

def analyze(loc):
    print("Analyzing image")
    image_data = open(loc, "rb").read()
    headers = {'Ocp-Apim-Subscription-Key': KEY,
            'Content-Type': 'application/octet-stream'}
    params = {'VisualFeatures': 'Categories,Description,Color'}
    response = requests.post(
            analyze_url, headers=headers, params=params, data=image_data)
    response.raise_for_status()
    analysis = response.json()
    
    print(analysis)
    image_caption = analysis["description"]["captions"][0]["text"].capitalize()
    print(image_caption)

capture(LOCATION)
analyze(LOCATION)
