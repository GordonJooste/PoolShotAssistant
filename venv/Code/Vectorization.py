import cv2
import numpy as np
import matplotlib.pyplot as plt # import
import matplotlib.cm

def sumproducts(x, y):

    result = 0
    for i in range(len(x)):
        for j in range(len(y)):
            result += x[i] * y[j]
    return result

def sumproductsVec(x, y):
    result = 0
    result = np.sum(x) * np.sum(y)
    return result
"""Return the sum of x[i] * y[j] for all pairs of indices i, j.

    >>> sumproducts(np.arange(3000), np.arange(3000))
    20236502250000

"""
print(sumproducts(np.arange(100), np.arange(100)))
print(sumproductsVec(np.arange(100), np.arange(100)))

def countlower(x, y):

    result = 0
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] < y[j]:
                result += 1
    return result

def countlowerVec(x,y):
    result = 0

    result = np.sum(np.searchsorted(np.sort(x), y))

    return result


"""Return the number of pairs i, j such that x[i] < y[j].

    >>> countlower(np.arange(0, 200, 2), np.arange(40, 140))
    4500

    """
print(countlower(np.arange(0, 200, 2), np.arange(40, 140)))
print(countlowerVec(np.arange(0, 200, 2), np.arange(40, 140)))
