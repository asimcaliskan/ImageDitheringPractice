import numpy as np
def FloydSteinberg(img, q):
    image = np.copy(img)
    height, width = image.shape
    for row in range(height - 1):
        for column in range(width -1):
            oldPixel = image[row, column]
            newPixel = round( image[row, column] / (256 / q)) * (256 / q)
            image[row, column] = newPixel
            quantizationError = oldPixel - newPixel
            image[row][column + 1] = image[row ][column + 1 ] + quantizationError * 7 / 16
            image[row + 1][column - 1] = image[row + 1][column - 1] + quantizationError * 3 / 16
            image[row + 1][column] = image[row + 1][column] + quantizationError * 5 / 16
            image[row + 1][column + 1] = image[row + 1][column + 1] + quantizationError * 1 / 16
    return image