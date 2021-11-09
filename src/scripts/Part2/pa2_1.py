from pa2_2 import color_transfer
import cv2
from PIL import Image 
import numpy as np
import math

SOURCE_IMAGE_PATH = "C:\\Users\\MONSTER\\GitHub\\ImageDitheringPractice\\exampleImages\\colortransfer\\ocean_day.jpg"
TARGET_IMAGE_PATH = "C:\\Users\\MONSTER\\GitHub\\ImageDitheringPractice\\exampleImages\\colortransfer\\ocean_sunset.jpg"


def RGB2LMS(image):
	converter_matrix = np.array( [[0.3811, 0.5783, 0.0402], [0.1967, 0.7244, 0.0782], [0.0241, 0.1288, 0.844]])
	height, width, channel = image.shape
	for row in range(height):
		for column in range(width):
			image[row][column] = np.matmul(converter_matrix, image[row, column])

def LMS2LAB(image):
	matrix_1 = np.array(
		[[1, 1, 1],
		[1, 1, -2],
		[1, -1, 0]])
	matrix_2 = np.array(
		[[1/math.sqrt(3), 0, 0],
		[0, 1/math.sqrt(6), 0],
		[0, 0, 1/math.sqrt(2)]])
	converter_matrix = np.matmul(matrix_2, matrix_1)
	height, width, channel = image.shape
	for row in range(height):
		for column in range(width):
			image[row][column] = np.matmul(converter_matrix, image[row, column])

def LMS2LOG10LMS(image):
	height, width, channel = image.shape
	for row in range(height):
		for column in range(width):
			for chnnl in range(channel):
				if image[row][column][chnnl] > 0.: 
					image[row][column][chnnl] = np.log10(image[row][column][chnnl])


def read_image():
	source_image = Image.open(SOURCE_IMAGE_PATH)
	source_image = np.array(source_image)
	source_image = source_image.astype(float)
	RGB2LMS(source_image)
	LMS2LOG10LMS(source_image)
	LMS2LAB(source_image)
	target_image = Image.open(TARGET_IMAGE_PATH)
	target_image = np.array(target_image)
	target_image = target_image.astype(float)
	RGB2LMS(target_image)
	LMS2LOG10LMS(target_image)
	LMS2LAB(target_image)
	return source_image, target_image


source_image, target_image = read_image()
color_transfer(source_image, target_image)