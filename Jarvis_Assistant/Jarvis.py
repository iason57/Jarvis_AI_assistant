import pyttsx3
import datetime
import speech_recognition as sr
import pywhatkit
import wikipedia
import pyjokes
import webbrowser as wb
import os
import smtplib
import requests
import json
import random
from pynput.keyboard import Key, Controller
import time as xronos
import pprint

keyboard  = Controller()
#shortcut ctrl + shift + z

#
from win32com.client import Dispatch
def speak2(audio):
    speak2 = Dispatch(("SAPI.SpVoice"))
    speak2.Speak(audio)
#
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def spliter(word):
    return [char for char in word] 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M")
    speak("The current time is " +Time)
    print("The current time is : "+Time)

def date():
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    if month==1:
        speak("The date is "+str(date)+"of January")
        print("The date is : "+str(date)+"of January")
    elif month==2:
        speak("The date is "+str(date)+" of February")
        print("The date is : "+str(date)+" of February")
    elif month==3:
        speak("The date is "+str(date)+" of March")
        print("The date is : "+str(date)+" of March")
    elif month==4:
        speak("The date is "+str(date)+" of April")
        print("The date is : "+str(date)+" of April")
    elif month==5:
        speak("The date is "+str(date)+" of May")
        print("The date is : "+str(date)+" of May")
    elif month==6:
        speak("The date is "+str(date)+" of June")
        print("The date is : "+str(date)+" of June")
    elif month==7:
        speak("The date is "+str(date)+" of July")
        print("The date is : "+str(date)+" of July")
    elif month==8:
        speak("The date is "+str(date)+" of August")
        print("The date is : "+str(date)+" of August")
    elif month==9:
        speak("The date is "+str(date)+" of September")
        print("The date is : "+str(date)+" of September")
    elif month==10:
        speak("The date is "+str(date)+" of October")
        print("The date is : "+str(date)+" of October")
    elif month==11:
        speak("The date is "+str(date)+" of November")
        print("The date is : "+str(date)+" of November")
    else:
        speak("The date is "+str(date)+" of December")
        print("The date is : "+str(date)+" of December")

def etos():
    year = int(datetime.datetime.now().year)
    print("The year is : "+year)
    speak("The year is  "+year)

def wishme():
    speak("Welcome back sir!")
    print("Welcome back sir!")
    time()
    date()
    hour = int(datetime.datetime.now().hour)
    if hour >= 5  and hour<12:
        speak("Good morging sir!")
        print("Good morging sir!")
    elif hour >= 12 and hour<18:
        speak("Good afternoon sir!")
        print("Good afternoon sir!")
    elif hour >= 18 and hour<24:
        speak("Good evening sir!")
        print("Good evening sir!")
    else:
        speak("Good night sir!")
        print("Good night sir!")
    
    speak("Jarvis at your service. Please tell me how can I help you?")
    print("Jarvis at your service. Please tell me how can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    while True:
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language='en-in')
            query = query.lower()
            if 'jarvis' in query:
                query = query.replace('jarvis', '')
            print(query)
            break
        except Exception as e:
            print(e)
            speak("Say that again please...")
    
    return query

def standby_():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    while True:
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language='en-in')
            query = query.lower()
            if 'jarvis' in query:
                return
        except Exception as e:
            print(e)
            print("Say that again please...")
    
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.live.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('iason57@hotmail.com', '6949265126....')
    parts = ("From: " + 'iason57@hotmail.com',
         "To: " + to,
         "Subject: Subject",
         "",
         content)    
    msg = '\r\n'.join(parts)
    server.sendmail('iason57@hotmail.com', to, msg)
    server.close()

