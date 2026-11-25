import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        pedestrians = hog.detectMultiScale(frame)

        for ped in pedestrians:
            top_left = (ped[0], ped[1])
            bottom_right = (ped[0] + ped[2], ped[1] + ped[3])
            cv2.rectangle(frame,top_left,bottom_right,255,2)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()