import cv2
import numpy as np

image1 = cv2.imread("bright.jpg",cv2.IMREAD_GRAYSCALE)
image2 = image1.copy()

image2[10][10] = ord('B')
image2[20][20] = ord('I')
image2[30][30] = ord('W')

print('CODE : ',
      chr(image2[10][10]),
      chr(image2[20][20]),
      chr(image2[30][30]))

image_cv = cv2.subtract(image1, image2)
image_np = image1 - image2
nnZ = cv2.findNonZero(image_np)
print(nnZ)

print('CODE : ',)
for xy in nnZ:
    xy = xy[0]
    print(xy, chr(image2[xy[1]][xy[0]]))

cv2.imshow('image1',image1)
cv2.imshow('image2',image2)
cv2.waitKey(0)