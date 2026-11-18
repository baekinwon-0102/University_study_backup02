# Flask를 이용한 다중 스마트 센스 웹 서버 프로그램
from flask import Flask, jsonify
from rpi_lcd import LCD
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
import glob, time
import threading

WARNING_TEMP = 28.0
CRITICAL_TEMP = 30.0

app = Flask(__name__)

try:
    lcd = LCD()
    lcd.clear()
    lcd.text("System Starting", 1)
    lcd.text("Please wait...",2)
except Exception as e:
    print(f"LCD 초기화 실패 (연결상태를 확인하세요): {e}")
    lcd = None

try:
    buzzer = TonalBuzzer(21)
except Exception as e:
    print(f"부저 초기화 실패 (연결상태를 확인하세요): {e}")
    buzzer = None

stop_event = threading.Event()
exit_event = threading.Event()
buzzer_thread = None

base_dir = '/sys/bus/w1/devices/'

device_folders = glob.glob(base_dir + '28-*')

device_files = []
for folder in device_folders:
    file_path = folder + '/w1_slave'
    device_files.append(file_path)
    
sensor_count = len(device_files)
print(f"=== 초기화 완료: 감지된 센서 {sensor_count}개 ===")

if sensor_count > 0:
    initial_status = "Initializing"
else:
    initial_status = "No Sensor"

sys_state_dict = {
    "status": initial_status,
    "sensor_count": sensor_count,
    "temperature": [None] * sensor_count
}

def read_temp_raw(device_file):
    with open(device_file,'r') as f:
        lines = f.readlines()
        return lines
    
# raw data 파싱해서 섭씨온도값 반환
def read_temp(device_file):
    try:
        lines = read_temp_raw(device_file)
        retry = 0
        # 첫번째줄 끝에 성공(YES)이 있어야 수집 완료
        while lines[0].strip()[-3:] != 'YES' and retry <5:
            time.sleep(0.2)
            lines = read_temp_raw(device_file)
            retry +=1
        if lines[0].strip()[-3:] != 'YES':
            return None
            
        # 두 번째 줄에서 't=' 위치를 찾아 온도 값 추출
        equals_pos = lines[1].find('t=')
        if equals_pos != -1: # false가 아니면
            temp_string = lines[1].strip()[equals_pos+2:]
            temp_c = float(temp_string) / 1000.0 # 밀리값을 섭씨(℃)로 변환
            return round(temp_c,2)
    except FileNotFoundError:
        print(f"[센서 연결 끊김] 파일을 찾을 수 없습니다: {device_file}")
    except Exception as e:
        print(f"[센서 읽기 오류] {device_file}: {e}")

def check_system_status(temps):
    status = "Normal"
    
    for i in temps:
        if i is None:
            continue
        if i > CRITICAL_TEMP:
            return "Critical"
        elif i > WARNING_TEMP:
            status = "Warning"
    
    return status

def update_lcd(temps):
    if lcd is None:
        return
    
    if len(temps) <= 0:
        lcd.text("No sensor", 1)
        lcd.text("Found",2)
    elif len(temps) == 1:
        lcd.text(f"Temp1: {temps[0]}", 1)
        lcd.text("Temp2: N/A",2)
    elif len(temps) == 2:
        lcd.text(f"Temp1: {temps[0]}", 1)
        lcd.text(f"Temp2: {temps[1]}",2)

def buzzer_play(item):
    if buzzer is None:
        return
    try:
        while not stop_event.is_set():
            if item == 'beep':
                if stop_event.is_set():
                    break
                buzzer.play(Tone(880))
                time.sleep(1)
                buzzer.stop()
                time.sleep(1)
                
            elif item == 'siren':
                for freq in range(300,851,10):
                    if stop_event.is_set():
                        break
                    buzzer.play(Tone(freq))
                    time.sleep(0.01)
                for freq in range(850, 300, -10):
                    if stop_event.is_set():
                        break
                    buzzer.play(Tone(freq))
                    time.sleep(0.01)
    finally:
        buzzer.stop()
        
def control_buzzer(status):
    global buzzer_thread
    
    if buzzer_thread is not None and buzzer_thread.is_alive():
        stop_event.set()
        buzzer_thread.join()
    if status == 'Warning':
        item = 'beep'
    elif status == 'Critical':
        item = 'siren'
    else:
        return
    
    stop_event.clear()
    buzzer_thread = threading.Thread(target=buzzer_play, args=(item,))
    buzzer_thread.daemon = True
    buzzer_thread.start()
    
def update_sensor():
    global sys_state_dict
    
    prev_status = None
    
    if sensor_count == 0:
        print("연결된 센서가 없어 업데이트를 실행하지 않습니다.")
        update_lcd([])
        return
    
    while not exit_event.is_set():
        current_temps = []
        
        for device_file in device_files:
            temp = read_temp(device_file)
            current_temps.append(temp)
        
        current_status = check_system_status(current_temps)
        
        sys_state_dict['status'] = current_status
        sys_state_dict['temperature'] = current_temps
        
        update_lcd(current_temps)
        
        if prev_status != current_status:
            control_buzzer(current_status)
            prev_status = current_status
        
        print(f"[시스템 상태] {sys_state_dict}")
        time.sleep(3)
        
@app.route('/temp')
def get_status():
    response_data = sys_state_dict.copy()
    return jsonify(response_data)

if __name__ == "__main__":
    try:
        sensor_thread = threading.Thread(target=update_sensor,daemon=True)
        sensor_thread.start()
        app.run(host='0.0.0.0', port =5003, use_reloader=False)
    finally:
        stop_event.set()
        exit_event.set()
        if buzzer:
            buzzer.stop()
        if lcd:
            lcd.clear()
            lcd.text("System Stopped",1)
    