import numpy as np
import cv2

image= cv2.imread("circuit.bmp")
template = cv2.imread("crystal.bmp")

w, h = template.shape[::-1][1:]

result = cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

cv2.rectangle(image, max_loc,
              (max_loc[0]+w, max_loc[1]+h),255,2)

cv2.imshow("result",result)
cv2.imshow("image",image)
cv2.waitKey(0)