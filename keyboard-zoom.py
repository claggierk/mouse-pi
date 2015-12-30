from subprocess import call
import picamera
import readchar
import time
import sys

globals = {
    'zoom_step'     : 0.01,

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

def main():
    initialize_camera()
    while True:
      keyboard_input = readchar.readchar()
      if keyboard_input == 'q':
         break
      elif keyboard_input == 'i':
         zoom_in()
      elif keyboard_input == 'o':
         zoom_out()

if __name__ == "__main__":
    main()
