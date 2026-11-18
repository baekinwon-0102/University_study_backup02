import cv2
import numpy as np

image1 = cv2.imread("original.png",cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('code.png',cv2.IMREAD_GRAYSCALE)

image_cv = cv2.subtract(image1, image2)
image_np = image1 - image2
nnZ = cv2.findNonZero(image_np)

print('CODE : ',)
for xy in nnZ:
    xy = xy[0]
    print(chr(image2[xy[1]][xy[0]]), end='')

cv2.imshow('image1',image1)
cv2.imshow('image2',image2)
cv2.waitKey(0)