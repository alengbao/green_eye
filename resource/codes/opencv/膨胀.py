import cv2 as cv


def 膨胀(img, kernel, called=None):
    res = cv.dilate(img, kernel, 1)
    return res


call = 膨胀