def run_Jarvis(count):
    command = input()
    """
    ta apo panw tha mpoyn se sxclio
    """
    #print(takeCommand())
    #command = "play Boulevard Of Broken Dreams Green Day"
    command = command.lower()
    if 'jarvis' in command:
        if 'open file jarvis' in command:
            command = "open file jarvis"
        else:
            command = command.replace("jarvis","")
    print("Command : "+command)
    if 'what can you do' in command:
        li_commands = {
            "play song/youtube video": "Example: 'play Boulevard Of Broken Dreams Green Day'",
            "Close cortana": "Example: 'close cortana'",
            "time": "Example: 'what time it is?'",
            "music": "Example: 'play music'",
            "date": "Example: 'what date it is?'",
            "tell you who is": "Example: 'who is mahatma gandhi'",
            "Ask me if Im singe": "Example: 'are you single?'",
            "Ask me how I am ": "Example: 'How are you Jarvis'",
            "Teel me a joke": "Example: 'Do you know any jokes'",
            "Search wikipedia": "Example: 'Search wikipedia for cat'",
            "Search in Chrome": "Example: 'I want to search in chrome'",
            "Open facebook": "Example: 'Open Facebook'",
            "Open a site": "Example: 'Open site youtube.com'",
            "Open code": "Example: 'Jarvis open code'",
            "Open file": "Example: 'Jarvis open file <filename>'",
            "Open program": "Example: 'Open opera'",
            "Open mail": "Example: 'Open mail'",
            "Send mail": "Example: 'Send mail'",
            "Remember something": "Example: 'I want to remember something'",
            "Open my code": "Example: 'Open file jarvis'",
            "Shutdown computer": "Example: 'shutdown'",
            "Restart computer ": "Example: 'restart'",
            "Sleep computer ": "Example: ' sleep '",
            "Type something": "Example: 'type'",
            "Turn me off ": "Example: 'Go offline Jarvis'",
            "Ask about weather": "Example: 'How is the weather?'",
            "Change volume": "Example: 'Jarvis set volume 10/Jarvis set volume +10'"
        }
        ans = "I can do lots of things. See the list of commands-"
        print(ans)
        speak(ans)
        pprint.pprint(li_commands)
    elif 'hello' in command:
        speak('Hello sir...')
        print('Hello sir...')
    elif 'volume' in command:
        speak('Changing volume...')
        print('Changing volume...')
        command = command.replace("volume","")
        command = command.replace("set","")
        command = command.replace(" ","")
        os.system("setvol "+command)
    elif 'unmute' in command:
        command = command.replace(" ","")
        os.system("setvol "+command)
        speak('Unmuting ...')
        print('Unmuting ...')
    elif 'mute' in command:
        speak('Muting ...')
        print('Muting ...')
        command = command.replace(" ","")
        os.system("setvol "+command)
    elif 'standby' in command:
        speak('Standby mode activated...')
        print('Standby mode activated...')
        standby_()
        speak('Standby mode deactivated...')
        print('Standby mode deactivated...')
    elif 'play music' in command:
        speak('playing music...')
        print('Playing music...')
        pywhatkit.playonyt("Θέμης Αδαμαντίδης - Στην Καρδιά")
    elif 'play' in command:
        song = command.replace('play', '')
        speak('playing ' + song)
        print('Playing : ' + song)
        pywhatkit.playonyt(song)
    elif 'cortana' in command:
        speak('Closing cortana ...')
        print('Closing cortana ...')
        os.system("taskkill /im Cortana.exe /f")
    elif 'time' in command:
        time()
    elif 'date' in command:
        date()
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 5)
        print(info)
        speak(info)
    elif 'are you single' in command:
        speak('I am in a relationship with sirs wifi')
        print('I am in a relationship with sirs wifi')
    elif 'joke' in command:
        speak(pyjokes.get_joke())
    elif 'wikipedia' in command:
        speak('Searching Wikipedia...')
        command = command.replace("wikipedia", "")
        command = command.replace("search", "")
        command = command.replace("for", "")
        results = wikipedia.summary(command, sentences=5)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'search' in command and 'chrome' in command:
        speak("What should i search ?")
        print("What should i search ?")
        #search = takeCommand().lower()
        search = "where is California"
        speak("Searching "+search)
        print("Searching : "+search)
        search = search.replace(" ","+")
        what = "start www.google.com/search?q="+search
        os.system(what)
    elif 'facebook' in command:
        speak('Opening facebook...')
        print('Opening facebook...')
        os.system("start www.facebook.com")
    elif 'open site' in command:
        speak('Opening site...')
        print('Opening site...')
        command = command.replace("open", "")
        command = command.replace("site", "")
        command = command.replace(" ", "")
        what = ("start www."+command)
        os.system(what)
    elif 'open code' in command:
        speak('Opening code...')
        print('Opening code...')
        command = command.replace("open","")
        command = command.replace("code","")
        os.system("code.exe")
    elif 'open file jarvis' in command:
        speak('Opening my code...')
        print('Opening my code...')
        command = command.replace("open","")
        command = command.replace("file","")
        char_array = spliter(command)
        keyboard.press(Key.cmd)
        keyboard.press('s')
        keyboard.release(Key.cmd)
        keyboard.release('s')
        xronos.sleep(1)
        for i in char_array:
            keyboard.press(i)
            keyboard.release(i)
        keyboard.press(".")
        keyboard.release(".")
        keyboard.press("p")
        keyboard.release("p")
        keyboard.press("y")
        keyboard.release("y")
        xronos.sleep(1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    elif 'open file' in command:
        command = command.replace("open","")
        command = command.replace("file","")
        speak('Opening file ...')
        print('Opening site : p'+command)
        char_array = spliter(command)
        keyboard.press(Key.cmd)
        keyboard.press('s')
        keyboard.release(Key.cmd)
        keyboard.release('s')
        xronos.sleep(1)
        for i in char_array:
            keyboard.press(i)
            keyboard.release(i)
        xronos.sleep(1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    elif 'open' in command:
        print_command = command.replace("open","")
        speak('Opening '+print_command)
        print('Opening program : '+print_command)
        char_array = spliter(command)
        keyboard.press(Key.cmd)
        keyboard.press('c')
        keyboard.release(Key.cmd)
        keyboard.release('c')
        xronos.sleep(1)
        for i in char_array:
            keyboard.press(i)
            keyboard.release(i)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        keyboard.press(Key.alt)
        keyboard.press(Key.f4)
        keyboard.release(Key.alt)
        keyboard.release(Key.f4)
    elif 'type' in command:
        speak("What should i type ?")
        print("What should i type ?")
        command ="where is the dog"
        speak("You told me to type "+ command)
        print("You told me to type : "+ command)
        data = spliter(command)
        xronos.sleep(2)
        for i in data:
            keyboard.press(i)
            keyboard.release(i)
    elif 'mail' in command and 'send' in command:
        speak("Ok lets get started...")
        print("Ok lets get started...")
        try:
            speak("What should I say?...")
            print("What should I say?...")
            #content = takeCommand()
            while True:
                content = "test 1,2"
                speak(content)
                print("Content : "+content)
                speak("Is the content ok?...")
                #content = takeCommand()
                command = "yes"
                if(command == "yes"):
                    break
            speak("Who is the receiver?...")
            print("Who is the receiver?...")
            while True:
                to = 'xaralampossp13@gmail.com'
                speak(to)
                print("To : "+to)
                speak("Is the receiver correct?...")
                #content = takeCommand()
                command = "yes"
                if(command == "yes"):
                    break
            sendEmail(to,content)
            print("Sender : iason57@hotmail.com")
            print("Receiver : "+to)
            print("Periexomeno : "+content)
            speak("Email has been sent!")
            print("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Unable to send the email")
            print("Unable to send the email")
    elif 'remember' in command:
        speak("What should I remember?")
        print("What should I remember?")
        #data = takeCommand()
        data = "Helen Trab sucks"
        speak("you said me to remember that "+data)
        print("you said me to remember that "+data)
        remember = open('data'+str(count)+'.txt','w')
        remember.write(data)
        remember.close()
    elif 'shutdown' in command:
        print("Shutting down...")
        speak("Shutting down...")
        os.system("shutdown /s /t 5")
    elif 'sleep' in command:
        print("Sleeping...")
        speak("Sleeping...")
        os.system("sleep.lnk")
    elif 'restart' in command:
        print("Restarting...")
        speak("Restarting...")
        os.system("shutdown /r /t 5")
    elif 'offline' in command:
        print('Goodbuy sir!')
        speak('Goodbuy sir!')
        quit()
    elif 'how are you' in command:
        li = ['good', 'fine', 'great']
        response = random.choice(li)
        print("I am "+response+" sir.")
        speak("I am "+response+" sir.")
    elif 'how is the weather' and 'weather' in command:
        speak("Where?...")
        print("Where?...")
        #data = takeCommand()
        data = "Athens"

        url = "https://community-open-weather-map.p.rapidapi.com/weather"

        querystring = {"q":"Athens,Greece","lat":"0","lon":"0","callback":"test","id":"null","lang":"null","units":"\"metric\" or \"imperial\"","mode":"xml, html"}

        headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "232d2aa9eemsh1049aa99d984d53p18b94bjsnadc9ab201349"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        json_data = response.text
        json_data = json_data.replace("test(", "")
        json_data = json_data.replace(")", "")
        dictionary = json.loads(json_data)
        descreption = dictionary['weather'][0]['description']
        temp = dictionary['main']['temp']
        temp = temp- 273.15
        temp = round(temp,2)
        humidity = dictionary["main"]["humidity"]
        air = dictionary["wind"]["speed"]
        air = air * 0.27777777777778
        air = round(air,2)
        print(data)
        print("Description : "+descreption)
        print("Temperature : "+str(temp)+" degrees of Celcius")
        print("Humidity : "+str(humidity)+"percent")
        print("Air speed : "+str(air)+"kilometers per hour")
        speak(descreption)
        speak("Temperature , "+str(temp)+" degrees of Celcius")
        speak("Humidity , "+str(humidity)+"percent")
        speak("air speed, "+str(air)+"kilometers per hour")
    else:
        speak('Please say the command again.')
        print('Please say the command again.')

#wishme()
print("Initializing Jarvis")
# standby_() --> test standby
count = 0
while True:
    run_Jarvis(count)
    count += 1
    print(" ")

"""
Cortana run jarvis
exit
"""