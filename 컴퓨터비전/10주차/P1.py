import numpy as np
import cv2

image = cv2.imread('morph.jpg',cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("could not read the image")

gaus = cv2.GaussianBlur(image,(9,9),0,0)
dst = cv2.Laplacian(gaus,cv2.CV_16S,1)
dst = cv2.convertScaleAbs(dst)

cv2.imshow('image',image)
cv2.imshow('dst',dst)
cv2.waitKey(0)