from cv2 import imread
import cv2
from matplotlib import pyplot as plt
import copy
import numpy as np


# loading images
img_1 = imread("1.jpg")
img_2 = imread("2.jpg")
img_3 = imread("3.png")
img_4 = imread("4.jpg")


# 3x3 median filter
three_by_three_filtered_img_1 = cv2.medianBlur(img_1, 3)
three_by_three_filtered_img_2 = cv2.medianBlur(img_2, 3)
three_by_three_filtered_img_3 = cv2.medianBlur(img_3, 3)
three_by_three_filtered_img_4 = cv2.medianBlur(img_4, 3)

# 5x5 median filter
five_by_five_filtered_img_1 = cv2.medianBlur(img_1, 5)
five_by_five_filtered_img_2 = cv2.medianBlur(img_2, 5)
five_by_five_filtered_img_3 = cv2.medianBlur(img_3, 5)
five_by_five_filtered_img_4 = cv2.medianBlur(img_4, 5)

# 9x9 median filter

nine_by_nine_filtered_img_1 = cv2.medianBlur(img_1, 9)
nine_by_nine_filtered_img_2 = cv2.medianBlur(img_2, 9)
nine_by_nine_filtered_img_3 = cv2.medianBlur(img_3, 9)
nine_by_nine_filtered_img_4 = cv2.medianBlur(img_4, 9)


final_img_1 = np.concatenate(
    (
        img_1,
        three_by_three_filtered_img_1,
        five_by_five_filtered_img_1,
        nine_by_nine_filtered_img_1,
    ),
    axis=1,
)
final_img_2 = np.concatenate(
    (
        img_2,
        three_by_three_filtered_img_2,
        five_by_five_filtered_img_2,
        nine_by_nine_filtered_img_2,
    ),
    axis=1,
)
final_img_3 = np.concatenate(
    (
        img_3,
        three_by_three_filtered_img_3,
        five_by_five_filtered_img_3,
        nine_by_nine_filtered_img_3,
    ),
    axis=1,
)
final_img_4 = np.concatenate(
    (
        img_4,
        three_by_three_filtered_img_4,
        five_by_five_filtered_img_4,
        nine_by_nine_filtered_img_4,
    ),
    axis=1,
)

cv2.imshow("img 01", final_img_1)
cv2.waitKey(0)
cv2.imshow("img 02", final_img_2)
cv2.waitKey(0)
cv2.imshow("img 03", final_img_3)
cv2.waitKey(0)
cv2.imshow("img 04", final_img_4)
cv2.waitKey(0)
