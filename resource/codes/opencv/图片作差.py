import cv2


def 图片作差(img1, img2, called=None):
    try:
        res = img1 - img2
        return res
    except:
        return None


call = 图片作差
