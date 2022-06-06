from numpy import median
from copy import deepcopy

"""
median filter from scratch
"""


def median_filter(image, kernel_size):
    # kernel size is the matrix that slides over the image pixels and applies the filter
    # for this function kernel_size must be an odd, positive integer.
    # when the kernel is at the borders it will ignore the pixels outside the image.
    # returns the modified image copy.
    radius = kernel_size // 2
    temp_image = deepcopy(image)
    for i, row in enumerate(image):
        for j, col in enumerate(row):
            # at each pixel, get all surrounding pixels, sort them, find the median and
            # replace the value of current pixel with median
            img_slice = image[
                i - radius if i - radius > 0 else 0 : i + radius + 1,
                j - radius if j - radius > 0 else 0 : j + radius + 1,
            ]

            temp_image[i, j] = median(img_slice)

    return temp_image
