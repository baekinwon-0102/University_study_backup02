import numpy as np
import cv2

image= cv2.imread("mario_game.png")
template = cv2.imread("coin.png")
template2 = cv2.imread("mario2.png")
template2_shape = template2.shape

template2_dst = cv2.resize(template2,(int(template2_shape[1]*0.5),int(template2_shape[0]*0.5)),0,0,cv2.INTER_LINEAR)

w, h = template.shape[::-1][1:]
w2,h2 = template2_dst.shape[::-1][1:]

result = cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED)
result2 = cv2.matchTemplate(image,template2_dst,cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result2)

threshold = 0.8
loc = np.where(result >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(image,pt,(pt[0]+w,pt[1]+h),(255,0,0),2)

cv2.rectangle(image,max_loc,(max_loc[0]+w2,max_loc[1]+h2),(0,255,0),2)

cv2.imshow("result",result)
cv2.imshow("image",image)
cv2.waitKey(0)