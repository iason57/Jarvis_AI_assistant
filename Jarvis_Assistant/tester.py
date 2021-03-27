from playsound import playsound
import speech_recognition as sr
import os

#playsound("C:\\Users\\iason\\Desktop\\Jarvis_Assistant\\audio\\intro.mp3")

r = sr.Recognizer()


while True:
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source,duration =0.5)
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio)#,language="en-US"
        
        query = query.lower()
        if 'jarvis' in query:
            query = query.replace('jarvis', '')
        print(query)
        break
    except Exception as e:
        print(e)
        print("Say that again please...")