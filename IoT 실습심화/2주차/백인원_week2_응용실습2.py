from gpiozero import LED
import time, threading, sys

# GPIO 26, 20번에 연결된 LED 객체 생성
led_a = LED(26)
led_b = LED(20)

def blink_led(led, interval):
    while True:
        led.on()
        time.sleep(interval)
        led.off()
        time.sleep(interval)


if __name__ == "__main__":
    print("멀티 스레딩 LED 실습")
    t1 = threading.Thread(target=blink_led,args=(led_a,1,))
    t2 = threading.Thread(target=blink_led,args=(led_b,0.5,))
    
    t1.daemon=True
    t2.daemon=True
    t1.start()
    t2.start()

try:
    while True:
        print("[메인스레드] LED가 독립적으로 동작중에 있습니다")
        time.sleep(2)
except KeyboardInterrupt:
    print("프로그램 강제 종료")
    sys.exit()

