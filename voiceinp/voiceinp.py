from wish.wish import speak
import speech_recognition as sr

def voiceinp():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 0.6
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
    except Exception:
        query = ' '
        speak('Sorry, I could not understand. Could you please say that again?')
    return query