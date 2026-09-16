import numpy as np
import cv2

def onChange(value):
    global image, title

    image[:] = value
    cv2.imshow(title,image)

def onMouse(event, x, y, flags, params):
    global image, bar_name

    if event == cv2.EVENT_LBUTTONDOWN:
        if(image[0][0] >= 10):
            image-= 10
        cv2.setTrackbarPos(bar_name,title, image[0][0])
        cv2.imshow(title,image)
    if event == cv2.EVENT_RBUTTONDOWN:
        if(image[0][0] < 246 ):
            image += 10
        cv2.setTrackbarPos(bar_name,title,image[0][0])
        cv2.imshow(title,image)

image = np.zeros((480,640), np.uint8)
title = "Trackbar"

cv2.imshow(title,image)
bar_name = 'Brightness'
cv2.createTrackbar(bar_name,title, image[0][0], 255, onChange)
cv2.setMouseCallback(title,onMouse)
while True:
    key = cv2.waitKeyEx(100) # 키보드 입력 값 반환

    if key == ord('q'): # q를 아스키 코드로 변환
        break
    elif key == ord('Q'):
        break
    elif key == 2424832:
        if (image[0][0] >= 10):
            image -= 10
        cv2.setTrackbarPos(bar_name, title, image[0][0])
        cv2.imshow(title, image)
    elif key == 2555904:
        if (image[0][0] < 246):
            image += 10
        cv2.setTrackbarPos(bar_name, title, image[0][0])
        cv2.imshow(title, image)

cv2.destroyAllWindows()