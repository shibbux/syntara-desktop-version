import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install speechrecogniton

def speak(Text):
    engine = pyttsx3.init("sapi5") 
    voice = engine.getProperty("voices") 
    engine.setProperty("voice", voice[0].id)
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
