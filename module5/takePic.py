from picamera import PiCamera
from time import sleep
import cv2
import sys

def resize200(inImg):
    img = cv2.imread(inImg)
    x = img.shape[1]
    y= img.shape[0]
    if(x>y):
        newY = int((200/x)*y)
        newX=200
    else:
        newY = 200
        newX = int((200/y)*x)
    newImg = cv2.resize(img, (newX,newY),interpolation = cv2.INTER_AREA)
    cv2.imwrite(inImg.split('.')[0]+'_thmb.jpg',newImg)


def main():
    camera = PiCamera()

    sleep(1)
    camera.capture(sys.argv[1]+'.jpg')
#   sleep(5)
#    resize200(sys.argv[1]+'.jpg')

if __name__ == "__main__":
    main()

