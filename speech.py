import speech_recognition as sr
import webbrowser as wb
import pyttsx3 
chrome_path = "content\\Google\\Chrome\\Application\\chrome.exe %s"
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
with sr.Microphone() as source:
    print("Say something")
    audio = r.listen(source, timeout=3)
    print('Done')

text = r.recognize_google(audio, show_all=False)
if text:
    print('Sarah thinks you said ---> ' + text)
    #speaking mode
    engine.say("opening browser saver")
    engine.runAndWait()
    search_url = 'https://www.google.com/search?q=' + text
    print("Opening the browser...")
    wb.open(search_url, new=2)  
else:
    print("Google Speech Recognition could not understand audio")
