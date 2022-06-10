import cv2


def 展示图片(image, called=None):
    print('show image')
    if image is None:
        print('图片为空')
    cv2.imshow("image", image)
    cv2.waitKey(0)
    return image


call = 展示图片
