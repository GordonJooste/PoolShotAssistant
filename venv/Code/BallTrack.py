# import the necessary packages
from collections import deque
import numpy as np
import argparse
import imutils
import cv2
import matplotlib.pyplot as plt
import time
import sys
#import Haar

# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-v", "--video",
#                help="path to the (optional) video file")
# ap.add_argument("-b", "--buffer", type=int, default=64,
#                help="max buffer size")
# args = vars(ap.parse_args())
# if a video path was not supplied, grab the reference
# to the webcam
# if not args.get("video", False):
#    camera = cv2.VideoCapture(0)

def tableDet(img):
    hGreen = 60
    lowerBound = np.array([hGreen - 20, 50, 40 - 27])
    upperBound = np.array([hGreen + 40, 255, 255])

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(imgHSV, lowerBound, upperBound)

    # cv2.imshow("mask",mask)
    # cv2.imshow("cam",img)
    # cv2.waitKey(5000)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    Emask = cv2.erode(mask, kernel, iterations=1)
    Emask = cv2.dilate(Emask, kernel, iterations=1)
    Dmask = cv2.erode(mask, kernel, iterations=1)
    # cv2.imshow("mask", mask)
    # cv2.imshow("mask", Emask)
    # cv2.waitKey(1)

    maskFinal = Emask
    idk, conts, h = cv2.findContours(maskFinal.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # cv2.drawContours(img, conts, -1, (255, 0, 0), 3)
    #print(len(conts))
    # for i in range(len(conts)):
    #    x, y, w, h=cv2.boundingRect(conts[i])
    #    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    #    #cv2.PutText(cv2.fromarray(img), str(i+1), (x, y+h), font, (0, 255, 255))

    if len(conts) != 0:
        # draw in blue the contours that were founded
        # cv2.drawContours(img, conts, -1, 255, 3)

        # find the biggest area
        c = max(conts, key=cv2.contourArea)

        x, y, w, h = cv2.boundingRect(c)
        # draw the book contour (in green)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # ROI!
        x1 = x + w;
        y1 = y + h
        #print(str(x) + ':' + str(y) + ' , ' + str(x1) + ':' + str(y1))

        # y : y + h , x : x + w
        table = imgHSV[y:y1, x:x1]

    # cv2.imshow("maskClose", maskClose)
    # cv2.imshow("maskOpen", maskOpen)
    # cv2.imshow("mask", maskFinal)
    # cv2.imshow("cam", img)
    # cv2.waitKey(1)

    return {'FMask': maskFinal, 'table': table, 'DMask': Dmask, 'y': y, 'y1': y1, 'x': x, 'x1': x1}
    # NEED TO SET LARGE CONTOUR TO ROI



# Ball
# Tracking
# with OpenCVPython

def circleDet(camera):
    (grabbed, frame) = camera.read()
    Itable = tableDet(frame)

    y = Itable['y']+40;y1 = Itable['y1']-40;x = Itable['x']+40;x1 = Itable['x1']-40

    # keep looping
    while True:
        # grab the current frame
        (grabbed, frame) = camera.read()

        # if we are viewing a video and we did not grab a frame,
        # then we have reached the end of the video
        # if args.get("video") and not grabbed:
        #     break

        # resize the frame, blur it, and convert it to the HSV
        # color space
        # frame = cv2.imread('p2.jpg')
        #frame = imutils.resize(frame, width=1080)
        #cv2.imshow("Frame", frame)
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)

        tableD = tableDet(frame)
        table = frame[y:y1, x:x1]
        mask = tableD['FMask']
        mask = mask[y:y1, x:x1]
        # construct a mask for the color "green", then perform
        # a series of dilations and erosions to remove any small
        # blobs left in the mask
        # mask = table['maskFinal']
        '''
        hGreen = 60
        lowerBound = np.array([hGreen - 27, 50, 40 - 27])
        upperBound = np.array([hGreen + 40, 255, 255])
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
        # Now mask the Table
        mask = cv2.inRange(table, lowerBound, upperBound)
        #Emask = cv2.erode(mask, kernel, iterations=1)
        #Emask = cv2.dilate(Emask, kernel, iterations=2)

        #mask = Emask
        # find contours in the mask and initialize the current
        # (x, y) center of the ball
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]q
        # cv2.drawContours(frameC, cnts, -1, (255, 0, 0), 3)
        #tableBGR = cv2.cvtColor(table, cv2.COLOR_HSV2BGR)
        '''
        # if(cimg.type() == (((0) & ((1 << 3) - 1)) + (((1)-1) << 3))):
        #    print('well shit')
        #    circlesA = np.uint16(0) '''
        # else:
        mask_inv = cv2.bitwise_not(mask)
        res = cv2.bitwise_and(table,table, mask=mask_inv)


        gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
        cv2.imshow('as', gray)
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 2, 68,
                                   param1=30,
                                   param2=15,
                                   minRadius=34,
                                   maxRadius=34)
        # Upper and lower bounds for white
        upperW = (103,151,132);lowerW =(91,110,130)
        tableH = tableD['table']
        if circles is not None:
            circlesA = np.uint16(np.around(circles))
            for i in circlesA[0, :]:
                print(tableH[i[1]+10, i[0]-10])
                #             x               y                Radius
                # print(str(i[0])+'    '+str(i[1])+'    '+str(i[2]))
                if np.all(tableH[i[1] + 10, i[0] - 10] <= upperW) and np.all(table[i[1] + 10, i[0]] - 10 >= lowerW):
                    # draw the outer circle
                    cv2.circle(table, (i[0], i[1]), i[2], (255, 0, 0), 2)
                    # draw the center of the circle
                    cv2.circle(table, (i[0], i[1]), 2, (0, 255, 0), 3)
                else:
                    # draw the outer circle
                    cv2.circle(table, (i[0], i[1]), i[2], (0, 255, 0), 2)
                    # draw the center of the circle
                    cv2.circle(table, (i[0], i[1]), 2, (0, 0, 255), 3)
        else:
            print('well fuck')
        # show the frame to our screen

        cv2.imshow('detected circles', table)

        key = cv2.waitKey(10000) & 0xFF

        # if the 'q' key is pressed, stop the loop
        if key == ord("q"):
            break

camera = cv2.VideoCapture("pvid2.mp4")
circleDet(camera)

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()