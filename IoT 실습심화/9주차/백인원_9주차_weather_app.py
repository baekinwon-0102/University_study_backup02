# 스마트 날씨 대시보드 웹 서버
from flask import Flask, render_template
from datetime import datetime
import requests
from rpi_lcd import LCD
import time
import threading

# 웹 서버 객체 생성
app = Flask(__name__)
lcd = LCD()

weather_data = {
                'temperature': '--',
                'humidity': '--',
                'description': '--'
                }

# OpenweatherMap API key
api_key = "b197e314b7bfee6b1fb40faf3778309d"

def upt():
    global weather_data
    # OpenweatherMap 사이트 URL
    url = "https://api.openweathermap.org/data/2.5/weather"
    # URL 쿼리스트링에 들어갈 요청 파라미터 정보
    params = {
    'q' : 'Incheon, KR', # 도시명(인천, 대한민국)
    'appid': api_key,    # 발급받은 API Key
    'units' : 'metric',  # 온도를 섭씨 단위로 받기 위한 설정
    }
    # 현재 날짜와 시간 정보 저장하기
    # 날씨정보를 저장할 딕셔너리 변수
    weather_data = None
    while True:
        try:
            # openWeatherMap으로 요청메시 지보내고 응답받기
        
            response = requests.get(url, params = params)
            if response.status_code == 200: # 성공인 경우
                data = response.json() # 받은 JSON을 딕셔너리로 변환
                print("응답메시지",data)
                weather_data = {
                    'temperature': data['main']['temp'],
                    'humidity': data['main']['humidity'],
                    'description': data['weather'][0]['description']
                    }
                print('weather_data:', weather_data)
                lcd.text(f"Temp: {weather_data['temperature']} C",1) # 1번줄 날짜 출력
                lcd.text(f"{weather_data['description']}",2) # 2번줄 시간 출력
                
            else:
                print("API Error: {response.status.code}")
                break
        except Exception as e: # 네트워크 에러가 발생한 경우
            print(f"Network Error: {e}")
        
        time.sleep(60)

# Flask 홈 화면
@app.route('/', strict_slashes=False)
def index():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return render_template('weather.html',weather=weather_data, time=current_time)

if __name__ == "__main__":
    lcd_thread = threading.Thread(target=upt)
    lcd_thread.daemon=True
    lcd_thread.start()
    app.run(host='0.0.0.0',port=5000)