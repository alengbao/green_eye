import cv2 as cv
import numpy as np


def 腐蚀(img, kernel, called=None):
    res = cv.erode(img, kernel, iterations=1)
    return res


call = 腐蚀
