# import the necessary packages
from collections import deque
import numpy as np
import argparse
import imutils
import cv2
from scipy import misc
import matplotlib.pyplot as plt # import
import matplotlib

# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-v", "--video",
#                help="path to the (optional) video file")
#ap.add_argument("-b", "--buffer", type=int, default=64,
#                help="max buffer size")
#args = vars(ap.parse_args())

# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points

#HSV Green Hue is 120, OpenCV Green Hue is 60 (1/2)




#pts = deque(maxlen=args["buffer"])

img = cv2.imread('p2.jpg')
#maybe dont need to   img=cv2.resize(img,(340,220))

def tableDet(img):
    hGreen = 60
    lowerBound = np.array([hGreen - 27, 50, 40 - 27])
    upperBound = np.array([hGreen + 40, 255, 255])

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(imgHSV, lowerBound, upperBound)

    # cv2.imshow("mask",mask)
    # cv2.imshow("cam",img)
    # cv2.waitKey(5000)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    Emask = cv2.erode(mask, kernel, iterations=1)
    Emask = cv2.dilate(Emask, kernel, iterations=2)
    # cv2.imshow("mask", mask)
    # cv2.imshow("mask", Emask)
    # cv2.waitKey(1)

    maskFinal = Emask
    imgC = img
    idk, conts, h = cv2.findContours(maskFinal.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #cv2.drawContours(img, conts, -1, (255, 0, 0), 3)
    print(len(conts))
    #for i in range(len(conts)):
    #    x, y, w, h = cv2.boundingRect(conts[i])
    #    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        # cv2.PutText(cv2.fromarray(img), str(i+1), (x, y+h), font, (0, 255, 255))


    # draw in blue the contours that were founded
    #cv2.drawContours(img, conts, -1, 255, 3)

    # find the biggest area
    c = max(conts, key=cv2.contourArea)

    x, y, w, h = cv2.boundingRect(c)
    # draw the book contour (in green)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # ROI!
    x1 = x+w; y1 = y+h
    print(str(x)+ ':'+str(y)+' , '+str(x1)+':'+str(y1))


    # y : y + h , x : x + w
    table = img[y:y1, x:x1]

    '''
    for rownum in range(len(img)):
        for colnum in range(len(img[rownum])):
            if(colnum <= x and colnum >= x+w and rownum <= y and rownum >= y+h):
                print(str(img[rownum][colnum]))
                img[rownum][colnum] = [0,0,0]
                print(str(img[rownum][colnum]))
                print()
    '''
    # cv2.imshow("maskClose", maskClose)
    # cv2.imshow("maskOpen", maskOpen)
    cv2.imshow("mask", maskFinal)
    cv2.imshow("img", img)
    cv2.imshow("table", table)
    cv2.waitKey(5000)

    return {'maskFinal': maskFinal, 'contImg': img, 'orgMask': mask}
    # NEED TO SET LARGE CONTOUR TO ROI
    # Set everything outside the large contour to black




tableDet(img)



