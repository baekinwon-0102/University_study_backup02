import cv2
import numpy as np

img_BGR = cv2.imread('HSI.png')

if img_BGR is None:
    raise ValueError('Could not read the image!')

img_HSV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)
Hue, Saturation, Value = cv2.split(img_HSV)

lower_blue = (120-10,30,30)  # 파란색 각도의 +- 20도 사이 값만 가져옴 뒤에 SV는 최소, 최대 값
upper_blue = (120+10,255,255)

img_mask = cv2.inRange(img_HSV, lower_blue, upper_blue)
img_result = cv2.bitwise_and(img_BGR, img_BGR, mask=img_mask)

cv2.imshow('img', img_BGR)
cv2.imshow('img_mask',img_mask)
cv2.imshow('img_result', img_result)

cv2.waitKey(0)

# 여기서 시험 문제 나옴