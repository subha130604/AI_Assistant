import pyautogui
import speech_recognition as sr
import pyttsx3
import pywhatkit
import pywhatkit as kit
import datetime
import pyjokes
import webbrowser
import requests
import wikipedia
import os
import subprocess
import psutil
import time
from ecapture import ecapture as ec


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with (sr.Microphone() as source):
            print('listening...!!!')
            listener.pause_threshold = 1
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print(" Hey Good morning")
        talk("Hey Good morning")
    elif hour>=12 and hour<18:
        print("Hey Good Afternoon")
        talk("Hey Good Afternoon")
    else:
        print("Hey Good Evening")
        talk("Hey Good Evening")
    print("I am fores . please tell me how can i help you")
    talk("I am fores . please tell me how can i help you")

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"

    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

def condition():
    usage = str(psutil.cpu_percent())
    talk("CPU is at" + usage + " percentage")
    battray = psutil.sensors_battery()
    percentage = battray.percent
    talk("our system have {percentage} percentage Battery")
    if percentage >= 75:
        talk("we could have enough charging to continue our work")
    elif percentage >= 40 and percentage <= 75:
        talk("we should connect out system to charging point to charge our battery")
    elif percentage >= 15 and percentage <= 30:
        talk("we don't have enough power to work, please connect to charging")
    else:
        talk(" we have very low power, please connect to charging otherwise the system will shutdown very soon")

def scshot():
    talk("please tell me the name for this screenshot file")
    name = take_command()
    talk("Please hold the screen for few seconds, I am taking screenshot")
    time.sleep(3)
    img = pyautogui.screenshot()
    img.save(f"{name}.png")
    talk("I am done, the screenshot is saved in main folder.")

def OpenApp(command):
    if 'calculator' in command:
        talk("Opening calculator")
        os.startfile("C:\\Windows\\System32\\calc.exe")
    elif 'notepad' in command:
        talk("Opening notepad")
        os.startfile("C:\\Windows\\notepad.exe")
    elif 'editor' in command:
        talk("Opening your Visual studio code")
        os.startfile("C:\\Users\\SUBHA\\OneDrive\\Desktop\\Visual Studio Code.lnk")
    else:
        talk("no such item")

def CloseApp(command):
    if ('notepad' in command):
        talk("okay closing notepad")
        os.system("taskkill /f /im notepad.exe")
    elif ('editor' in command):
        talk("okay closing vs code")
        os.system("taskkill /f /im Code.exe")
    else:
        talk("no such item")

def Google_Apps(command):
    if 'gmail' in command:
        talk('opening your google gmail')
        webbrowser.open('https://mail.google.com/mail/')
    elif 'maps' in command:
        talk('opening google maps')
        webbrowser.open('https://www.google.co.in/maps/')
    elif 'news' in command:
        talk('opening google news')
        webbrowser.open('https://news.google.com/')
    elif 'calendar' in command:
        talk('opening google calender')
        webbrowser.open('https://calendar.google.com/calendar/')
    elif 'photos' in command:
        talk('opening your google photos')
        webbrowser.open('https://photos.google.com/')
    elif 'documents' in command:
        talk('opening your google documents')
        webbrowser.open('https://docs.google.com/document/')
    elif 'spreadsheet' in command:
        talk('opening your google spreadsheet')
        webbrowser.open('https://docs.google.com/spreadsheets/')
    else:
        talk("no such item")



