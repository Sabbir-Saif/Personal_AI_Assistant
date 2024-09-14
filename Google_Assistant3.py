import tkinter
import datetime
import webbrowser
import sys
#import pyjokes
import pywhatkit
import requests
import speech_recognition as sr
import pyttsx3
import wikipedia
import wolframalpha
import os
import cv2
import random
from requests import get
import Google_assistant2 as ai2
import smtplib
#import pyjokes
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) #0=male 1,2=female
activationWord='siri'

#######################
#######################

#configure browser
chrome_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))

def speak(text, rate=175): #talking
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate',rate)
    engine.say(text)
    engine.runAndWait()


def parse_command(phrase_time_limit=5):   #Speech recognize kore sheta print korbe
    listener = sr.Recognizer()
    print('Listening to a command')
    try:
      with sr.Microphone() as source:
        #listener.adjust_for_ambient_noise(source,duration=120)
        listener.pause_threshold=1
        input_speech=listener.listen(source,timeout=600,phrase_time_limit=3600)
        print('Recognizing Speech...')
        query=listener.recognize_google(input_speech,language='en')   #en_us, bn(bengali)
        print(f'The input speech was : {query}')
        speak(f'You said : {query}')
    except Exception as exception:
        print("I didn't quite catch that.")
        speak("I didn't quite catch that.")
        print(exception)
        return 'None'
    return query


def wish():
    hour=int(datetime.datetime.now().hour)
    time=datetime.datetime.today().strftime("%H:%M %p ")
    if hour>=6 and  hour<12:
        speak('Good Morning, Refath! It is '+time+ '.')
    elif hour>=12 and hour<16:
        speak('Good Noon, Refath! It is '+time+ '.')
    elif hour>=16 and hour<21:
        speak('Good evening, Refath! It is '+time+ '.')
    else: speak('Hey! Are you sleepy, Refath? It is '+time+'. This is almost time for your bed.')
    speak("Hey, I'm "+activationWord+". Your personal AI Assistant. How can I help?")

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('u1802171@student.cuet.ac.bd','#sabbireridentity#18eee171secC')
    server.sendmail('Your email id',to,content)
    server.close()

def location():
    try:
        ipad=requests.get("https://api.ipify.org").text
        #print(ipad)
        url="https://get.geojs.io/v1/ip/geo/"+ipad+'.json'
        geo_req=requests.get(url)
        geo_data=geo_req.json()
        #print(geo_data)
        city=geo_data['timezone'][:4]
        region=geo_data['timezone'][5:]
        country=geo_data['country']
        print(f"Your location is : {region}, {city}, {country}.")
        speak(f"Your location is : {region}, {city}, {country}.")

    except: speak('Sorry. Did not get it.')

def youtube_automation():
    take=parse_command().lower().split()
    import keyboard
    if 'pause' in take: keyboard.press('space bar')
    elif 'restart' in take: keyboard.press('0')
    elif 'mute' in take: keyboard.press('m')
    elif 'full screen' in take: keyboard.press('f')
    elif 'back' in take: keyboard.press('j')
    elif 'skip' in take: keyboard.press('l')
    elif 'film mode' in take: keyboard.press('t')

def chrome_automation():
    take = parse_command().lower().split()
    import keyboard
    if 'close' in query: keyboard.press_and_release('ctrl+w')
    elif 'open new tab' in query.join(" ")  or 'open new' in query.join(" "): keyboard.press_and_release('ctrl+t')
    elif 'open new window' in query.join(" ") : keyboard.press_and_release('ctrl+n')
    elif 'history' in query:
        keyboard.press_and_release('ctrl+h')

def alarm():
    speak('Enter the time')
    time=input('Time : ')
    while True:
        time_ac=datetime.datetime.now()
        now=time_ac.strftime("%H:%M:%S")
        if now==time:
          z=""
          while 'stop' not in z:
            speak('Time to wake up, Sir!')
            from playsound import playsound
            playsound("C:\\Users\\u1802\\Downloads\\alarm.wav")
            z=parse_command().lower().split()

web=['facebook','twitter','cuet','youtube','google','toffee','cricbuzz','pycharm']
websites=['www.facebook.com','www.twitter.com','www.cuet.ac.com','www.youtube.com','www.google.com',"https://toffeelive.com/","https://www.cricbuzz.com/",'https://www.jetbrains.com/pycharm/']
sample=['notepad','messenger','camera','music']



'''Main Loop'''

