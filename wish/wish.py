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
    hour = int(x.strftime('%H'))
    p = x.strftime('%p')
    if hour >= 4 and hour < 12: 
        speak("Good morning sir")
    elif hour >= 12 or hour < 17:
        speak("good afternoon sir")
    elif hour >= 17 or hour < 20:
        speak("good evening sir")
    elif hour >= 20 or hour < 4:
        speak("its time to spleep sir")
    else:
        speak("hello  sir")
