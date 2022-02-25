from picamera import PiCamera
from gpiozero import MotionSensor
from datetime import datetime
import os
import sys
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import time

COMMASPACE = ', '

def send_email(image, timestamp):
    sender = 'thorhallurtr21@tskoli.is'
    password = '' # Setja inn passord
    recipients = ['thorhallurtr21@tskoli.is']

    outer = MIMEMultipart()
    outer['Subject'] = 'image: %s' % timestamp
    outer['To'] = COMMASPACE.join(recipients)
    outer.preamble = "idk"

    attachments = [image]

    for file in attachments:
        try:
            with open(file, 'rb') as fp:
                msg = MIMEBase('application', "octet-stream")
                msg.set_payload(fp.read())
            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
            outer.attach(msg)
        except:
            print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
            raise

    composed = outer.as_string()

    try:
        with smtplib.SMTP('smtp.outlook.office365.com') as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(sender, password)
            s.sendmail(sender, recipients, composed)
            s.close()
        print("Email sent!")
    except:
        print("Unable to send email. Error: ", sys.exc_info()[0])
        raise

pir = MotionSensor(17)
camera = PiCamera()
camera.resolution = (1024, 768)

while True:
    pir.wait_for_motion()
    timestamp = datetime.now().isoformat()
    print("Taking picture %s" % timestamp)
    camera.capture('image_Time_{}.jpg'.format(timestamp))
    image = ('image_Time_{}.jpg'.format(timestamp))
    send_email(image, timestamp)
    pir.wait_for_no_motion()
    print("Motion stopped")


