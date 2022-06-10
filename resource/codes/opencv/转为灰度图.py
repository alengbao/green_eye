import cv2 as cv


def 转为灰度图(img, called=None):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return gray


call = 转为灰度图
