import numpy as np
import cv2

def onMouse(event, x, y, flags, data):
    global pt
    if event == cv2.EVENT_LBUTTONDOWN:
        pt = (x,y)
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.rectangle(image, pt, (x,y), (255,0,0),2)

        mask = np.zeros(image.shape[:2], np.uint8)
        mask[pt[1]:y, pt[0]:x] = 255
        mean_value2 = cv2.mean(image,mask)
        mean_value2_str = str(round(mean_value2[0]))

        cv2.putText(image,mean_value2_str,pt,font,0.5,(255,0,0))

        cv2.imshow("image",image)
    elif event == cv2.EVENT_RBUTTONDOWN:
        pt = (x,y)
    elif event == cv2.EVENT_RBUTTONUP:
        cv2.rectangle(image, pt, (x, y), (0, 0, 255), 2)

        mask = np.zeros(image.shape[:2], np.uint8)
        mask[pt[1]:y, pt[0]:x] = 255
        mean_value2 = cv2.mean(image, mask)
        mean_value2_str = str(round(mean_value2[2]))

        cv2.putText(image, mean_value2_str, pt, font, 0.5, (0, 0, 255))

        cv2.imshow("image", image)

image = cv2.imread("logo.jpg")

if image is None:
    raise Exception("read error")

pt = (-1,-1)
font = cv2.FONT_HERSHEY_COMPLEX

cv2.imshow("image",image)
cv2.setMouseCallback('image',onMouse)
cv2.waitKey(0)