from subprocess import call
import RPi.GPIO as GPIO
import picamera
import time
import sys

globals = {
    'zoom_step'     : 0.03,

    'zoom_xy_min'   : 0.0,
    'zoom_xy'       : 0.0,
    'zoom_xy_max'   : 0.4,

    'zoom_wh_min'   : 1.0,
    'zoom_wh'       : 1.0,
    'zoom_wh_max'   : 0.2
}

camera = picamera.PiCamera()

pin_17 = False
pin_18 = False

def initialize_camera():
    camera.sharpness = 0
    camera.contrast = 0
    camera.brightness = 50
    camera.saturation = 0
    camera.ISO = 0
    camera.video_stabilization = True
    camera.exposure_compensation = 0
    camera.exposure_mode = 'auto'
    camera.meter_mode = 'average'
    camera.awb_mode = 'auto'
    camera.image_effect = 'none'
    camera.color_effects = None
    camera.rotation = 0
    camera.hflip = False
    camera.vflip = False

    # (x, y, w, h)
    set_min_zoom()
    camera.start_preview()
    print "Camera is configured and outputting video..."

def update_zoom():
    #print "Setting camera to (%s, %s, %s, %s)" % (globals['zoom_xy'], globals['zoom_xy'], globals['zoom_wh'], globals['zoom_wh'])
    camera.zoom = (globals['zoom_xy'], globals['zoom_xy'], globals['zoom_wh'], globals['zoom_wh'])
    print "Camera at (x, y, w, h) = ", camera.zoom

def set_min_zoom():
    globals['zoom_xy'] = globals['zoom_xy_min']
    globals['zoom_wh'] = globals['zoom_wh_min']

def set_max_zoom():
    globals['zoom_xy'] = globals['zoom_xy_max']
    globals['zoom_wh'] = globals['zoom_wh_max']

def zoom_out():
    if globals['zoom_xy'] - globals['zoom_step'] < globals['zoom_xy_min']:
        set_min_zoom()
    else:
        globals['zoom_xy'] -= globals['zoom_step']
        globals['zoom_wh'] += (globals['zoom_step'] * 2)
    update_zoom()

def zoom_in():
    if globals['zoom_xy'] + globals['zoom_step'] > globals['zoom_xy_max']:
        set_max_zoom()
    else:
        globals['zoom_xy'] += globals['zoom_step']
        globals['zoom_wh'] -= (globals['zoom_step'] * 2)
    update_zoom()

def button_pressed_21(pin):
    print "Exiting..."
    camera.stop_preview()
    sys.exit(0)

def button_pressed_17(pin):
    global pin_17
    print "pin:", pin
    zoom_in()
    #print "pin_17", pin_17
    #while pin_17 == True:
    #    print('GPIO #17 button pressed')
    #    time.sleep(0.2)

def button_pressed_18(pin):
    global pin_18
    print "pin:", pin
    zoom_out()
    #print "pin_18", pin_18
    #while pin_17 == True:
    #    print('GPIO #18 button pressed')
    #    time.sleep(0.2)

def configure_button_listeners():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    pin_17 = GPIO.input(17)
    pin_18 = GPIO.input(18)

    # GPIO.RISING
    # GPIO.FALLING
    # GPIO.BOTH
    GPIO.add_event_detect(17, GPIO.FALLING, callback=button_pressed_17, bouncetime=200)
    GPIO.add_event_detect(18, GPIO.FALLING, callback=button_pressed_18, bouncetime=200)
    GPIO.add_event_detect(21, GPIO.FALLING, callback=button_pressed_21, bouncetime=200)

    print "Button Listeners are configured and listening..."

def main():
    configure_button_listeners()
    initialize_camera()
    raw_input() # Run the loop function to keep script running

if __name__ == "__main__":
    main()
