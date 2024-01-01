import pyttsx3
import datetime
from datetime import datetime

x=datetime.now()
t = x.strftime('%I:%M:%p')
y = x.year

engine=pyttsx3.init('sapi5')
engine.setProperty('rate',190)
engine.setProperty('volume',100)
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish():
    hour = x.strftime('%I')
    p = x.strftime('%p')
    if 'AM' in p: 
        speak("Good morning sir")
    else:
        if hour >= 12 and hour < 17:
            speak("good afternoon sir")
        elif hour >= 17 and hour < 20:
            speak("good evening sir")
        else:
            speak("hello  sir")