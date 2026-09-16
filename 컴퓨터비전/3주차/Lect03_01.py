import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Mouse Left Down Detected")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("Mouse Right Down Detected")
    elif event == cv2.EVENT_LBUTTONUP:
        print("Mouse Left Up Detected")
    elif event == cv2.EVENT_RBUTTONUP:
        print("Mouse Right Up Detected")

image = np.zeros((480,640), np.uint8)
title = "MouseEvent"
title2 = "MouseEvent2"

cv2.imshow(title, image)
cv2.imshow(title2, image)

cv2.setMouseCallback(title, onMouse)
cv2.setMouseCallback(title2, onMouse)
cv2.waitKey(0)
cv2.destoryAllWindows()