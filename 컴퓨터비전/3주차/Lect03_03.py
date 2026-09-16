import numpy as np
import cv2

image = np.zeros((400,600,3),np.uint8)
image[:] = (255,255,255)

pt1 = (50,50)
pt2 = (250,150)
pt3 = (400,150)
pt4 = (500,50)
roi = (50, 200, 200, 100)

# line(title, pos1, pos2,color, bold)
cv2.line(image,pt1,pt2,(0,0,255))
cv2.line(image,pt3,pt4,(0,255,0))

# rectangle(title, pos1,pos2, color, bold)
cv2.rectangle(image,pt1,pt2,(255,0,0),3)
cv2.rectangle(image,roi,(0,0,255),3)
cv2.rectangle(image,(400, 200, 100, 100),(0,255,0), cv2.FILLED)

cv2.imshow('line & rectangle',image)
cv2.waitKey(0)
cv2.destroyAllWindows()