if __name__=='__main__' :  #Only ei file run korlei eta run hbe. Onno file thke import korle eta run hbe na
     #speak('All systems nominal.')
     wish()
     while input('Want to continue with me? \n1=YES\n2=NO\n')=='1':
         # parse as a list
             query=parse_command().lower().split()
             #query='screenshot'.lower().split()
             if query[0]==activationWord: #alexa say hello bolte hobe nahoy kaj korbe na
                  query.pop(0)

            #list Commands
             if 'hello' in query or 'hi' in query :
                     print('Greetings, All.')
                     speak('Greetings, All.')
                     continue
             else:
                     speech=' '.join(query)
                     speak(speech)
             if query[0]=='go' and query[1]=='to':
                 speak('Opening')
                 query=" ".join(query[2:])
                 webbrowser.get('chrome').open_new(query)
             elif 'notepad' in query:
               if 'open' in query:
                 npath="C:\\Windows\\System32\\notepad.exe"    #Double slash required
                 os.startfile(npath)
               else:
                 speak('okay Sir, Closing notepad.')
                 os.system("taskkill /f /im notepad.exe")
             elif 'command prompt'  in query:
                 os.system("start cmd")
             elif 'camera' in query:
                 cap=cv2.VideoCapture(0)
                 while True:
                     ret,img=cap.read()
                     cv2.imshow('webcam',img)
                     k=cv2.waitKey(50)
                     if k==27: break;
                 cap.release()
                 cap.destroyAllWindows
             elif 'music' in query:
                 music_dir="C:\\Users\\u1802\\music"
                 songs=os.listdir(music_dir)
                 rd=random.choice(songs)
                 '''for song in songs:
                     if song.endswith(".mp3"):
                         os.startfile(os.path.join(music_dir,song))''' # When there are various type items
                 os.startfile(os.path.join(music_dir,rd))

             elif 'ip' in query and "address" in query:
                 print(query)
                 ip=get("https://api.ipify.org").text
                 speak(f"Your IP adress is {ip}")
                 print(ip)
             elif 'cricbuzz' in query or 'cricket' in query:
                    import cricbuzzdotcom
                    webbrowser.open(cricbuzzdotcom.site)
                    while 'stop' not in query:
                             speak("Hey, What should I show you from cricbuzz.")
                             query=parse_command().lower().split()
                             cricbuzzdotcom.website(query)
                    continue
             elif 'screenshot' in query or 'ss' in query:
                 import pyautogui
                 c=pyautogui.screenshot()
                 c.save('C:\\Users\\u1802\\OneDrive\\Desktop\\New folder\\ss.png')

             elif 'open' in query:
                 if 'messenger' in query:
                     os.startfile('C:\\Users\\u1802\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Messenger')
                 elif 'pycharm' in query:
                     os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.1\\bin\\pycharm64.exe")
                 elif 'youtube' in query:
                     import youtube
                     webbrowser.open(youtube.site)
                     while 'stop' not in query:
                         speak('Wanna listen a song? Or tell me should I open a channel.')
                         query=parse_command().lower().split()
                         speak('Tell me the song name, you wish to listen. Or you may tell the channel name I need to open. ')
                         song=parse_command().lower().split()
                         youtube.youtube(query,song)
                 else:
                  for i in web:
                     if i in query:
                       index=web.index(i)
                       webbrowser.open(websites[index])
                       speak("Hey, What should I show you from"+i)
                       cmd=parse_command().lower()
                       webbrowser.open(f"{cmd}")
                       if index==len(web)-1: ai2.run_alexa(query)

             elif 'close' in query:
                 for i in query:
                     if i in sample:
                         got=i
                 speak('okay Sir, Closing'+got)
                 os.system('taskkill /f /im '+got+".exe")
             elif 'whatsapp' in query:
                 if 'message' in query:
                     if 'send' in query:
                         pywhatkit.sendwhatmsg("+8801864912224","Fuck You Rubish.",2,25)
             elif 'email' in query:
                 if '046' in query:  #Google account/less secure apps on korba,,otherwise kaj korbena
                     speak('What should I say?')
                     content=parse_command().lower()
                     to='u1802046@student.cuet.ac.bd'
                     sendEmail(to,content)
                     speak('Email has been sent to Mahir Faisal.')
             elif 'joke' in query:
                 if 'tell' in query or 'say' in query:
                     joke=pyjokes.get_jokes('en')
                     print(joke)
                     speak(joke)
             elif "no" in query and 'thanks' in query:
                     speak('Thanks for using me. Have a good day,Sir.')
                     sys.exit()
             elif 'shut' in query:
                 if 'window' in query or 'pc' in query or 'computer' in query or 'program' in query:
                     os.system("shutdown /s /t 5")
             elif 'restart' in query:
                 if 'window' in query or 'pc' in query or 'computer' in query or 'program' in query:
                     os.system("shutdown /r /t 5")
             elif 'sleep' in query:
                     os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
             elif 'location' in query:
                 speak('Let me try, Sir!')
                 location()
             elif 'bbc' in query:
                 speak('opening')
                 from new import auto_webs
                 webbrowser.open('https://www.bbc.com/')
                 while 'stop' not in query:
                     speak("Hey, What should I show you from cricbuzz.")
                     query = parse_command().lower().split()
                     auto_webs(query)
             elif 'alarm' in query:
                 alarm()
             else:
                 query = " ".join(query)
                 print(query)
                 ai2.run_alexa(query)