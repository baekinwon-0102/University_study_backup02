import numpy as np
import cv2

def contain(p, shape):
    return 0 <= p[0] < shape[0] and 0 <= p[1] < shape[1]

def bilinear_value(img,pt):
    x,y = np.int32(pt)
    if x >= img.shape[1]-1:
        x = x-1
    if y >= img.shape[0]-1:
        y = y-1

    P1 = float(img[y,x])
    P2 = float(img[y,x+1])
    P3 = float(img[y+1,x])
    P4 = float(img[y+1,x+1])

    M1 = P1+(pt[1] - y) * (P3 - P1)
    M2 = P2+(pt[1] - y) * (P4 - P2)
    P = M1 + (pt[0]-x)*(M2 - M1)
    return np.clip(P,0,255)

def rotate(img, degree):
    dst = np.zeros(img.shape[:2], img.dtype)
    radian = (degree / 180) * np.pi
    sin, cos = np.sin(radian),np.cos(radian)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            y = -j * sin + i * cos
            x = j * cos + i * sin
            x = int(x)
            y = int(y)
            if contain((y,x), img.shape):
                dst[i,j] = bilinear_value(img,[x,y])
                # dst[i,j] = img[y,x]
    return dst

image = cv2.imread('rotate.jpg',cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 에러")
dst1 = rotate(image,20)

cv2.imshow('image',image)
cv2.imshow('dst1',dst1)
cv2.waitKey(0)
