import numpy as np
import cv2

def calculate_mean_and_standart_deviation(image):
	image_mean, image_std = cv2.meanStdDev(image)
	image_mean = np.hstack(np.around(image_mean, 3))
	image_std = np.hstack(np.around(image_std ,3))
    #image_mean : [mean_of_channel_1, mean_of_channel_2, mean_of_channel_3]
    #image_std : [std_of_channel_1, std_of_channel_2, std_of_channel_3]
	return image_mean, image_std

#0 =< image channel value =< 255
def pixel_boundary_check(pixel):
    if(pixel < 0): 
        return 0
    elif(pixel > 255):
        return 255
    else:
        return pixel

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
                pixel = round(pixel)
                pixel = pixel_boundary_check(pixel)
                source_image[row, column, channel] = pixel

    source_image = cv2.cvtColor(source_image, cv2.COLOR_LAB2BGR)
    cv2.imshow("RESULT IMAGE", source_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()