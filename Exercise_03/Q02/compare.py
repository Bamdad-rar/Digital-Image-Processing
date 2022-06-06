from util import median_filter
from cv2 import imread,medianBlur
import cv2
from numpy import asarray
import numpy as np
from time import perf_counter


"""comparing opencv's median filter and my implementation """
# img = imread('1.jpg',0)
img = asarray(imread('1.jpg',0))

start = perf_counter()
my_filtered_img = median_filter(img, 3)
print(f"my median filter performance : {perf_counter()-start}")

start = perf_counter()
opencv_filtered_img = medianBlur(img, 3)
print(f"opencv median filter performance :{perf_counter()-start}")

final_img = np.concatenate([img,my_filtered_img,opencv_filtered_img], axis=1)

cv2.imshow('test', final_img)
cv2.waitKey(0)