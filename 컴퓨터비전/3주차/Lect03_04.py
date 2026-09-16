import numpy as np
import cv2

image = np.zeros((400,600,3), np.uint8)
image[:] = (255,255,255)

pt1=(50,200)
pt2=(50,260)

# putText(window, title, pos, fontface, fontScale, color)
cv2.putText(image, 'SIMPLEX',(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(42,42,165))
cv2.putText(image, 'DUPLEX',(50,130),cv2.FONT_HERSHEY_DUPLEX,3,(128,128,0))
cv2.putText(image, 'TRIPLEX',pt1,cv2.FONT_HERSHEY_TRIPLEX,2,(221,160,221))
fontFace = cv2.FONT_HERSHEY_PLAIN | cv2.FONT_ITALIC # 기울임 표현
cv2.putText(image, 'ITALIC',pt2,fontFace,4,(221,160,221))

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()