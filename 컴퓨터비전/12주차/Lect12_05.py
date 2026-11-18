import cv2

image1 = cv2.imread('bright.jpg',cv2.IMREAD_GRAYSCALE)
image2 = image1.copy()

image2[0][0] = 2
image2[1][0] = 0
image2[2][0] = 2
image2[3][0] = 0

cv2.imshow("image1",image1)
cv2.imshow("image2",image2)
cv2.waitKey(0)