def run_fores():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time1 = datetime.datetime.now().strftime('%I:%M %p')
        print('current time is ' + time1)
        talk('current time is ' + time1)

    elif 'date' in command:
        date = datetime.datetime.now().strftime('%B %d %Y')
        print('the date is ' + date)
        talk('the date is ' + date)

    elif 'day' in command:
        day = datetime.datetime.now().strftime('%A')
        print('the day is ' + day)
        talk('the day is ' + day)

    elif 'can we go out' in command:
        talk('sorry, i have a headache')

    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    elif 'are you real' in command:
        talk('no,im virtual')

    elif 'how are you' in command:
        talk('i am fine, what about you?')

    elif 'i am fine' in command:
        talk('good.how can i help you...')

    elif 'what can you do' in command:
        talk('I talk with you until you want to stop, I can say time, open google browser,and I can also open your college websites, I can search for some thing in google and I can tell jokes')

    elif 'your age' in command:
        talk('I am very younger than you')

    elif 'are you there' in command:
        talk('Yes, I am here.what i want to assist for today...')

    elif 'tell me something' in command:
        talk('you are the most beautiful person in the world...smile and start... today is a brand new day')

    elif 'thank you' in command:
        talk(' I am here to help you..., your welcome')

    elif 'what will you do when you get bored' in command:
        talk('hey, I will be listening to all your words at any time..')

    elif 'i love you' in command:
        talk('I love you too dear...')

    elif 'do you ever get tired' in command:
        talk('It would be impossible to tire of our conversation')

    elif 'can you hear me' in command:
        talk('Yes, I can hear you')

    elif 'your name' in command:
        talk('My name is fores')

    elif "system condition" in command:
        talk("checking the system condition")
        condition()

    elif ('open calculator' in command) or ('open notepad' in command) or ('open editor' in command):
        OpenApp(command)

    elif ('close notepad' in command) or ('close editor' in command):
        CloseApp(command)

    elif ('open gmail' in command) or ('open maps' in command) or ('open calendar' in command) or (
            'open documents' in command) or ('open spreadsheet' in command) or (
            'open photos' in command) or ('open news' in command):
        Google_Apps(command)

    elif 'open hotstar' in command:
        talk('opening your disney plus hotstar')
        webbrowser.open('https://www.hotstar.com/in')

    elif 'open prime' in command:
        talk('opening your amazon prime videos')
        webbrowser.open('https://www.primevideo.com/')

    elif 'open netflix' in command:
        talk('opening Netflix videos')
        webbrowser.open('https://www.netflix.com/')

    elif 'open ms word' in command:
        talk('opening ms word')
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\Word.lnk")

    elif 'open ms excel' in command:
        talk('opening ms excel')
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk")

    elif 'open ms powerpoint' in command:
        talk('opening ms powerpoint')
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk")

    elif 'open github' in command:
        talk('opening your github')
        webbrowser.open('https://github.com/subhasri0311')

    elif 'news' in command:
        webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
        talk('Here are some headlines from the Times of India, Happy reading')
        time.sleep(6)

    elif 'flipkart' in command:
        talk('Opening flipkart online shopping website')
        webbrowser.open("https://www.flipkart.com/")

    elif 'amazon' in command:
        talk('Opening amazon online shopping website')
        webbrowser.open("https://www.amazon.in/")

    elif 'location' in command:
        talk('What is the location?')
        location = take_command()
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        talk('Here is the location ' + location)

    elif 'show power battery' in command:
        power_battery = psutil.sensors_battery()
        battery_percentage = power_battery.percent
        print(battery_percentage)
        talk('The system have + battery_percentage + percent battery')

    elif 'open microsoft edge' in command:
        talk('opening your Microsoft edge')
        os.startfile("C:\\Users\\Public\\Desktop\\Microsoft Edge.lnk")

    elif 'volume up' in command:
        pyautogui.press('volumeup')
        talk("volume increased")

    elif 'volume down' in command:
        pyautogui.press('volumedown')
        talk("volume decreased")

    elif 'volume mute' in command:
        pyautogui.press('volumemute')
        talk("volume muted")

    elif "change password" in command:
        talk("What is the new password")
        new_pw = input("Enter New Password: ")
        new_password = open("password.txt", "w")
        new_password.write(new_pw)
        new_password.close()
        talk("Password changed successfully")
        print("Password changed successfully")

    elif 'send whatsapp message' in command:
        talk("On what number should I send the message sir? Please enter in the console: ")
        number = input("Enter the number: ")
        talk("What is the message?")
        message = take_command().lower()
        send_whatsapp_message(number, message)
        talk("I've sent the message.")
        print("I've sent the message.")

    elif 'advice' in command:
        talk("Here's an advice for you")
        advice = get_random_advice()
        talk(advice)
        talk("For your convenience, I am printing it on the screen.")
        print(advice)

    elif 'weather' in command:
        city = "erode"
        res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=16f0afad2fd9e18b7aee9582e8ce650b&units=metric").json()
        temp1 = res["weather"][0]["description"]
        temp2 = res["main"]["temp"]
        print(f"Temperature is {format(temp2)} degree Celsius \nWeather is {format(temp1)}")
        talk(f"Temperature is {format(temp2)} degree Celsius \nWeather is {format(temp1)}")

    elif 'open code' in command:
        codePath = "C:\\Users\\SUBHA\\OneDrive\\Desktop\\Visual Studio Code.lnk"
        os.startfile(codePath)

    elif 'cricket' in command:
        webbrowser.open_new_tab("cricbuzz.com")
        talk('This is live news from cricbuzz')
        time.sleep(6)

    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())

    elif 'open google' in command:
        talk("opening google")
        webbrowser.open_new_tab("https://www.google.com")
        talk("Google chrome is open now")
        time.sleep(5)

    elif 'open geeksforgeeks' in command:
        talk("opening geeks for geeks")
        webbrowser.open_new_tab("www.geeksforgeeks.com")
        talk("Opening Geeks for Geeks ")
        time.sleep(5)

    elif 'open spotify' in command:
        talk("opening spotify")
        spotify = "C:\\Users\\SUBHA\\OneDrive\\Desktop\\Spotify.lnk"
        talk("starting spotify app")
        os.startfile(spotify)

    elif 'open youtube' in command:
        talk("opening youtube")
        webbrowser.open_new_tab("https://www.youtube.com")
        talk("youtube is open now")
        time.sleep(5)

    elif 'open gmail' in command:
        talk("opening google mail")
        webbrowser.open_new_tab("gmail.com")
        talk("Google Mail open now")
        time.sleep(5)

    elif 'command prompt' in command:
        talk('Opening command prompt')
        os.system('start cmd')
        time.sleep(5)

    elif 'take photo' in command:
        talk("taking photo... give some poses")
        ec.capture(0, "camera", "img.jpg")

    elif 'shutdown' in command:
        talk("shutting down the system in 10 seconds")
        time.sleep(10)
        os.system("shutdown /s /t 5")

    elif 'sleep the system' in command:
        talk("the system is going to sleep")
        os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")

    elif 'restart the system' in command:
        talk("restarting the system in 10 seconds")
        time.sleep(10)
        os.system("shutdown /r /t 5")

    elif 'take screenshot' in command:
        scshot()

    elif 'take notes' in command:
        statement = command.replace("take notes", "")
        note(statement)

    elif 'who is' in command:
        talk("searching wikipedia ")
        command = command.replace("wikipedia", "")
        result = wikipedia.summary(command, sentences=2)
        talk("According to wikipedia")
        print(result)
        talk(result)

    elif ('search' in command) or ('define' in command) or ('what is' in command):
        talk("searching in google")
        webbrowser.open("https://www.google.com/search?q=" + command)
        time.sleep(5)

    else:
        talk('please say again.')


if __name__ == '__main__':
    wish()
    while True:
        run_fores()


