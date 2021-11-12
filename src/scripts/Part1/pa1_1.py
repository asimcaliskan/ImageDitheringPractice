import cv2
from pa1_2 import FloydSteinberg 
import numpy as np

IMAGE_PATH = r"C:\Users\MONSTER\GitHub\ImageDitheringPractice\src\DitheringImages\dithering2.jpg"
ROUND_VALUE = 64


def roundImage(img):
    image = np.copy(img)
    height, width = image.shape
    for row in range(height):
        for column in range(width):
            image[row, column] = round( image[row, column] / (256 / ROUND_VALUE)) * (256/ROUND_VALUE)
    return image


image = cv2.imread(IMAGE_PATH)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert image to gray image
roundedImage = roundImage(image)
ditheredImage = FloydSteinberg(image, ROUND_VALUE)
cv2.imshow("\src\DitheringImages\normal_result.png",roundedImage)
cv2.imshow("\src\DitheringImages\dithered_result.png",ditheredImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

