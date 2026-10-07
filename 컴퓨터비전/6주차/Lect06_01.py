import cv2
import numpy as np

def onThreshold(value):
    th[0] = cv2.getTrackbarPos("Blue_min","result")
    th[1] = cv2.getTrackbarPos("Blue_max","result")

    # _, result = cv2.threshold(B, th[1], 255, cv2.THRESH_TOZERO_INV)
    _, result = cv2.threshold(hue,th[1],255,cv2.THRESH_TOZERO_INV)
    cv2.threshold(result,th[0],255,cv2.THRESH_BINARY,result)
    cv2.imshow('result',result)

img_BGR = cv2.imread('color_space.jpg')

if img_BGR is None:
    raise ValueError('Could not read the image!')

img_HSV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)
# Hue, Saturation, Value = cv2.split(img_HSV)

# B = np.copy(img_BGR[:,:,0])
hue = np.copy(img_HSV[:,:,0])
th = [0,0]

cv2.imshow('img_BGR', img_BGR)
cv2.namedWindow('result')
cv2.createTrackbar("Blue_min","result",th[0],255,onThreshold)
cv2.createTrackbar("Blue_max","result",th[1],255,onThreshold)
onThreshold(th[0])

# cv2.imshow('img', img_BGR)
# cv2.imshow('Hue', Hue)
# cv2.imshow('Saturation', Saturation)
# cv2.imshow('Value', Value)

cv2.waitKey(0)