import cv2
import numpy as np
import matplotlib.pyplot as plt # import
import matplotlib.cm


# define the upper and lower boundaries of the HSV pixel
# intensities to be considered 'skin'
lower = np.array([0, 48, 80], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")
camera = cv2.VideoCapture(0)
#image = cv2.imread('s13.jpg',0)
# keep looping over the frames in the video
while True:
    # grab the current frame
    (grabbed, frame) = camera.read()

    # if we are viewing a video and we did not grab a
    # frame, then we have reached the end of the video
    converted = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    skinMask = cv2.inRange(converted, lower, upper)

    # apply a series of erosions and dilations to the mask
    # using an elliptical kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    skinMask = cv2.erode(skinMask, kernel, iterations=2)
    skinMask = cv2.dilate(skinMask, kernel, iterations=2)

    # blur the mask to help remove noise, then apply the
    # mask to the frame
    skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
    skin = cv2.bitwise_and(frame, frame, mask=skinMask)

    # show the skin in the image along with the mask
    cv2.imshow("images", np.hstack([frame, skin]))
    cv2.imshow('img',skinMask)

    # if the 'q' key is pressed, stop the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


camera.release()
cv2.destroyAllWindows()
#gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#th3 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,5)


#kernel = np.ones((5,5),np.uint8)
#erosion = cv2.erode(th3,kernel,iterations = 1)
#dilation = cv2.dilate(erosion,kernel,iterations = 1)
#opening = cv2.morphologyEx(th3, cv2.MORPH_OPEN, kernel)
#closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

#plt.imshow(dilation,cmap = matplotlib.cm.Greys_r) #load
#plt.imshow(opening,cmap = matplotlib.cm.Greys_r)
#plt.show()


