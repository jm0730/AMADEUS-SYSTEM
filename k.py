import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import webbrowser
import cv2
from pathlib import Path

while True:

    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""


            try:
                said = r.recognize_google(audio, language="ko-KR")
                print(said)

            except Exception as e:
                print("Exception: " + str(e))

        return said

    text = get_audio()

    if "안녕" in text:
        my_file = Path("kr_Hello.mp3")
        if my_file.is_file():
            print("안녕하세요.")
            playsound.playsound("kr_Hello.mp3")
            continue

        else:
            print("안녕하세요.")
            text ="안녕하세요"
            tts = gTTS(text=text, lang='ko')
            tts.save("kr_Hello.mp3")
            playsound.playsound("kr_Hello.mp3")
            continue

    if "너의 이름은" in text:
        my_file = Path("kr_name.mp3")
        if my_file.is_file():
            print("제 이름은 아마데우스라고 합니다.")
            playsound.playsound("kr_name.mp3")
            continue

        else:
            print("제 이름은 아마데우스라고 합니다.")
            text ="제 이름은 아마데우스라고 합니다."
            tts = gTTS(text=text, lang='ko')
            tts.save("kr_name.mp3")
            playsound.playsound("kr_name.mp3")
            continue

    if "유튜브" in text:
        my_file = Path("kr_youtube.mp3")
        if my_file.is_file():
            print("YouTube를 실행합니다.")
            playsound.playsound("kr_youtube.mp3")
            url = "https://www.youtube.com"
            webbrowser.open(url)
            continue

        else:
            print("YouTube를 실행합니다.")
            text ="YouTube를 실행합니다."
            tts = gTTS(text=text, lang='ko')
            tts.save("kr_youtube.mp3")
            playsound.playsound("kr_youtube.mp3")
            url = "https://www.youtube.com"
            webbrowser.open(url)
            continue
        
    else:
        print('잘 듣지 못했습니다. 다시 한 번 말씀해 주세요.')
        continue
