from flask import Flask, request, render_template
from gpiozero import Servo
import time

# 웹 서버 객체 생성
app = Flask(__name__)

# SG90 서보모터 객체 생성 (GPIO 18번)
servo = Servo(18, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

# door의 현재 상태를 저장할 전역변수 ('CLOSE' 또는 'OPEN')
current_status = 'CLOSE'

def control_door(action):
    global current_status
    if action == 'OPEN':
        servo.max() # 서보모터를 최대각도(1.0)로 이동 -> 문열림
        current_status = 'OPEN'
    elif action == 'CLOSE':
        servo.min() # 서보모터를 최소 각도(-1.0)로 이동 -> 문 닫힘
        current_status = 'CLOSE'
    # 모터가 회전할 수 있는 시간 추가
    time.sleep(0.5)
    # 이동 후 펄스신호를 끊어 떨림(jiter) 방지
    servo.detach()
    
# 초기 상태 설정: 서버가 켜질때 문닫음
control_door('CLOSE')

# 1. Flask 홈 화면 및 SSR 렌더링
@app.route('/',strict_slashes=False)
def index():
    # 현재 문 상태를 'door_status'라는 변수로 HTML로 전달
    return render_template('door_index.html', door_status=current_status)

# 2. SSR 방식, GET 요청 시 처리 (웹 버튼 클릭 시)
@app.route('/get',methods=['GET'], strict_slashes=False)
def get_door():
    action = request.args.get('action') # 주소창에서 ?action=값 읽기
    
    if action in ['OPEN','CLOSE']:
        control_door(action)
        
    return render_template('door_index.html',door_status=current_status)

# 3. CSR방식. POST 요청시 처리 (앱 인벤터 제어용)
@app.route('/post',methods=['POST'], strict_slashes=False)
def post_door():
    action = request.form.get('action') # 주소창에서 ?action=값 읽기
    
    if action in ['OPEN','CLOSE']:
        control_door(action)
        
    return f"DOOR_STATUS: {current_status}"

if __name__ == "__main__":
    # 앞선 실습과 충돌나지 않도록 포트는 5001번으로 수정
    app.run(host='0.0.0.0', port=5001)
    