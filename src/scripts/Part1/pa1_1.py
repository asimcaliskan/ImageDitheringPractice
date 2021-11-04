import cv2
from pa1_2 import FloydSteinberg 
import numpy as np

IMAGE_PATH = "C:\\Users\\MONSTER\\GitHub\\ImageDitheringPractice\\src\\DitheringImages\\grayscale.png"
ROUND_VALUE = 2


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
cv2.imshow("Quantized Image",roundedImage)
cv2.imshow("Dithered Image",ditheredImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

