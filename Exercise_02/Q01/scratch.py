import cv2
import numpy as np
from matplotlib import pyplot as plt
import copy

# read image in grayscale
img = cv2.imread('1.png',cv2.IMREAD_GRAYSCALE)

hist,bins = np.histogram(img,256,[0,256])

cdf = np.cumsum(hist)
cdf_normalized = cdf * hist.max() / cdf.max()


plt.plot(cdf_normalized)
plt.hist(np.array(img).flatten(),256,[0,256])
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

# removing zeroes
cdf_m = np.ma.masked_equal(cdf,0)

# histogram equalization formula
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())

# bringing back the zeroes
cdf = np.ma.filled(cdf_m,0).astype('uint8')
img2 = cdf[img]

cv2.imshow("enhanced images", img2)
cv2.waitKey(0)
