from flask import Flask, Response, jsonify
from picamera2 import Picamera2
import cv2
import time
import os

app = Flask(__name__)

SAVE_DIR = 'static/image'
os.makedirs(SAVE_DIR, exist_ok=True)

picam2 = Picamera2()
picam2.preview_configuration.main.size = (1280,720)
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")

picam2.start()

def generate_frames():
    while True:
        im = picam2.capture_array()
        
        # 배열을 웹에서 볼 수 있는 JPEG 이미지로 압축
        ret, buffer = cv2.imencode(".jpeg",im)
        if not ret: # 압축 실패시 건너뛰기
            continue
        # 압축된 이미지를 네트워크 전송용 바이트 형태로 변환
        frame_bytes = buffer.tobytes()
        
        # return 대신 yeild(연속반환)를 사용해 웹 브라우저로 끊임없이 전송
        yield (b'--frame\r\n'
               b'Content-Type:image/jpeg\r\n\r\n' + frame_bytes+b'\r\n')
    
@app.route('/stream')
def stream():
    print("클라이언트 CCTV 스트리밍 접속!")
    return Response(generate_frames(),
                    mimetype = 'multipart/x-mixed-replace; boundary=frame')
        # 여러개의 이미 지데이터를 연속해서 보내서 새 영상 데이터가 오면 이전 데이터에 덮어쓰기
    
@app.route('/picture')
def take_pickture():
    im = picam2.capture_array()
    
    filename = time.strftime("capture_%Y%m%d_%H%M.jpeg")
    filepath = f"{SAVE_DIR}/{filename}"
    
    cv2.imwrite(filepath, im)
    print(f"사진 촬영 및 저장 완료; {filepath}")
    
    image_url = f"/{SAVE_DIR}/{filename}"
    
    return jsonify({"image_url": image_url})
    
if __name__ == "__main__":
    try:
        print("웹 CCTV 서버가 시작되었습니다.(종료: Ctrl+C)")
        app.run(host='0.0.0.0', port=5004)
    finally:
        picam2.stop()
        picam2.close()
        print("웹 CCTV 서버를 종료합니다")
            
