import speech_recognition as sr
import pyttsx3
import os
import datetime
import subprocess
import sys
import pywhatkit 

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer  = sr.Recognizer() 

def speak(text):
    engine.say(text)
    engine.runAndWait()

def open_software(software_name):
    if 'chrome' in software_name:
        speak('Opening Chrome...')
        program = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([program])

    elif 'microsoft edge' in software_name:
        speak('Opening Microsoft Edge...')
        program = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        subprocess.Popen([program])

    elif 'play' in software_name:
        b='Opening Youtube'
        engine.say(b)
        engine.runAndWait()
        pywhatkit.playonyt(software_name)

    elif 'notepad' in software_name:
        speak('Opening Notepad...')
        subprocess.Popen(['notepad.exe']) 
    elif 'calculator' in software_name:
        speak('Opening Calculator...')
        subprocess.Popen(['calc.exe'])
    else:
        speak(f"I couldn't find the software {software_name}")

def close_software(software_name):
    if 'chrome' in software_name:
        speak('Closing Chrome...')
        os.system("taskkill /f /im chrome.exe")

    elif 'microsoft edge' in software_name:
        speak('Closing Microsoft Edge...')
        os.system("taskkill /f /im msedge.exe")

    elif 'notepad' in software_name:
        speak('Closing Notepad...')
        os.system("taskkill /f /im notepad.exe")
    elif 'calculator' in software_name:
        speak('Closing Calculator...')
        os.system("taskkill /f /im calculator.exe")
    else:
        speak(f"I couldn't find any open software named {software_name}")

def listen_for_wake_word():
    with sr.Microphone() as source:
        print('Listening for wake word...')
        while True:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            recorded_audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(recorded_audio, language='en_US')
                text = text.lower()
                if 'jarvis' in text:
                    print('Wake word detected!')
                    speak('Hi Sir, How can I help you?')
                    return True
            except Exception as ex:
                print("Could not understand audio, please try again.")

def cmd():
    with sr.Microphone() as source:
        print('Clearing background noise... please wait!')
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Ask me anything...')
        recorded_audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(recorded_audio, language='en_US')
        text = text.lower()
        print('Your message:', text)
    except Exception as ex:
        print(ex)
        return

    if 'stop' in text:
        speak('Stopping the program. Goodbye!')
        sys.exit()
    if 'open' in text:
        software_name = text.replace('open', '').strip()
        open_software(software_name)
    elif 'close' in text:
        software_name = text.replace('close', '').strip()
        close_software(software_name)
    elif 'time' in text:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        print(current_time)
        speak(current_time)
    elif 'who is god' in text:
        speak('Ajitheyyy Kadavuleyy')
    elif 'what is your name' in text:
        speak('My name is Jarvis Your Artificial Intelligence')

while True:
    if listen_for_wake_word():
        while True: 
            if cmd():
                break
