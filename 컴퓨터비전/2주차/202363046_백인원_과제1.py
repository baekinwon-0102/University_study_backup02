import numpy as np
import cv2

image = np.zeros((240, 320), np.uint8)

title1,title2,title3 = 'A','B','C'

cv2.namedWindow(title1)
cv2.namedWindow(title2)
cv2.namedWindow(title3)

cv2.moveWindow(title1, 150, 150)
cv2.moveWindow(title2, 470, 150)
cv2.moveWindow(title3, 150, 380)

cv2.imshow(title1, image)
cv2.imshow(title2, image)
cv2.imshow(title3, image)
cv2.waitKey(0) # 키 입력을 기다림
cv2.destroyAllWindows()

