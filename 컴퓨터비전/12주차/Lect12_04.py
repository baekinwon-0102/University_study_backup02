import numpy as np
import cv2

image = np.zeros((20,20), np.uint8)
image0 = np.zeros((20,20), np.uint8)
image1 = np.zeros((20,20), np.uint8)
image2 = np.zeros((20,20), np.uint8)

image[9][9]=255
cv2.circle(image0,(9,9),0,255,1)
cv2.circle(image1,(9,9),1,255,1)
cv2.circle(image2,(9,9),2,255,1)

cv2.imshow("image1",image1)
cv2.imshow("image2",image2)

cv2.waitKey(0)