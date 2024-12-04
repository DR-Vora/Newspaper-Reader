# 📰 Newspaper Reader

A Python-based Newspaper Reader that fetches the latest news headlines and reads them aloud using text-to-speech technology. It combines the power of **News API** with the Python `pyttsx3` library for a fully automated, voice-assisted news-reading experience.  

---

## ✨ Features

- Fetches the latest news headlines from **TechCrunch** via the **News API**.
- Reads out:
  - News author.
  - Title of the article.
  - Description of the article.
- Customizable voice settings:
  - Male and female voices available.
  - Adjustable speech rate for better clarity.
- Text-to-speech functionality powered by `pyttsx3`.

---

## 📋 Prerequisites

### Libraries Used
- **`pyttsx3`**: For text-to-speech functionality.
- **`requests`**: To fetch data from the News API.
- **`json`**: To parse the news data in JSON format.

### Installation
To install the required libraries, run:
```bash
pip install pyttsx3 requests
```

---

## 🚀 How to Use

1. **Get a News API Key**:
   - Visit [News API](https://newsapi.org/) and sign up for a free account.
   - Generate an API key for accessing news data.
   - Replace the placeholder API key (`7e7a3d0035594f3686e9c934997f7ad3`) in the script with your own API key.

2. **Run the Script**:
   ```bash
   python newspaper_reader.py
   ```

3. The assistant will fetch and read the latest news headlines for you.

---

## 🛠️ Code Overview

```python
import pyttsx3
import requests
import json
import time

e = pyttsx3.init('sapi5')
v = e.getProperty('voices')
e.setProperty('voices', v[1].id)  # Use female voice (v[0] for male)
e.setProperty('rate', e.getProperty('rate') - 50)  # Slow down speech rate

def speak(audio):
    e.say(audio)
    e.runAndWait()

if __name__ == "__main__":
    speak("Hello, I am your reading assistant. And I am going to read news for you. Now the 1st News is by")

    url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=YOUR_API_KEY"

    news = requests.get(url).text
    news = json.loads(news)

    arts = news['articles']

    for article in arts:
        print(article['author'])
        speak(article['author'])
        print(article['title'])
        speak(article['title'])
        print(article['description'])
        speak(article['description'])

        time.sleep(1)  # Delay for better pacing
        speak("Moving to the next news which is by ")
```

---

## 🖥️ Example Usage

### Input
- No user input required; the script automatically fetches news articles.

### Output
- The assistant will:
  - Speak and display the author, title, and description of each news article.
  - Pause briefly before moving to the next article.

Example:
```
Hello, I am your reading assistant. And I am going to read news for you. 
Now the 1st News is by TechCrunch.
The Future of AI: 10 Predictions for 2025.
AI is evolving rapidly, and here are the top trends to watch.
Moving to the next news which is by ...
```

---

## 📅 Improvements and Future Additions

- Add support for multiple news sources or categories.
- Enable user input to choose the source or type of news.
- Provide options for summarizing or skipping news articles.
- Make it cross-platform by adapting the sound feature for non-Windows systems.

---

## 🛡️ Limitations

- The API key must be valid and active for the script to work.
- The news source is currently fixed to **TechCrunch**.
- `winsound` is Windows-specific; the script's sound notifications may not work on other operating systems.

---

## ✍️ Author

- **Dhairya Vora**  
  📧 **Email**: voradhairya22@gmail.com 
  👉 **LinkedIn**: [Dhairya Vora](https://www.linkedin.com/in/dhairya-vora-475577275)
