# 무지개 그라데이션
from gpiozero import RGBLED
import time

# RGB LED 객체 생성
rgb = RGBLED(red=17, green=22, blue=27)

# 색상 변환속도 제어
DELAY = 0.02

print("PWM을 이용한 무지개 그라데이션 시작.(종료는 'CTRL+C')")

try:
    while True:
        print("Red -> Yellow (GREEN duty 증가)")
        # (1.0, 0.0, 0.0) -> (1.0, 1.0, 0.0)
        for g in range(0,101):
            rgb.color= (1.0, g/100, 0.0)
            time.sleep(DELAY)
        
        print("Yellow -> Green (RED duty 감소)")
        # (1.0, 1.0, 0.0) -> (0-.0, 1.0, 0.0)
        for r in range(100,-1,-1):
            rgb.color=(r/100, 1.0, 0)
            time.sleep(DELAY)
            
        print("Green -> Cyan (BLUE duty 증가)")
        # (0.0, 1.0, 0.0) -> (0.0, 1.0, 1.0)
        for b in range(0,101):
            rgb.color=(0.0, 1.0, b/100)
            time.sleep(DELAY)
        
        print("Cyan -> Blue (GREEN duty 감소)")
        # (0.0, 1.0, 1.0) -> (0.0, 0.0, 1.0)
        for g in range(100,-1,-1):
            rgb.color=(0.0, g/100, 1.0)
            time.sleep(DELAY)
            
        print("Blue -> Pink (RED duty 증가)")
        # (0.0, 0.0, 1.0) -> (1.0, 0.0, 1.0)
        for r in range(0,101):
            rgb.color=(r/100, 0.0, 1.0)
            time.sleep(DELAY)
        
        print("Pink -> Red (BLUE duty 감소)")
        # (1.0, 0.0, 1.0) -> (1.0, 0.0, 0.0)
        for b in range(100,-1,-1):
            rgb.color=(1.0, 0.0, b/100)
            time.sleep(DELAY)
except KeyboardInterrupt:
    pass
finally:
    rgb.close()
    print("프로그램을 종료합니다")