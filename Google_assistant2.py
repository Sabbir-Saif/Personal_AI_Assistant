#python speech recognition ("pip install SpeechRecognition") search dilum on Terminal
#"pip install pyttsx3" on Terminal
#"pip install PyAudio" on Terminal
#pip install pywhatkit on Terminal
import datetime
import wikipedia
import speech_recognition as sr
import pyttsx3
#import pywhatkit
listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
   engine.say(text)
   engine.runAndWait()

def take_command():
  try:
    with sr.Microphone() as source:
        print("Hey Sexy,,,Say something Horny......")
        voice=listener.listen(source)
        command=listener.recognize_google(voice)
        command=command.lower()
        print(command)
        if 'alexa' in command:
            command=command.replace('alexa',"")
            print(command)

  except:
    print("Unknown error occured")
  return command

def run_alexa1():
  try:
    command=take_command()
    if 'play' in command:
        command.replace('play',"")
        talk("playing "+command)
        pywhatkit.playonyt(command)
    elif 'date' in command:
        date=datetime.datetime.date()
        #talk("Today's date is: "+ str(date))
    elif 'who' in command or 'what' in command:
        info=wikipedia.summary(command,5)
        print(info)
        talk(info)
    elif 'colour' in command:
        pywhatkit.search('https://toffeelive.com/#video/5d50889672f6f860d14f502de3de1957')
    else:
        pywhatkit.search(command)
  except:
      talk('Unknown Error Occured')

def run_alexa(command):
  #try:
    if 'play' in command:
        command=command.replace('play'," ")
        talk("playing "+command)
        pywhatkit.playonyt(command)
    elif 'date' in command:
        date=datetime.datetime.date()
        #talk("Today's date is: "+ str(date))
    elif 'who' in command or 'what' in command:
        info=wikipedia.summary(command,sentences=15)
        talk('According to Wikipedia.')
        print(info)
        talk(info)
    elif 'colour' in command:
        pywhatkit.search('https://toffeelive.com/#video/5d50889672f6f860d14f502de3de1957')
    else:
        pywhatkit.search(command)
  #except:
      #talk('Unknown Error Occured')

if __name__=='__main__':
      run_alexa1()