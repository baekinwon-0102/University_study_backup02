# CharLCD 텍스트 출력하기
# pip install rpi_lcd 터미널에서 설치 후 진행
from rpi_lcd import LCD
import time

# LCD 객체 생성(i2c 주소는 0x27 기본값으로 인식)
lcd = LCD()

print("CharLCD 텍스트 출력하기 (Ctrl-C 종료)")
try:
    while True:
        # LCD에 텍스트 출력하기
        lcd.text("Hello Raspbery!",1) # 1번줄 출력
        lcd.text("by Baek Inwon",2) # 2번줄 이름 출력
        time.sleep(1)
except KeyboardInterrupt:
    # LCD에 종료 텍스트 출력하기
    lcd.text("GoodBye!",1) # 1번줄 출력
    lcd.text("Raspbery Pi",2) # 2번줄 이름 출력
    time.sleep(3)
    lcd.clear() # 화면 전체 지우고 종료
    print("LCD 프로그램 종료")