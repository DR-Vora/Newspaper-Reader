import pyttsx3
import requests
import json

e = pyttsx3.init('sapi5')

v = e.getProperty('voices')
e.setProperty('voices',v[1].id) # there are 2 type audio inbuilt. One is male and another is Female and to access male voice we use index = 0 as v[0]
def speak(audio):
    e.say(audio)
    e.runAndWait()

if __name__=="__main__":
    speak("Hello, I am your assistant .And i am going to read news for you. Now the 1st News is by")

    url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=7e7a3d0035594f3686e9c934997f7ad3"

    news = requests.get(url).text
    news = json.loads(news)

    #print(news["totalResults"])

    arts = news['articles']

    for article in arts:
        print(article['author'])
        speak(article['author'])
        print(article['title'])
        speak(article['title'])
        print(article['description'])
        speak(article['description'])
        speak("Moving to the next news which is by ")
        