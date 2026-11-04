# OpenWeatherMap 사이트에서 주변날씨정보 받아오기
# Python requests 모듈 사용
import requests
from datetime import datetime

# 날짜형식은 2026-10-23 10:30
current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
print(current_time)

# OpenweatherMap API Key
api_key = "b197e314b7bfee6b1fb40faf3778309d"
# 사이트 URL
url = "https://api.openweathermap.org/data/2.5/weather"
# 요청 파람터
params = {
    'q' : 'Incheon, KR', # 도시명(인천, 대한민국)
    'appid': api_key,    # 발급받은 API Key
    'units' : 'metric',  # 온도를 섭씨 단위로 받기 위한 설정
    }

# openWeatherMap으로 요청메시지 보내고 응답받기
response = requests.get(url, params = params)
weather_data = response.json() # 받은 JSON을 딕셔너리로 변환

# 받은 날씨정보를 출력하기
print(weather_data)