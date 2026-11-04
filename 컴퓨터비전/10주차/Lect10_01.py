import numpy as np
import cv2

def filter(image,mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows,cols),np.float32)
    ycenter, xcenter = mask.shape[1]//2, mask.shape[0]//2

    for i in range(ycenter,rows-ycenter):
        for j in range(xcenter,cols-xcenter):
            sum = 0.0
            for u in range(mask.shape[0]):
                for v in range(mask.shape[1]):
                    y = i+u - ycenter
                    x = j+v - xcenter
                    sum += image[y,x] * mask[u,v]
            dst[i,j] = sum
    return dst
image = cv2.imread('filter_blur.jpg',cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("could not read the image")

data = [[1/9,1/9,1/9],
        [1/9,1/9,1/9],
        [1/9,1/9,1/9]]

mask = np.array(data, np.float32)
blur1 = filter(image,mask)
blur1 = cv2.convertScaleAbs(blur1)

cv2.imshow('image',image)
cv2.imshow('blur1',blur1)
cv2.waitKey(0)
cv2.destroyAllWindows()