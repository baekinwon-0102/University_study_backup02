import numpy as np
import cv2

capture = cv2.VideoCapture('video_file2.avi')

if not capture.isOpened(): raise Exception('Cannot open video')

frame_rate = capture.get(cv2.CAP_PROP_FPS)
delay = int(1000 / frame_rate)

width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
print('resolution:', width, 'x',height)
frame_cnt = 0
font = cv2.FONT_HERSHEY_SIMPLEX

fourcc = cv2.VideoWriter_fourcc(*'FMP4')
writer = cv2.VideoWriter('video_file2_out.mp4', fourcc, frame_rate, (int(width),int(height)))

while True:
    ret, frame = capture.read()

    if not ret or cv2.waitKey(delay) >= 0:
        break

    frame_cnt += 1
    cv2.putText(frame, str(frame_cnt), (52, 52), font, 2, (0, 0, 0), 3)
    cv2.putText(frame,str(frame_cnt),(50,50),font,2,(255,255,0),3)
    writer.write(frame)
    cv2.imshow('video file',frame)

capture.release()
writer.release()