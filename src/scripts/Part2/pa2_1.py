from numpy.lib.utils import source
from pa2_2 import color_transfer
import cv2

SOURCE_IMAGE_PATH = "C:\\Users\\MONSTER\\GitHub\\ImageDitheringPractice\\exampleImages\\colortransfer\\ocean_day.jpg"
TARGET_IMAGE_PATH = "C:\\Users\\MONSTER\\GitHub\\ImageDitheringPractice\\exampleImages\\colortransfer\\autumn.jpg"

def read_image():
	source_image = cv2.imread(SOURCE_IMAGE_PATH)
	source_image = cv2.cvtColor(source_image,cv2.COLOR_BGR2LAB)
	target_image = cv2.imread(TARGET_IMAGE_PATH)
	target_image = cv2.cvtColor(target_image,cv2.COLOR_BGR2LAB)
	return source_image, target_image

source_image, target_image = read_image()

color_transfer(source_image, target_image)