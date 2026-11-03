import numpy as np
import cv2

image = cv2.imread('hist_stretch.jpg')
title = 'hist'
if image is None:
    raise Exception("file error")
pt1 = (250,160)
pt2 = (480,360)
width = int(pt1[0] + (pt2[0]-pt1[0])/2)
height = int(pt1[1] + (pt2[1]-pt1[1])/2)
all = (width,height)
print(all)
cv2.rectangle(image, pt1,pt2,(0,0,255),3)
cv2.putText(image,f'{pt2[0]-pt1[0]} x {pt2[1]-pt1[1]}',(250,150),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0))
cv2.putText(image,'Cat',all,cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
cv2.imshow(title,image)
params_png = (cv2.IMWRITE_PNG_COMPRESSION,9)
cv2.imwrite('202363046_BIW_01.png',image,params_png)

cv2.waitKey(0)