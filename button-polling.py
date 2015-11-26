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
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    # GND to COM
    # G17 to NC (normally connected)
    pin_17 = GPIO.input(17)
    if pin_17 == True:
        print('GPIO #17 button pressed')
        time.sleep(0.2)

    # GND to COM
    # G18 to NO (normally open)
    pin_18 = GPIO.input(18)
    if pin_18 == False:
        print('GPIO #18 button pressed')
        time.sleep(0.2)

