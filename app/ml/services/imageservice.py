import cv2

IMG_SIZE = 240


def resize_image(image):
    return cv2.resize(image, (IMG_SIZE, IMG_SIZE))
