from scipy import misc
import numpy as np
import matplotlib.pyplot as plt # import
import matplotlib.cm


image = misc.imread('S13.jpg')

plt.imshow(image) #load
plt.show()  # show the window

def weightedAverage(pixel):
    return 0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2]

grey = np.zeros((image.shape[0], image.shape[1])) # init 2D numpy array
# get row number
for rownum in range(len(image)):
   for colnum in range(len(image[rownum])):
      grey[rownum][colnum] = weightedAverage(image[rownum][colnum])

plt.imshow(grey, cmap = matplotlib.cm.Greys_r)
plt.show()