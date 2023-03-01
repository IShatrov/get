import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)

while True:
    GPIO.output(22, 1)
    time.sleep(0.5)
    GPIO.output(22, 0)
    time.sleep(0.5)