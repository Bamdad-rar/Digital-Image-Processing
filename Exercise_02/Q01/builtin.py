import cv2
import numpy as np

img = cv2.imread('1.png',cv2.IMREAD_GRAYSCALE)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ))
cv2.imshow("result", res)
cv2.waitKey(0)


