import numpy as np
import cv2
image = np.zeros((480, 640), np.uint8) # 480 * 640 사이즈 윈도우를 0으로 채움
image[:] = 128 # 모든 배열 값을 128로 채워서 회색이 됨

title1, title2 = "Position1", 'Position2'

cv2.imshow(title1, image)
cv2.imshow(title2, image)

while True:
    key = cv2.waitKeyEx(100) # 키보드 입력 값 반환

    if key == ord('q'): # q를 아스키 코드로 변환
        break
    elif key == ord('Q'):
        break
    elif key == ord('c'):
        print("c가 입력되었습니다.")
    elif key == ord('d'):
        print("d가 입력되었습니다.")
    elif key == ord('C'):
        print("C가 입력되었습니다.")
    elif key == ord('D'):
        print("D가 입력되었습니다.")
