import psutil
import random
import pywhatkit
import os
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)   #it helps us print number of voices present
'''
print("Choice gender of your assistant")
print("1)Male\n2)Female")
gender=input("Enter your choice:\n")
if gender=='1':
    engine.setProperty('voice',voices[0].id)
elif gender=='2':
    engine.setProperty('voice',voices[1].id)
else:
    print("Wrong input")
'''
engine.setProperty('voice',voices[1].id)
def speak(audio):   #this is our speak funtion which we use to for our AI to speak
    engine.say(audio)
    engine.runAndWait()
def greetings():
    #this function will greet us according to time
    hour = int(datetime.datetime.now().hour)
    # we get hours according to 24hours clock
    if hour >= 0 and hour < 12:
        speak("Good Morning! hope you have a nice day")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon! hope you had a nice start of the day")
    else:
        speak("Good evening!")
    speak("Hello boss I'am assistant how my I help you?")
def takeCommand():
    #It takes microphone input from the user and returns string output
    '''
        We take input from user usingspeechRecognition and we have given it a shortform sr
        This input is taken using microphone
        After taking input it returns us string output
        :return:
        '''
    r = sr.Recognizer()
    with sr.Microphone() as source:#aking input of voice by microphone
        speak("Listening command...")
        print("Listening Command...")
        # we change our pause_threshold that is our non-speaking audio
        # before phrase is considered as complete
        # we can take a gap of 1sec in between so it is required
        r.pause_threshold = 1
        audio = r.listen(source)
    # using try and exception because we should know where we have issues/error
    try:
        speak("Recognizing Your Voice...")
        print("Recognizing Your Voice...")
        #query is our command which we give to assistant
        command = r.recognize_google(audio, language='en-in')
        print(f"boss said: {command}\n")
        speak(f"boss said: {command}\n")
    except Exception as e:
        # print(e)
        #we don't want to print our error so print(e) is commented
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return command

def battery():
    usage = str(psutil.cpu_percent())
    battery = psutil.sensors_battery()
    print(f"CPU : {usage}\n Battery : {battery}")
    speak(f"CPU : {usage}\n Battery : {battery}")

if __name__ == '__main__':
    greetings()
    while True:
        #this will help to run the loop again and again
        command = takeCommand().lower()

        if 'wikipedia' in command:
            speak('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'play' in command:
            song = command.replace('play', '')
            speak(f"playing {song}")
            pywhatkit.playonyt(song)


        elif 'sleep' in command or 'exit' in command:
            speak("Sleeping.....")
            quit()

        elif 'open google' in command or 'google' in command:
            speak("opening google.com")
            webbrowser.open("google.com")

        elif 'github' in command:
            speak("opening github.com")
            webbrowser.open_new_tab("github.com")

        elif 'time' in command:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"Current time is {current_time}")
            print(f"Current time is {current_time}")

        elif 'generate password' in command:
            speak("Generating")
            lower = "abcdefghijklmnopqrstuvwxyz"
            upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            numbers = "0123456789"
            characters = "+/&*%$#@!"
            length = 10
            all = f"{upper}+{characters}+{lower}+{numbers}"
            password = "".join(random.sample(all, length))
            speak(password)
            print(password)


        elif 'suggest games' in command or 'games' in command:
            speak("Some of the popular mobile games you may find on playstore are")
            list4 = ['Call of Duty mobile', 'Candy Crush', 'Subway Surfers', 'Temple Run', 'Boom beach',
                     'Clash Of Clans', 'Mini Militia', 'Ludo King', 'Among Us', 'Hill Climb Racing', '8 ball pool']
            speak(list4)

        elif 'breakfast' in command:

            speak("Vegitarian breakfast")
            list2 = ['Methi Paratha', 'Vegetable Pancake', 'Aloo paratha', 'Carrot Halwa',
                     'Misal Pav', 'Dosa', 'Idli Sambar', 'Pasta', 'Maggie', 'Noodles', 'Upma',
                     'Bread Butter', 'Bread Jam', 'Sandwhich', 'Toast', 'Peanut Butter and Bread',
                     'Bread Pakoda', 'Sago(saaboodaana)', 'saaboodaana vada', 'saabu kichdi', 'khawa poli',
                     'poran poli']
            speak(random.choice(list2))

        elif 'dinner' in command or 'lunch' in command:
            speak("Vegitarian dinner")
            list1 = ['panner tikka masala', 'aloo paratha', 'bhendi', 'kofta', 'dal rice', 'kaju masala', 'veg maratha',
                     'veg handi', 'kaju curry', 'veg mix', 'palak paneer', 'shev bhaji', 'paneer burji',
                     'baingan masal',
                     'shenga bhaji', 'aloo fry', 'methi aloo', 'aloo palak', 'bhindi masala', 'veg kholapuri',
                     'mushroom masala', 'navaratna kurma', 'veg keema (soyabean)', 'veg mix', 'nargisi kofta',
                     'veg bhuna',
                     'veg hyderabadi',
                     'veg diwani handi', ]
            speak(random.choice(list1))

        elif 'snacks' in command or 'starters' in command:
            speak("Vegitarian starters or snacks")
            list3 = ['veg manchurian', 'haara baara kebab', 'haaka noodles', 'schezwan noodles', 'panner tikka',
                     'panner phadi kebab', 'panner chilli', 'burger', 'pizza', 'french fries', 'hot dog', 'platters',
                     'panner shengai', 'pav bhaji', 'tomato soup', 'manchow soup', 'panner fingers',
                     'cheese pakoda', 'onine pakoda', 'aloo pakoda', 'samosa', 'vada pav', 'shev puri',
                     'pani puri', 'chutney puri', 'dhai puri', 'spring rolls', 'wraps']
            speak(random.choice(list3))

        elif 'do you love me' in command:
            speak("Yes I love you as a your my boss")

        elif 'do you have a boyfriend' in command:
            speak("No but I'm in love with internet")

        elif 'what is your name' in command:
            speak("You can call me assistant")

        elif 'when is your birthday' in command:
            speak("I was created on 1st May 2021")

        elif 'battery' in command or 'cpu' in command:
            battery()

        elif 'codeblocks' in command or 'code blocks' in command:
            speak("Opening codeblocks")
            path="C:\Program Files (x86)\CodeBlocks\codeblocks.exe"
            os.startfile(path)

        elif 'pycharm' in command or 'py charm' in command:
            speak("Opening Pycharm")
            path1="C:\Program Files\JetBrains\PyCharm Community Edition 2020.2.3\bin\pycharm64.exe"
            os.startfile(path1)



        else:
            speak("Sorry boss I'm yet not functioned for this program")
            print("Sorry boss I'm yet not functioned for this program")