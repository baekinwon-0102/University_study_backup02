import numpy as np
import cv2

image = np.zeros((480, 640), np.uint8) # 480 * 640 사이즈 윈도우를 0으로 채움
image[:] = 128 # 모든 배열 값을 128로 채워서 회색이 됨

title1, title2 = "Position1", 'Position2'

# cv2.namedWindow(title1) # moveWindow 사용하려면 이거 필수 아니면 없어도 imshow만 쓰면 뜸
# cv2.namedWindow(title2)

# cv2.moveWindow(title1, 150, 150) # 지정한 위치로 윈도우 창 이동
# cv2.moveWindow(title2, 400, 50)  # 내 화면의 이미지 좌표

cv2.imshow(title1, image)
cv2.imshow(title2, image)

while True:
    key = cv2.waitKeyEx(100) # 키보드 입력 값 반환
    print(key)

    if key == 27:  # ESC 입력시 종료
        break
    elif key == ord('q'): # q를 아스키 코드로 변환
        break
    elif key == 81:
        break
    elif key == ord('a'):
        print("a키가 입력되었습니다.")
    elif key == ord('A'):
        print("A키가 입력되었습니다.")
    elif key == 2424832:
        print("왼쪽 화살표 눌렸습니다.")
    elif key == 2555904:
        print("오른쪽 화살표 눌렸습니다.")
    elif key == 2621440:
        print("아래쪽 화살표 눌렸습니다.")
    elif key == 2490368:
        print("위쪽 화살표 눌렸습니다.")

# cv2.waitKey(0) # 키 입력을 기다림
# cv2.destroyAllWindows()