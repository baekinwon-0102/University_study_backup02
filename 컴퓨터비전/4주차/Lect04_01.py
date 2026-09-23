import numpy as np
import cv2

title1 = 'gray2gray'
title2 = 'gray2color'

gray2gray = cv2.imread("read_color.jpg",cv2.IMREAD_GRAYSCALE)
gray2color = cv2.imread("read_color.jpg",cv2.IMREAD_COLOR)

if gray2gray is None or gray2color is None:
    raise Exception("read error")

print("pixel value: [100, 100]")
print("title1: ", gray2gray[100,100])
print("title2: ", gray2color[100,100])

cv2.imshow(title1,gray2gray)
cv2.imshow(title2,gray2color)
cv2.waitKey(0)
cv2.destroyAllWindows()