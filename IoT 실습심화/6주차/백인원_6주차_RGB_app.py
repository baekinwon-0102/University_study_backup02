from flask import Flask, request, render_template
from gpiozero import RGBLED

# 웹 서버 객체 생성
app = Flask(__name__)

# RGBLED pin 설정 및 객체 생성
rgb = RGBLED(red=17, green=22, blue=27)

# RGB 상태 DB (딕셔너리)
RGB_state_dict = {'RED':0, 'GREEN':0, 'BLUE':0}

# RGBLED 제어 핵심로직
def update_RGB():
    r_val = float(RGB_state_dict['RED'])
    g_val = float(RGB_state_dict['GREEN'])
    b_val = float(RGB_state_dict['BLUE'])
    rgb.color = (r_val,g_val,b_val)
    
update_RGB() # REBLED 초기화

# 루트로 접속 시 처리
@app.route('/', strict_slashes=False)
def index():
    return render_template('RGB_index.html', RGB_states=RGB_state_dict)

# SSR방식, GET 요청에 대한 처리 (웹 브라우저 용)
@app.route('/get', methods=['GET'], strict_slashes=False)
def get_RGB():
    # URL 쿼리에서 key로 value 저장하기
    color = request.args.get('color')
    state = request.args.get('state')
    
    RGB_state_dict[color] = int(state)
    update_RGB() # RGBLED 상태 업데이트
    
    return render_template('RGB_index.html', RGB_states=RGB_state_dict) # 템플릿 엔진으로 넘겨주는 값

@app.route('/post',methods=['POST'], strict_slashes=False)
def post_RGB():
    # 요청메시지 바디에서 key로 value 저장
    color = request.form.get('color')
    pwm_v = request.form.get('pwm_value')
    print(color)
    print(pwm_v)
    
    RGB_state_dict[color] = int(pwm_v)/100
    update_RGB() # RGBLED pwm 값 업데이트
    
    # 앱 인벤터가 성공여부를 확인할 수 있도록 결과 문자열 반환
    return f"""RED:{RGB_state_dict['RED']},
        GREEN:{RGB_state_dict['GREEN']}
        BLUE:{RGB_state_dict['BLUE']}"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)