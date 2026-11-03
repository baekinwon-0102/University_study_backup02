import numpy as np
import cv2

capture = cv2.VideoCapture('video_file2.avi')

if not capture.isOpened(): raise Exception('Cannot open video')

frame_rate = capture.get(cv2.CAP_PROP_FPS)
delay = int(1000 / frame_rate)

width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
print('resolution:', width, 'x',height)
print('frame_rate:', frame_rate)
print('delay:', delay)
frame_cnt = 0
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame = capture.read()

    if not ret or cv2.waitKey(delay) >= 0:
        break
    bgr = cv2.split(frame)
    frame_cnt += 1
    if frame_cnt > 90:
        break
    elif frame_cnt <=30:
        cv2.add(bgr[0],100,bgr[0])
        frame = cv2.merge(bgr)
        cv2.putText(frame, str(frame_cnt), (52, 52), font, 2, (0, 0, 0), 3)
        cv2.putText(frame, str(frame_cnt), (50, 50), font, 2, (0, 0, 255), 3)
    elif frame_cnt <=60:
        cv2.add(bgr[1], 100, bgr[1])
        frame = cv2.merge(bgr)
        cv2.putText(frame, str(frame_cnt), (52, 52), font, 2, (0, 0, 0), 3)
        cv2.putText(frame, str(frame_cnt), (50, 50), font, 2, (255, 0, 0), 3)
    elif frame_cnt <=90:
        cv2.add(bgr[2], 100, bgr[2])
        frame = cv2.merge(bgr)
        cv2.putText(frame, str(frame_cnt), (52, 52), font, 2, (0, 0, 0), 3)
        cv2.putText(frame, str(frame_cnt), (50, 50), font, 2, (0, 255 , 0), 3)
    cv2.imshow('video file',frame)

capture.release()