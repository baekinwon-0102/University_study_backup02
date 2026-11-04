# LCD로 디지털 시계 구현하기
from rpi_lcd import LCD
from datetime import datetime
import time

# LCD 객체 생성(i2c 주소는 0x27 기본값으로 인식)
lcd = LCD()

print("LCD 스마트 시계 시작...(Ctrl+c 종료)")
lcd.clear()
try:
    while True:
        # 현재 날짜와 시간 데이터 가져오기
        now  = datetime.now()
        print(now)
        # LCD 출력할 포맷으로 변환
        # 날짜 예시: 2026-10-28
        date_string = now.strftime(" %Y-%m-%d ")
        # 시간 예시: 10:20:30
        time_string = now.strftime(" %H:%M:%S ")
        
        # LCD 화면에 출력하
        lcd.text(date_string,1) # 1번줄 날짜 출력
        lcd.text(time_string,2) # 2번줄 시간 출력
        
        # 1초마다 날짜시간 업데이트 
        time.sleep(1)
except KeyboardInterrupt:
    # LCD에 종료 텍스트 출력하기
    lcd.text("GoodBye!",1) # 1번줄 출력
    lcd.text("Raspbery Pi",2) # 2번줄 이름 출력
    time.sleep(3)
    lcd.clear() # 화면 전체 지우고 종료
    print("LCD 프로그램 종료")
