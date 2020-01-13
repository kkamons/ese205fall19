
from picamera import PiCamera
from time import sleep

camera = PiCamera()

sleep(1)
camera.capture('test.png')
sleep(4)
camera.resolution = (300,200)
camera.capture('testing.png')
