import cv2
import numpy as np
import sys


def findAngle(inImg):
    img = cv2.imread(inImg)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # lower and upper limits for the color red
    mask1 = cv2.inRange(hsv, (0,50,50),(10,255,255))
    mask2 = cv2.inRange(hsv,(170,50,50),(180,255,255))
    # notice that there are 2 ranges for red on HSV
    mask = mask1+mask2
    
    #use mask to find threshold
    M = cv2.moments(mask)
    # find the center
    cX = int(M['m10'] / M['m00'])
    cY = int(M['m01'] / M['m00'])

    mask = cv2.blur(mask,(5,5))
    thresh = cv2.threshold(mask,200,255,cv2.THRESH_BINARY)[1]

    # use threshold
    M = cv2.moments(thresh)
    cX = int(M['m10'] / M['m00'])
    cY = int(M['m01'] / M['m00'])
    cv2.circle(img,(cX,cY),5,(0,255,0))
    cv2.imwrite(inImg.split('.')[0]+'_thresh.png',thresh)
    
    angle = np.arctan2(cX-int(img.shape[1]/2),img.shape[0]-cY)*(180/np.pi)
    return angle

def main():

    inImg = sys.argv[1]
    angle = findAngle(inImg)
    print(angle)

if __name__ == "__main__":
    main()
