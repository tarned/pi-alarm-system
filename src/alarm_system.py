#!/usr/bin/python
##
# @file
# @author Denise Ratasich
# @date 22.03.2015
##

import logging
import sys
from motion_sensor import MotionSensor
from camera import CameraController

MOTION_SENSOR_PIN = 10

def callback():
    print 'test'

# set logging settings
root = logging.getLogger()
root.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(levelname)5s]: %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)

try:
    # test motion sensor class
    motion_sensor = MotionSensor(MOTION_SENSOR_PIN, callback)
    motion_sensor.start()
    logging.info('Make sure the motion sensor is connected to GPIO pin ' + 
		 str(MOTION_SENSOR_PIN) + '.')

    cam = CameraController()
    cam.capture()

except RuntimeWarning as e:
    logging.warn(e)
except Exception as e:
    logging.error(e)
    raise
except:
    logging.error('Unexpected error.')
    raise
