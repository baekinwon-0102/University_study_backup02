#4주차 응용실습과제: 스마트팩토리 자동분류 시스템
from gpiozero import Servo,RGBLED
import time

# SG90 구동 펄스폭 지정및 객체 생성(GPIO18)
servo = Servo(18, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)
# RGBLED GPIO pin 지정 및 객체 생성
rgb = RGBLED(red=17, green=22, blue=27)

# 스마트팩토리 DB 딕셔너리로 저장
factory_db = {
    '1': ((0,1,0), 0 ,"A제품(중앙라인)"), # Green, 서보위치: 0(mid)
    '2': ((0,0,1), -1, "B제품(왼쪽라인)"), # Blue, 서보위치: -1(min)
    '3': ((1,0,0), 1, "불량품(오른쪽라인)"), # Red, 서보위치: 1.0(max)
    '0': ((0,0,0), 0, "시스템 초기화(시스템 정지)") # Off, 서보위치: 0(mid)
    }

print("스마트팩토리 자동분류 시스템 시작")
print('='*40)
print("1:A제품 통과, 2:B제품 통과, 3:불량품 감지")
print("0: 시스템 초기화(시스템 정지), q: 시스템 빠져나오기")
print('='*40)

try:
    # 시스템 초기상태 지정
    # DB에서 RGB 초기상태 가져와서 위치 지정하기
    servo.value = factory_db['0'][1]
    rgb.color = factory_db['0'][0]
    time.sleep(0.5) # 모터 이동시간 보장
    # 서보모터의 떨림 방지
    servo.detach()
    
    while True:
        # 사용자로부터 센서 입력값 받기
        item = input("센서코드 입력:")
        if item == 'q':
            print("시스템 가동을 중지합니다")
            break
        if item in factory_db:
            # 코드(키)에 해당하는 정보(값) DB에서 가져와 변수에 저장하기
            color_val,servo_pos,status = factory_db[item]
            print(f"센서감지: {status}")
            
            # RGBLED 색상 구동하기
            rgb.color = color_val
            
            # 서보모터 위치 구동하기
            servo.value = servo_pos
            time.sleep(0.5)
            
            # 서보모터의 떨림 방지
            servo.detach()
            print("상품 전송완료")
        else:
            print("잘못된 코드입니다")
except KeyboardInterrupt:
    print("\n 사용자 강제 종료 감지")
finally:
    # 사용한 리소스 완전히 반납
    servo.close()
    rgb.close()
    print("스마트 팩토리 자동 분류시스템 종료")