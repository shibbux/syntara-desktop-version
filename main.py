
import bs4, requests, datetime, webbrowser  # pip install bs4 requests pyautogui webbrowser datetime googlenews -> cmd
from pyautogui import *
import pywhatkit as kit # pip install pywhatkit -> cmd
import speedtest # pip install speedtest-cli -> cmd
#######################################

import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install speechrecogniton



def speak(Text):
    engine = pyttsx3.init("sapi5")
    voice = engine.getProperty("voices")
    engine.setProperty("voice", voice[1].id)
    engine.setProperty("rate", 200)
    print(f"jarvis: {Text}")
    engine.say(text=Text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("  ")
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source, phrase_time_limit=3)

        try:
            print("  ")
            print("Recognizing...")
            print("  ")
            query = r.recognize_google(audio, language="en-in")
            print(f"You: {query}")

        except Exception as e:
            print(e)
            return ""
        return query.lower()


##################################
def tasks():
    while True:
        query = listen() # jo mai bolne wala hu
        query = query.replace("jarvis","")

        if "time" in query:
            # time = datetime.datetime.now().strftime("%H:%M:%S %p") # 24 hour format
            time = datetime.datetime.now().strftime("%I:%M:%S %p") # 12 hour format
            speak(time)

        elif "your name" in query:
            speak("my name is syntaara")
        
        elif "date" in query:
            date = datetime.datetime.now().strftime("%D")
            speak(date)
            
        elif "day" in query:
            day = datetime.datetime.now().strftime("%A")
            speak(day)

        elif "temperature" in query:
            q = "temperature in faridabad"
            r = requests.get(f"https://www.google.com/search?q={q}")
            data = bs4.BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"the temperature outside is {temp}")
            
            speak("do you want another place temperature")
            place = listen()
            if "yes" in place:
                speak("tell me the name of the place")
                next = listen()
                r = requests.get(f"https://www.google.com/search?q={next}")
                data = bs4.BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"the temperature outside is {temp}")
            else:
                speak("no problem!")

        elif "open" in query: 
            query = query.replace("open","")
            press("win")
            sleep(.2)
            typewrite(query)
            sleep(.2)
            press("enter")

        elif "play" in query: 
            query = query.replace("play ","")
            kit.playonyt(query)
            speak(f"ok boss, playing {query}")

        elif "website" in query: 
            query = query.replace("website","") 
            query = query.replace(" ","") 
            webbrowser.open(f"https://www.{query}.com")
            speak(f"ok boss, opening {query}")
            
        # elif "news of" in query:
        #     query = query.replace("news of ","")
        #     new = GoogleNews.GoogleNews()
        #     speak(f"getting news of {query}")
        #     new.get_news(query)
        #     new.result()
        #     a = new.gettext()
        #     speak(a[1:5])

        # elif "headlines" in query or "headline" in query:
        #     new = GoogleNews.GoogleNews()
        #     speak("getting fresh headlines")
        #     new.get_news("headlines")
        #     new.result()
        #     a = new.gettext()
        #     speak(a[1:10])
        
        elif "speed test" in query:
            speed = speedtest.Speedtest()
            speak("checking")
            ul = speed.upload()
            ul = int(ul/800000)
            dl = speed.download()
            dl = int(dl/800000)
            speak(f"your upload speed is {ul} mbp s and your download speed is {dl} mbp s")
        
tasks()
