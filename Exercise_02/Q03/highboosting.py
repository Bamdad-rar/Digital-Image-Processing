import cv2

# Load the image
image = cv2.imread("3.jpg")
# Blur the image
cv2.imshow("original",image)
cv2.waitKey(0)

gauss = cv2.GaussianBlur(image, (7,7), 0)

cv2.imshow("gauss",gauss)
cv2.waitKey(0)
# Apply Unsharp masking
unsharp_image = cv2.addWeighted(image, 2, gauss, -1, 0)

cv2.imshow("unsharp",unsharp_image)
cv2.waitKey(0)
