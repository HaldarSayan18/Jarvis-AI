import pyttsx3
import datetime
import os
import smtplib
#import wikipedia
import webbrowser
import speech_recognition as spR
EmailDict = {
    "Sayan"         : "sayanhaldar@gmai.com",
    "Sayan_cemk"    : "it2004@cemk.ac.in",
    "Subhasish"     : "it2014@cemk.ac.in",
    "Hrick"         : "it2022@cemk.ac.in"
}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

#int name = 0;
def speak(aud):
    engine.say(aud)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour >= 0 and hour < 12):
        speak("Good Morning!!")
    elif(hour == 12):
        speak("Good Noon!!")
    elif(hour >= 12 and hour < 18):
        speak("Good Afternoon!!")
    else:
        speak("Good Evening!!")
    speak("Hi! I am JarvisAI. Tell me how can I help you")

def takeCmd():      #takes microphone input from user and returns string as output
    r = spR.Recognizer()
    with spR.Microphone() as Source:
        print('JarvisAI is listening..')
        r.pause_threshold = 1
        aud = r.listen(Source)
    try:
        print("wait!! AI is recognizing...")
        query = r.recognize_google(aud, language="en-US")
        print("My command: "+query)
    except Exception as E:
        print(E)
        print("Sorry!! can't recognize...\n Please say that again")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()           #used to initiate the SMTP connection and greet the server
    server.starttls()       #is used to enable encryption for the SMTP connection
    server.login('youracc@gmail.com', 'your-passwd')
    server.sendmail('sayanhaldar05@gmail.com', to, content)
    server.close()

if(__name__ == "__main__"):
    #speak("Sayan Haldar is a python programmer.")
    wishMe()
    while True:
        query = takeCmd().lower()       #converting in lowercase to match the query
        #logic for executing tasks bssed on query
        if 'the time' in query:
            starTime = datetime.datetime.now().strftime("%H:%M:S")
            speak("Current time is: "+starTime)
            print(starTime)
        
        #elif("wikipedia" in query):
        #    speak("searching wikipedia...")
        #    query.replace("wikipedia", " ")
        #    results = wikipedia.summary(query, sentences = 3)
        #    speak("According to wikipedia")
        #    print(results)
        #    speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'play movie' in query:
            movie_dir = "E:\\extras (movie)"
            #double backslash is used to escape the character
            movies = os.listdir(movie_dir)
            print(movies)
            #for i in range(len(movies)):
            #    os.startfile(os.path.join(movie_dir, movies[i]))
        
        elif 'open VS code' in query:
            VSpath = "C:\\Users\\intel\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(VSpath)
        
        elif 'send email' in query:
            email_dir = dict(EmailDict)
            print(email_dir)
            try:
                speak("What I have to say ?")
                content = takeCmd()
                to = "sayanhaldar05@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as E:
                print(E)
                speak("Sorry! I am unable to send the email.")