from flask import Flask, request
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone # 음계 사용하면 필요 없
import time, threading

app = Flask(__name__)

# GPIO 21번 연결된 수동부저 객체생성( 기본 220hz ~ 880hz )
buzzer = TonalBuzzer(21)

stop_event = threading.Event()
is_playing=False

melody = [
    ['G4', 0.2],['G4', 0.2],['A4',0.4],['G4', 0.4],['C5', 0.4],['B4', 0.8],
    ['G4', 0.2],['G4', 0.2],['A4',0.4],['G4', 0.4],['D5', 0.4],['C5', 0.8],
    ['G4', 0.2],['G4', 0.2],['G5',0.4],['E5', 0.4],['C5', 0.4],['B4', 0.4],['A4', 0.4],
    ['F5', 0.2],['F5', 0.2],['E5',0.4],['C5', 0.4],['D5', 0.4],['C5', 0.8]
]

def buzzer_play(item):
    global is_playing
    try:
        while not stop_event.is_set():
            
            
            if item =='beep':
                is_playing = True
                buzzer.play(Tone(880))
                time.sleep(1)
                buzzer.stop()
                time.sleep(1)
                
            
            elif item == 'siren':
                is_playing = True
                for freq in range(300,851, 10):
                    buzzer.play(Tone(freq))
                    time.sleep(0.01)
                
                # 주파수 하강 (850hz에서 300hz까지 10hz씩)
                for freq in range(850, 300, -10):
                    buzzer.play(Tone(freq))
                    time.sleep(0.01)
                
            elif item == 'music':
                is_playing = True
                for note, duration in melody:
                    if stop_event.is_set():break
                    buzzer.play(Tone(note))
                    time.sleep(duration*0.85)
                    buzzer.stop()
                    time.sleep(duration*0.15)
                time.sleep(1)
            elif item == 'stop':
                stop_buzzer()
                break
    except Exception as e:
        print("부저 에러",e)
    finally:
        buzzer.stop()
        
        is_playing=False

def stop_buzzer():
    global is_playing 
    stop_event.set()
    buzzer.stop()
    is_playing = False
    print("쓰레드 종료")
    time.sleep(0.5)

@app.route('/get/buzzer/<item>')
def play_buzzer(item):
    global is_playing, stop_event, buzzer_thread
    print(item)
    
    if item == 'stop':
        stop_buzzer()
        return "Melody Stop"
    if item not in ['beep', 'siren', 'music']:
        return 'invalid melody type'
    
    if is_playing:
        print("연주중")
        stop_event.set()
        if buzzer_thread and buzzer_thread.is_alive():
            buzzer_thread.join()
    
    stop_event.clear()
    is_playing = True
    
    buzzer_thread = threading.Thread(target=buzzer_play, args=(item,))
    buzzer_thread.daemon = True
    buzzer_thread.start()
    
    return f"{item} Playing"

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=5002)