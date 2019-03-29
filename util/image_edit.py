import cv2
import numpy


def image_resize(image, height, width):
    size = (int(height), int(width))
    img = cv2.resize(image, size, interpolation=cv2.INTER_CUBIC)
    return img


def rgb2gray(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return img


def rgb2hsv(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return img


def hsv2rgb(image):
    img = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
    return img


def _edit_lightness(image, ratio):
    for i in range(image[:, :, 2].shape[0]):
        for j in range(image[:, :, 2].shape[1]):
            lightness = image[:, :, 2][i][j]
            lightness = lightness * ratio
            if lightness > 255:
                image[:, :, 2][i][j] = 255
            else:
                image[:, :, 2][i][j] = lightness
    return image


def get_image_size(image):
    height = image.shape[0]
    width = image.shape[1]
    color = image.shape[2]
    return height, width, color


if __name__ == '__main__':
    print("image_edit")
