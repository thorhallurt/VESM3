from mfrc522 import SimpleMFRC522
import gpiozero

reader = SimpleMFRC522()

ledA = gpiozero.LED(17)
ledB = gpiozero.LED(18)

print("Starting reader")
while True:
    try:
        id = 0
        id, text = reader.read()
        if id == 602217986175:
            ledA.on()
            ledB.off()
        elif id == 838901700084:
            ledB.on()
            ledA.off()
    except KeyboardInterrupt:
        ledA.off()
        ledB.off()
        break
