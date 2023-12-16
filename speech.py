import speech_recognition as sr
import webbrowser as wb

chrome_path = "content\\Google\\Chrome\\Application\\chrome.exe %s"
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something")
    audio = r.listen(source, timeout=3)
    print('Done')

text = r.recognize_google(audio, show_all=False)
if text:
    print('Sarah thinks you said ---> ' + text)
    search_url = 'https://www.google.com/search?q=' + text
    print("Opening the browser...")
    wb.open(search_url, new=2)  
else:
    print("Google Speech Recognition could not understand audio")
