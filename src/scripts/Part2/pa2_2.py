import numpy as np
import cv2
import math
from PIL import Image
def LMS2RGB(image):
	converter_matrix = np.array( [[4.4679, -3.5783, 0.1193], [-1.2186, 2.3809, -0.1624], [0.0497, -0.2439, 1.2045]])
	height, width, channel = image.shape
	for row in range(height):
		for column in range(width):
			image[row][column] = np.matmul(converter_matrix, image[row, column])

def LAB2LMS(image):
	matrix_1 = np.array(
		[[1, 1, 1],
		[1, 1, -1],
		[1, -2, 0]])
	matrix_2 = np.array(
		[[1/math.sqrt(3), 0, 0],
		[0, 1/math.sqrt(6), 0],
		[0, 0, 1/math.sqrt(2)]])
	converter_matrix = np.matmul(matrix_1, matrix_2)
	height, width, channel = image.shape
	for row in range(height):
		for column in range(width):
			image[row][column] = np.matmul(converter_matrix, image[row, column])

def LOG10LMS2LMS(image):
	height, width, channel = image.shape
	for row in range(height):
		for column in range(width):
				image[row][column] = np.power(10, image[row][column])


def calculate_mean_and_standart_deviation(image):
	image_mean, image_std = cv2.meanStdDev(image)
	image_mean = np.hstack(image_mean)
	image_std = np.hstack(image_std)
    #image_mean : [mean_of_channel_1, mean_of_channel_2, mean_of_channel_3]
    #image_std : [std_of_channel_1, std_of_channel_2, std_of_channel_3]
	return image_mean, image_std

#0 =< image channel value =< 255
def pixel_boundary_check(image):
	height, width, channel = image.shape
	for row in range(height):
		for column in range(width):
			for chnnl in range(channel):
				if(image[row][column][chnnl] < 0): 
					image[row][column][chnnl] = 0
				elif(image[row][column][chnnl] > 255):
					image[row][column][chnnl] = 255


def color_transfer(source_image, target_image):
	source_image_mean, source_image_std = calculate_mean_and_standart_deviation(source_image)
	target_image_mean, target_image_std = calculate_mean_and_standart_deviation(target_image)

	source_image_height, source_image_width, source_image_channel = source_image.shape
	for row in range(0,source_image_height):
		for column in range(0,source_image_width):
			for channel in range(0,source_image_channel):
				pixel = source_image[row, column, channel]
                #step 5, 6 and 7 on the paper
                #l'" = (var_lt/var_ls).(l − mean_ls) + mean_lt
                #α'" = (var_αt/var_αs).(α − mean_αs) + mean_αt
                #β'" = (var_βt/var_βs).(β − mean_βs) + mean_βt
				pixel = ((target_image_std[channel] / source_image_std[channel]) * (pixel - source_image_mean[channel])) + target_image_mean[channel]
				source_image[row, column, channel] = pixel

	#source_image = cv2.cvtColor(source_image, cv2.COLOR_LAB2RGB)
	LAB2LMS(source_image)
	LOG10LMS2LMS(source_image)
	LMS2RGB(source_image)
	pixel_boundary_check(source_image)
	source_image = source_image.astype(np.uint8)
	source_image = Image.fromarray(source_image)
	source_image.show()