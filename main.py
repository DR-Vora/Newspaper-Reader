import pyttsx3
e = pyttsx3.init('sapi5')

v = e.getProperty('voices')
e.setProperty('voices',v[1].id) # there are 2 type audio inbuilt. One is male and another is Female and to access male voice we use index = 0 as v[0]
def speak(audio):
    e.say(audio)
    e.runAndWait()

if __name__=="__main__":
    speak("Hello, I am your assistant")