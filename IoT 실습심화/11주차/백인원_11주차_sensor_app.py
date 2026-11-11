# DS18B20 온도센서로부터 데이터 센싱하기
from flask import Flask, jsonify
import glob, os
import time
from rpi_lcd import LCD

app = Flask(__name__)
lcd = LCD()

status = None
temps = [0.0, 0.0]

sys_state_dict = {"status":status, "temperature":temps}

# 센서파일이 위치하는 경로지정(온도 센서는 고유 ID가 28-로 시작)
base_dir = '/sys/bus/w1/devices/' # 기본 경로
device_folders = glob.glob(base_dir+'28-*') # 센서별 폴더경로

if not device_folders:
    print("센서를 찾을 수 없습니다")
    exit()
    
# 첫 번째로 발견된 센서의 경로 지정
device_folder = device_folders[0]
# 센서값이 저장된 파일 지정
device_file = device_folder + '/w1_slave'

# 센서값 raw data(가공하지 않은 원본 데이터) 전체 읽기
def read_temp_raw():
    with open(device_file,'r') as f:
        lines = f.readlines()
        return lines
    
# raw data 파싱해서 섭씨온도값 반환
def read_temp():
    lines = read_temp_raw()
    
    # 첫번째줄 끝에 성공(YES)이 있어야 수집 완료
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
        
    # 두 번째 줄에서 't=' 위치를 찾아 온도 값 추출
    equals_pos = lines[1].find('t=')
    if equals_pos != -1: # false가 아니면
        temp_string = lines[1].strip()[equals_pos+2:]
        temp_c = float(temp_string) / 1000.0 # 밀리값을 섭씨(℃)로 변환
        return round(temp_c,2)
    
@app.route('/temp')
def get_status():
    global status
    current_temp = read_temp()
    
    sys_state_dict["status"] = "Normal"
    sys_state_dict["temperature"][0] = current_temp
    
    response_data = sys_state_dict
    lcd.text(f"Status: {response_data['status']}",1)
    lcd.text(f"Temp: {response_data['temperature'][0]} ℃",2)
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)
