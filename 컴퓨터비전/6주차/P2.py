import cv2
import numpy as np

def onThreshold(value):
    th[0] = cv2.getTrackbarPos("Hue_min","result")
    th[1] = cv2.getTrackbarPos("Hue_max","result")
    th_v[0] = cv2.getTrackbarPos("V_min", "result")
    th_v[1] = cv2.getTrackbarPos("V_max", "result")

    _, result1 = cv2.threshold(hue,th[1],255,cv2.THRESH_TOZERO_INV)
    cv2.threshold(result1,th[0],255,cv2.THRESH_BINARY,result1)
    _, result2 = cv2.threshold(va, th_v[1], 255, cv2.THRESH_TOZERO_INV)
    cv2.threshold(result2, th_v[0], 255, cv2.THRESH_BINARY, result2)
    result = cv2.bitwise_and(result1,result2)
    cv2.imshow('result',result)

img_BGR = cv2.imread('fruit.png')

if img_BGR is None:
    raise ValueError('Could not read the image!')

img_HSV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)

hue = np.copy(img_HSV[:,:,0])
va = np.copy(img_HSV[:,:,2])
th = [0,0]
th_v = [0,0]

cv2.namedWindow('result')
cv2.createTrackbar("Hue_min","result",th[0],255,onThreshold)
cv2.createTrackbar("Hue_max","result",th[1],255,onThreshold)
cv2.createTrackbar("V_min","result",th_v[0],255,onThreshold)
cv2.createTrackbar("V_max","result",th_v[1],255,onThreshold)
onThreshold(th[0])

cv2.waitKey(0)