import numpy as np
import cv2

image = cv2.imread('laplacian.jpg',cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("could not read the image")

gaus = cv2.GaussianBlur(image,(3,3),0,0)
dst1 = cv2.Laplacian(gaus,cv2.CV_16S,1)
dst1 = cv2.convertScaleAbs(dst1)

gaus2 = cv2.GaussianBlur(image,(9,9),0,0)
dst2 = cv2.Laplacian(gaus2,cv2.CV_16S,1)
dst2 = cv2.convertScaleAbs(dst2)

dst3 = cv2.Laplacian(image,cv2.CV_16S,1)
dst3 = cv2.convertScaleAbs(dst3)

cv2.imshow('image',image)
cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)
cv2.imshow('dst3',dst3)
cv2.waitKey(0)