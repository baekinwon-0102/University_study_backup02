import numpy as np
import cv2

image = cv2.imread("bit_test.jpg")
logo = cv2.imread("logo.jpg")

logo_thr = cv2.threshold(logo, 50, 255, cv2.THRESH_BINARY)[1]
logo_split = cv2.split(logo_thr)
cv2.imshow("logo_split[0]", logo_split[0])
cv2.imshow("logo_split[1]", logo_split[1])
cv2.imshow("logo_split[2]", logo_split[2])
pass_mask = cv2.bitwise_or(logo_split[1], logo_split[2])
cv2.imshow("pass_mask1", pass_mask)
# pass_mask = cv2.bitwise_or(logo_split[2], pass_mask)
cv2.imshow("pass_mask2", pass_mask)
pass_mask = cv2.bitwise_not(pass_mask)
cv2.imshow("pass_mask3", pass_mask)

h = logo.shape[0]
w = logo.shape[1]
roi = image[:h, :w]
cv2.imshow("logo", logo)
cv2.imshow("roi", roi)

background = cv2.bitwise_and(roi, roi, mask=pass_mask)
roi_merge = cv2.add(background, logo)
image[:h, :w] = roi_merge
cv2.imshow("background", background)
cv2.imshow("roi_merge", roi_merge)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()