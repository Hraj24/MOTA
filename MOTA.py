import os
import webbrowser as wb
import wikipedia    #pip install wikipedia
import pyttsx3  #pip install pyttsx3
import datetime
import speech_recognition as sr   #pip install SpeechRecognition
import smtplib
import pyautogui   #pip intall pyautogui
import pyjokes   #pip install pyjokes
#import pywhatkit as kit
import psutil  #pip install psutil



engine=pyttsx3.init()


Lady_english="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
#Lady_spanish="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\"TTS_MS_ES-ES_HELENA_11.0"


def speak(audio):
    engine.setProperty('voice',Lady_english)
    engine.say(audio)
    engine.runAndWait()
    engine.setProperty('rate',150)
    engine.setProperty('volume',45)

#speak("Hello, I am MOTA, your personal assistant. How can I help you?")




def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is") 
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back sir!")
    time() 
    date()
    hour= datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good morning sir!")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir!")
    elif hour>=18 and hour<24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")

    speak("MOTA at your service. Please tell me how can i help you?")


def takeCommand():
   
    r=sr.Recognizer()
    #sr.pyaudio_module=sr.get_pyaudio()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
        
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Sat that again Plese...")

        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('harahjha2002@gmail.com','password')
    server.sendmail('harahjha2002@gmail.com',to,content)
    server.close()



def screenshot():
    img=pyautogui.screenshot()
    img.save("C:\\Users\\Harsh\\Desktop\\MOTA\\Screenshot.png")


def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at"+usage)
    battery=psutil.sensors_battery()
    speak("Battery is at"+str(battery.percent)+"%")
    avgload=psutil.getloadavg()
    speak("Average load is"+str(avgload))
    memory=psutil.virtual_memory()
    speak("Memory is"+str(memory.percent)+"occupied")


def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    wishme()
    while True:
        query=takeCommand().lower()
        if 'open google' in query:
            wb.open("google.com")

        elif 'open youtube' in query:
            wb.open("youtube.com")

        elif 'open stackoverflow' in query:
            wb.open("stackoverflow.com")

        elif 'open github' in query:
            wb.open("github.com")

        elif 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'open code' in query:
            codepath="C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VSCode\\Code.exe"
            os.startfile(codepath)

        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'play music' in query:
            music_dir="C:\\Users\\HP\\Music\\Songs"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="harshrajjha200224@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Harsh. I am not able to send this email")
        
        elif 'search in chrome' in query:
            speak("What should I search?")
            chromepath="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            search=takeCommand().lower()
            wb.open_new_tab(search+'.com')
        
        elif 'logout' in query:
            os.system("shutdown -l")
        
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        
        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        
        elif 'remember that' in query:
            speak("What should I remember?")
            data=takeCommand()
            speak("You asked me to remember that"+data)
            #remember=data
            remember=open('data.txt','w')
            remember.write(data)
            remember.close()

        
        elif 'do you know anything' in query:
            remember=open('data.txt','r')
            speak("You asked me to remember that"+remember.read())


        elif 'screenshot' in query:
            screenshot()
            speak("Done!")

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()


        elif 'offline' in query:
            speak("Good Bye Sir!")
            quit()
            

        




#takeCommand()
#wishme()
#date()
#time()


