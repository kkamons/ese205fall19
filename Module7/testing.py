from picamera import PiCamera
import picamera.array
import time
import cv2

t1 = time.time()
camera = PiCamera()
camera.framerate = 30
stream = picamera.array.PiRGBArray(camera)  # Create the stream

t2 = time.time()
camera.capture('testing1.png')         # Take & save large image

t3 = time.time()
camera.resolution = (320, 208)
camera.capture('testing2.png')         # Take & save smaller image

t4 = time.time()
camera.capture(stream, format='bgr')   # Save directly to memory
image = stream.array
stream.truncate(0)                     # needed to take another pic

t5 = time.time()
cv2.imwrite('testing3.png', image)     # Save the image from memory
t6 = time.time()

camera.capture(stream,format='bgr',use_video_port=True)
img = stream.array
stream.truncate(0)

t7 = time.time()
cv2.imwrite('testing4.png',img)
t8 = time.time()

print("setup object:  "+ str(t2-t1))
print("take and save p1:  "+ str(t3-t2))
print("take and save small picture:  "+ str(t4-t3))
print("take streamed image: " + str(t5-t4))
print("save streamd img: " + str(t6-t5))
print("take streamed img using video port: " + str(t7-t6))
print("save streamed img using video port: " + str(t8-t7))
