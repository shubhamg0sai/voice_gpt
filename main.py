import datetime
from datetime import datetime
from wish.wish import speak , wish
from voiceinp.voiceinp import voiceinp
from ai.ai import ai

x=datetime.now()
t = x.strftime('%I:%M:%p')
y = x.year
d = x.strftime('%A')
wish()
if __name__ == '__main__':
    while True:
        print (t, y)
        print(d)
        query = voiceinp().lower()
        ans = ai(query)
        print(ans)
        speak(ans)