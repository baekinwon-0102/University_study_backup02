from gpiozero import LED
import time

# GPIO 26, 20번에 연결된 LED 객체 생성
led_a = LED(26)
led_b = LED(20)

# list에 순서대로 저장
leds = [led_a, led_b]

print("=== for문을 이용한 two LED 제어 ===")
try:
    for i in range(5):
        print(f"{i+1}번째 반복 시작")
        leds[0].on()
        time.sleep(1)
        leds[0].off()
        time.sleep(1)
        leds[1].on()
        time.sleep(1)
        leds[1].off()
        time.sleep(1)
        leds[0].on()
        leds[1].on()
        time.sleep(1)
        leds[0].off()
        leds[1].off()
        time.sleep(1)
except KeyboardInterrupt:
    print("프로그램 강제 종료")
