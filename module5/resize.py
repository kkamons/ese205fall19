import cv2
import numpy as np
import sys
import math

def resizeW(inImg,w):
    img = cv2.imread(inImg)
    x = img.shape[1]
    y = img.shape[0]

    newX = w
    newY = int((w/x)*y)

    smallImg = cv2.resize(img,(newY,newX))
    cv2.imwrite(inImg.split('.')[0]+'ResizedW.png',smallImg)

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
    cv2.imwrite(inImg.split('.')[0]+'Resized200.png',newImg)

def main():
    inImg = sys.argv[1]
    #w = int(sys.argv[2])
    newImg = resize200(inImg)


if __name__ == "__main__":
    main()
