# http://razzpisampler.oreilly.com/ch07.html
# sudo python switch.py

import RPi.GPIO as GPIO
import time

# set mode to broadcom to get their naming conventions of the GPIO pins
GPIO.setmode(GPIO.BCM)

# PIN #: number
# input/output: GPIO.IN vs GPIO.OUT
# pull_up_down: GPIO.PUD_UP vs GPIO.PUD_DOWN
# PUD = Pull Up Down
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)
