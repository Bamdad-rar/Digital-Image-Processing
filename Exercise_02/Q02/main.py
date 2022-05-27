import cv2
import numpy as np
import copy
from matplotlib import pyplot as plt
from utils import Mapper

# Read the image
img = cv2.imread("2.jpg", cv2.IMREAD_GRAYSCALE)

# blank image
stretched_img = np.zeros((img.shape[0], img.shape[1]), dtype="uint8")

img_min = np.min(img)
img_max = np.max(img)
cols = img.shape[0]
rows = img.shape[1]

mapper = Mapper(40, 80, 250, 235)

for i in range(cols):
    for j in range(rows):
        stretched_img[i, j] = mapper.transform(img[i, j])


plt.hist(np.array(img).flatten(), 256, [0, 256])
plt.savefig("h1.jpg")
plt.hist(np.array(stretched_img).flatten(), 256, [0, 256])
plt.savefig("h2.jpg")



res = np.hstack((img, stretched_img))
cv2.imshow("result", res)
cv2.imwrite("result.jpg", res)
cv2.waitKey(0)
