import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    global title
    if event == cv2.EVENT_LBUTTONDOWN:
        text = str(image[y, x])
        cv2.circle(image,(x,y),4,(0,0,255),2)
        cv2.putText(image,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,0))
        cv2.imshow(title,image)

title = 'imgaeK'
image = cv2.imread('read_color.jpg',cv2.IMREAD_COLOR)

if image is None:
    raise Exception("read Error")
cv2.imshow(title,image)
cv2.setMouseCallback(title,onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()