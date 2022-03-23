import pyttsx3
import datetime 
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
import cv2
import pyglet

engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("Hello this is travis")
speak("Good Morning")

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("The Current time is")
    speak(Time)


def date():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    date=datetime.datetime.now().date
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome ")
    speak("How can I help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.energy_threshold=4000
        r.pause_threshold=1
        audio=r.listen(source)
        
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again Please")
        speak("How can i help you")
        return "None"
    return query


def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('jp9978552@gmail.com','Elon@123')
    server.sendmail('jp9978552@gmail.com',to,content)
    server.close()

def screenshot():
    img =pyautogui.screenshot()
    img.save('D:/Projects/Assistant/screenshots/screenshotsnew.png')

def cpu():
    usage=str(psutil.cpu_percent())
    speak('CPU is at'+usage)
    battery=psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)

def img(): 
  ag_file = "sirilike.gif"
  animation = pyglet.resource.animation(ag_file)
  sprite = pyglet.sprite.Sprite(animation)

# create a window and set it to the image size
  win = pyglet.window.Window(width=sprite.width, height=sprite.height)

# set window background color = r, g, b, alpha
# each value goes from 0.0 to 1.0
  green = 0, 1, 0, 1
  pyglet.gl.glClearColor(*green)

  @win.event
  def on_draw():
     win.clear()
     sprite.draw()

  pyglet.app.run()


def takepics():
  # define a video capture object
   vid = cv2.VideoCapture(0)
  
   while(True):  
    # Capture the video frame
    # by frame
        ret, frame = vid.read()
  
    # Display the resulting frame
        # cv2.imshow('frame', frame)
      
        cv2.imwrite("piccs/User" + ".jpg",frame)
        if cv2.waitKey(100) & 0xff:
           break
  
# After the loop release the cap object
        vid.release()
# Destroy all the windows
        cv2.destroyAllWindows()


def joke():
    speak(pyjokes.get_joke())

def wish():
    speak('Hello There')


def how():
    speak('I am Fine Thanks For Asking')
    speak('Its really good to hear from you')
    speak("I hope you and your loved ones are safe and healthy")

def pwd():
    speak("Please say me name of Directory")

def mkdr():
    os.mkdir(nm)
    speak("Drictory Created Successfully")

def pic():
    speak("Get Ready")
    speak("Capturing Picture")

def showpic():
    speak("Here is your Captured picture")
    img=cv2.imread('picss/User.jpg')

    cv2.imshow('User',img)

    cv2.waitKey(2000) & 0xff
    cv2.destroyAllWindows()

def youtube():
    firfx='C:/Program Files/BraveSoftware/Brave-Browser/Application/brave %s'
    wb.get(firfx).open_new('youtube.com')

def google():
    firfx='C:/Program Files/BraveSoftware/Brave-Browser/Application/brave %s'
    wb.get(firfx).open_new('google.com')





if __name__=="__main__":
    wishme()
    while True:
        query=takeCommand().lower()

        if 'what is time now' in query:
            time()
        elif 'Todays date' in query:
            date()
        elif 'what is'in query:
            speak("Searching...")
            query=query.replace("what is","")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)

        elif 'who is'in query:
            speak("Searching...")
            query=query.replace("who is","")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)


        elif 'send email' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="atual.om@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Unable to send the Email")

        elif 'search in browser' in query:
            speak("What should i search ?")
            chromepath = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave %s'
            search =takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
       
    

        elif 'play songs' in query:
            songs_dir='C:/Users/jp997/Music'
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,'Stay.mp3'))

        elif 'remember one thing' in query:
            speak("What should I remember?")
            data =takeCommand()
            speak("you said me to remember that"+data)
            remember=open('data.txt','w')
            remember.write(data)
            remember.close()
        
        elif 'do you know anything' in query:
            remember=open('data.txt','r')
            speak("You said me to remember that" +remember.read())

        elif 'take screenshot' in query:
            screenshot()
            speak("Done")

        elif 'cpu status' in query:
            cpu()

        elif 'tell me joke' in query:
            joke()

        elif 'directory' in query:
             pwd()
             nm=takeCommand()
             mkdr()
            
        elif 'open youtube' in query:
            youtube()

        elif 'open google' in query:
            google()
            
        elif 'hello' in query:
            wish()

        elif 'how are you' in query:
            how()
            speak('How can i help you')

        elif 'take a pic' in query:
            pic()
            takepics()
        
        elif 'show me pic' in query:
            showpic()

        elif 'where are we' in query:
            speak("Now we are in vivekananda global university jaipur rajasthan")
            
        elif 'wish me' in query:
            speak("Happy Engineers day")

        elif 'do you love me' in query:
            speak("Of Course You are one of a kind")
            speak("you are the fantastic person i have ever met")

        elif 'thank you' in query:
            speak("You are welcome")
            speak("Have a nice day ")
            quit()

        elif 'who are you' in query:
            speak("i am travis")
            speak("Thanks for asking")
            speak("How can i help you")

        elif 'thanks' in query:
            speak("You are welcome")
            speak("How can i help you")

        elif 'who made you' in query:
            speak('proudly saying Atul made me in his lab')
      

        elif 'bye' in query:
            speak('ok bye ')
            speak('Have a nice day')
            quit()
       
            


takeCommand()














