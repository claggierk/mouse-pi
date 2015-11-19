import picamera
import time

def main():
    print "Testing the ole camera out eh feo?"
    camera = picamera.PiCamera()

    camera.sharpness = 0
    camera.contrast = 0
    camera.brightness = 50
    camera.saturation = 0
    camera.ISO = 0
    camera.video_stabilization = False
    camera.exposure_compensation = 0
    camera.exposure_mode = 'auto'
    camera.meter_mode = 'average'
    camera.awb_mode = 'auto'
    camera.image_effect = 'none'
    camera.color_effects = None
    camera.rotation = 0
    camera.hflip = False
    camera.vflip = False
    camera.crop = (0.0, 0.0, 1.0, 1.0)

    #camera.capture('image2.jpg')
    camera.start_preview()
    time.sleep(10)
    camera.stop_preview()

if __name__ == "__main__":
    main()
