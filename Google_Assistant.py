#python speech recognition ("pip install SpeechRecognition") search dilum on Terminal
#"pip install pyttsx3" on Terminal
#"pip install PyAudio" on Terminal

import speech_recognition as sr
import pyttsx3
listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say("I am Alexa!")
engine.say("What can I do for you?")
engine.runAndWait()
try:
    with sr.Microphone() as source:
        print("Hey Sexy,,,Say something Horny......")
        voice=listener.listen(source)
        command=listener.recognize_google(voice)
        print(command)
        if 'Alexa' in command:
            engine.say(command)
            engine.runAndWait()
            print('THANK You from ALEXA :)')
except:
    print("Unknown error occured")