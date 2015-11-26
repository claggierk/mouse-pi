# Import the modules to send commands to the system and access GPIO pins
from subprocess import call
import RPi.GPIO as GPIO

def button_pressed_21(pin):
    print "pin:", pin

def configure_button_listeners():
    # set mode to broadcom to get their naming conventions of the GPIO pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # GPIO.RISING
    # GPIO.FALLING
    # GPIO.BOTH
    GPIO.add_event_detect(21, GPIO.FALLING, callback=button_pressed_21, bouncetime=200) # Set up an interrupt to look for button presses

def main():
    configure_button_listeners()
    raw_input() # Run the loop function to keep script running

if __name__ == "__main__":
    main()

