import cv2 as cv


def 转为二值图像(img, called=None):
    ret, binary = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
    return binary


call = 转为二值图像
