import RPi.GPIO as GPIO
from time import sleep

BUTTON_PIN = 17
button_value = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)

try:
    while True:
        inputValue = GPIO.input(BUTTON_PIN)
        if inputValue != button_value:
            button_value = inputValue
            print('Button value is {}'.format(button_value))
except(KeyboardInterrupt):
    print('End')
    GPIO.cleanup()
