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
                said = r.recognize_google(audio, language="ja-JP")
                print(said)

            except Exception as e:
                print("Exception: " + str(e))

        return said

    text = get_audio()

    if "こんにちは" in text:
        my_file = Path("jp_Hello.mp3")
        if my_file.is_file():
            print("こんにちは。　今日は元気ですか。")
            playsound.playsound("jp_Hello.mp3")
            continue

        else:
            print("こんにちは。　今日は元気ですか。")
            text ="こんにちは。　今日は元気ですか"
            tts = gTTS(text=text, lang='ja')
            tts.save("jp_Hello.mp3")
            playsound.playsound("jp_Hello.mp3")
            continue

    if "君の名は" in text:
        my_file = Path("jp_name.mp3")
        if my_file.is_file():
            print("私の名はアマデウスです。")
            playsound.playsound("jp_name.mp3")
            continue

        else:
            print("私の名はアマデウスです。")
            text ="私の名はあまでうすです"
            tts = gTTS(text=text, lang='ja')
            tts.save("jp_name.mp3")
            playsound.playsound("jp_name.mp3")
            continue

    if "YouTube" in text:
        my_file = Path("jp_youtube.mp3")
        if my_file.is_file():
            print("YouTubeを実行します。")
            playsound.playsound("jp_youtube.mp3")
            url = "https://www.youtube.com"
            webbrowser.open(url)
            continue

        else:
            print("YouTubeを実行します。")
            text ="YouTubeを実行します"
            tts = gTTS(text=text, lang='ja')
            tts.save("jp_youtube.mp3")
            playsound.playsound("jp_youtube.mp3")
            url = "https://www.youtube.com"
            webbrowser.open(url)
            continue
        
    else:
        print('よく理解出来ませんでした。もう一度いってください。')
        continue
