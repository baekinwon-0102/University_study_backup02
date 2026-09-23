import numpy as np
import cv2


image = cv2.imread('color.jpg')

if image is None:
    raise Exception("Can't read the image")

bgr = cv2.split(image)

# cv2.subtract(bgr[0],100,bgr[0]) #블루채널 색상 100만큼 빼기
# cv2.add(bgr[0],100,bgr[0])
cv2.subtract(bgr[1],254,bgr[1])
cv2.subtract(bgr[2],254,bgr[2])
merge_bgr = cv2.merge([bgr[0],bgr[1],bgr[2]])

cv2.imshow('image',image)
cv2.imshow('blue channel',bgr[0])
cv2.imshow('green channel',bgr[1])
cv2.imshow('red channel',bgr[2])
cv2.imshow('merge channel',merge_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()