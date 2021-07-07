#       ------------------------------------------------- PYTHON VOICE ASSISTANT PROJECT -----------------------------------------------------


import pyttsx3                        # this module is used FOR SPEAK A ASSISTANT 
import speech_recognition as sr       # this module is used FOR LISTENING a User Voice and return a string of voice
import wolframalpha                   # It is used to compute expert-level answers using Wolfram’s algorithms, knowledgebase and AI technology.
import wikipedia                      # Search wikipedia infomation
import webbrowser                     # these module used for a open a webbrowser tab        
import datetime                       # show datetime 
import requests                       # Requests is used for making GET and POST requests.                                            # choose a randomly number we can also implement more tasks
import os                             # The OS module in Python provides functions for interacting with the operating system
import pyjokes                        # One line jokes for programmers
import smtplib                        # The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP                         # This module provides various time-related functions. For related functionality, see also the datetime and calendar modules.
import pywhatkit as kit
import psutil                         # psutil is a cross-platform library for retrieving information on running processes and system utilization(CPU, memory, disks, networks, sensors) in Python

from ecapture import ecapture as ec   # To capture images from your Camera.

# CREATE A LOGIC OF SPEACK MODULE --pyttsx3

engine=pyttsx3.init('sapi5')  # sapi5 is API PROVIDE BY MICROSOFT
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0])


# CREATE A SPEAK FUNCTION TO SPEAK OVER ASSISTANT...
def speak(audio):
    
    """
    [speak function take one argument and returns it]

    Args:
    audio (STRING): [speak function take audio in STRING we can pass in arguments and returns as a in voice ]
    
    """
    engine.say(audio)
    engine.runAndWait()


# CREATE A WISH FUNCTION FOR AI WISH FOR YOU Ex. GOOD MORING like AS per TIME ....
def wishMe():
    
    """
    [ wishme function work as a wish like GOOD MORNING,etc like ]
    
    [ useing datetime to get a hours of present day ]
    
    """
    dt=datetime.datetime.now().hour
    
    if (dt>6 and dt<=12):
        speak(" GOOD MORNING DHRUV! ")
        
    elif (dt>12 and dt<=18):
        speak(" GOOD AFTERNOON DHRUV! ") 
    
    else:
        speak(" GOOD EVENING DHRUV! ")
    
    speak(" How may i help you Dhruv! ")

# CREATE A TAKECOMMAND FUNCTION TO RECOGNIZE OVER USER INPUT VOICE 
def takecommand():
    
    """
    [takecommand function take a user input Voice and return to Strings]
    
    User Voice recognition and then listening to it.
    
    """
    
    s=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        
        s.pause_threshold=0.5     # seconds of non-speaking audio before a phrase is considered complete
        audio = s.listen(source,phrase_time_limit=10,timeout=10)

    
    try:
        print("Recognizing...")
        s.energy_threshold = 5000
        s.dynamic_energy_threshold = True
        au=s.recognize_google(audio,language='en-in')
        print(f" User Said {au}\n ")
    
    except Exception as e:
        print(e)
        print("Say That Again...")
        
        return "None"
    
    return au

# CREATE sendEmail function to send a mail through SMTP server
def sendEmail(to,content):
    
    """
    [summary: sendEmail THROUGH A SMTP SERVER using Google Mail API]

    Args:
        to ([String]): [Content E-mail address To send through another people ]
        content ([String]): [content requried Message and Body ]
    """
    try:
        server=smtplib.SMTP("smtp.gmail.com",587) # Ports 465 and 587 are intended for email client to email server communication - sending out email using SMTP protocol
        server.ehlo()
        server.starttls()
    
        # USING A APP PASWORD PROVIDED BY G-MAIL 
        from_Email="YOUR E-MAIL"
        server.login("YOUR EMAIL",'YOUR Google APP PASSWORD')
        server.sendmail(from_Email,to,content)
    except Exception as e:
        print(e)
        speak("something problem in Function Fix it.")

# Create a function to show a bettry percentage
def getBattery(seconds):
    """
    [get current battery percentage and conver into HH:MM:SS]

    Args:
        seconds ([Battery_call_function]): [battery function call to get battery in HH:MM:SS]

    Returns:
        [STRING]: [Battery percentage in (HH:MM:SS) ]
    """
    # python script showing battery details
  
    # function returning time in hh:mm:ss
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    
    return "%d:%02d:%02d" % (hours, minutes, seconds)
  
    
#    -----------------------------------------------------------  LOGIC  PART  --------------------------------------------------

if __name__ == "__main__":
    clean=lambda:os.system('cls')
    
    # This Function will clean any
    # command before execution of this python file
    clean()
    wishMe()
    
    edith=True
    while edith:
        
        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
        
        query=takecommand().lower()
        
                                    # WIKIPEDIA SEARCHING for User        
        if 'wikipedia' in query:
            speak("Searching Wikipedia....")
            q=query.replace('wikipedia','')
            result=wikipedia.summary(q,sentences=4)
            speak("According to Wikipedia")
            speak(result)
            
                                    # OPENING YOUTUBE FOR USER
        elif 'open youtube' in query:
            speak("ok. i will opening youtube for you")
            webbrowser.open('www.youtube.com')
            
                                    # OPENING GOOGLE FOR USER
        elif 'open google' in query:
            speak("ok. i will opening google for you")
            webbrowser.open("www.google.com")
            
                                    # OPENING STACKOVERFLOW FOR USER
        elif 'open stack overflow' in query:
            speak("ok. i will opening stackoverflow for you")
            webbrowser.open("www.stackoverflow.")

                                    # AI Speak a News Headline 
        elif 'news' in query:
            nw='https://timesofindia.indiatimes.com/home/headlines'
            speak("Today latest news is: ")
            speak(nw)
        
                                    # Opening VLC
        elif 'vlc' in query:
            speak("opening vlc")
            os.system('start VLC')
            
                                   # Opening Gmail for User
        elif 'open gmail' in query:
            speak("opening gmail for you")
            webbrowser.open('www.gmail.com')
            
                                    # OPENING AMAZON FOR USER
        elif 'open amazon' in query or 'purchase' in query:
            speak("ok. i will open amazon for you.")
            speak("Enjoy your shopping Sir")
            webbrowser.open("www.amazon.com")

                                    # PLAYING MUSIC FOR USER
        elif 'play song' in query:
            speak('Here you go with music')
            
            # music dir path
            musicdir='F:\SONGS'          # SET YOUR OWN PATH DIR
            songs=os.listdir(musicdir)
            os.startfile(os.path.join(musicdir,songs[0]))
        
                                    # QUIT EDIT FOR USER 
        elif 'quit' in query or 'quite' in query:
            speak('Have a nice day dhurv')
            speak('Thank you for giving time dhruv. I am enjoying with you')
            edith=False

                                    # SHOW A PRESENT TIME FOR USER
        elif 'time' in query:
            dt=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, Time is {dt}")

                                    # SEND EMAIL TO PARTICULAR PERSON
        elif 'send mail to dc' in query:
            
            try:
                speak("What should i say")
                content=takecommand()        # take a message content what should be send through takecommand
                to='EMAIL'  
                sendEmail(to,content)
                speak("Email has been sent successfully")
    
            except Exception as e:
                print(e)
                print("Sorry Dhruv i am not able to send email")
        
                                    # SEND E-MAIL ANY OF THIS PEOPLE 
        elif 'send mail' in query:
            
            try:
                speak("what should i say")
                content=takecommand()
                to=input("To Email: ")  # i will take input function to send Email TO another person. You can take also a takecommand to get E-MAIL address
                sendEmail(to,content)
                speak('Email has been sent !')
                
            except  Exception as e:
                print(e)
                print("Sorry Dhruv i am not able to send email")
                
                                    # 
        elif 'how are you' in query:
            speak('i am fine, Thank you!')
            speak('How are you! Sir')
        
                                    #
        elif 'good' in query or "fine" in query:
            speak("It's good to know that your fine")

                                    #
        elif "what's your name" in query or "what is your name" in query:
            speak('My name is Edith')
            speak("i am your AI ASSISTANT") 
        
                                    #
        elif 'who made you' in query or "who created you" in query:
            speak('i have been created by Dhruv')
        
                                    # JOKES FOR YOU
        elif "joke" in query:
            speak(pyjokes.get_joke())
            
                                    #
        elif "calculate" in query:
            
            question=takecommand()
            app_id="YOUR APP ID" 
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak("The answer is " + answer)
        
                                    #
        elif "search" in query or "play" in query:
            query=query.replace('search','') 
            query=query.replace('play','')
            webbrowser.open_new_tab(query)
        
                                    #
        elif "who i am" in query:
            speak("if you talk then definately you are human") 
            
                                    # OPENING POWEPOINT FOR USER
        elif "powerpoint" in query:
            speak("openigning power point presentation")
            os.system('start POWERPNT')
        
                                    # OPENING WORD FOR USER
        elif "word" in query:
            speak("opening microsoft word presentation")
            os.system('start WINWORD')

                                    # OPENING CMD FOR USER
        elif "cmd" in query:    
            speak("opening command line")
            os.system("start cmd")
            
                                    # OPENIGN LOCATION FOR USER
        elif "where is" in query:
            query=query.replace('where is','')
            location=query
            speak("here is your location is")
            speak(location)
            webbrowser.open('https://www.google.co.in/maps/place/'+location+'')
        
                                    # take a photo 
        elif "take photo" in query:
            ec.capture(0,'edith camera','img.jpg')
        
                                    # Writing Note For user
        elif "write a note" in query:
            speak("What should i write Sir!")
            note=takecommand()
            file=open('edith.txt','a')
            speak("Sir, should i include date and time")
            usdt=takecommand()
            if 'yes' in usdt or 'sure' in usdt:
                dt=datetime.datetime.now().strftime("%H:%M:%S")
                file.write(dt)
                file.write(" :-- ") 
                file.write("\n")
                file.write(note)
            else:
                file.write(note)
        
                                # Showing notes for user
        elif "show note" in query:
            speak("Showing notes")
            file=open('edith.txt','r')
            rd=file.readlines()
            print(rd)
            speak(rd)

                                # showing Weather
        elif "show weather" in query or "today weather" in query:
            
            api_key='YOUR  API KEY'          
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takecommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature in kelvin unit is " +
                        str(current_temperature) +
                        "\n humidity in percentage is " +
                        str(current_humidiy) +
                        "\n description  " +
                        str(weather_description))
                speak(" Temperature in kelvin unit is " +
                        str(current_temperature) +
                        "\n humidity in percentage is " +
                        str(current_humidiy) +
                        "\n description  " +
                        str(weather_description))
            else:
                speak(" City Not Found ")
        
                                #
        elif "will you be my gf" in query or "will you be my bf" in query:  
            speak("I'm not sure about, may be you should give me some time")
 
                                #
        elif "how are you" in query:
            speak("I'm fine, glad you me that")
 
                                #
        elif "i love you" in query:
            speak("It's hard to understand")
 
                                #
        elif "what is" in query or "who is" in query:
            
            # Use the same API key
            # that we have generated earlier
            client = wolframalpha.Client("API-KEY")
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")

                                # Opening Gallery for user
        elif "gallery" in  query:
            
            gallery_path='‪YOUR GALLERY PATH'
            lis_gallery=os.listdir(gallery_path)
            os.startfile(os.path.join(gallery_path,lis_gallery[0]))
            
                                # Opening Paint for user
        elif 'paint' in query:
                                
            speak("opening paint")
            os.system('start mspaint')

                                # Show Current Battery percentage AND ALSO PLUGGED IN OR NOT
        elif "battery" in query:
                                
            # returns a tuple
            battery = psutil.sensors_battery()
  
            print("Battery percentage : ", battery.percent)
            print("Power plugged in : ", battery.power_plugged)
  
            # converting seconds to hh:mm:ss
            print("Battery left : ", getBattery(battery.secsleft))
            
            speak(f"Battery percentage str{battery.percent}")
            speak(f"Power plugged in {battery.power_plugged}")
            speak(f"Battery left  {getBattery(battery.secsleft)}")

                                #
        elif 'play video' in query:
            
            speak("which song would you like to play")
            tk=takecommand()
            #tkd=tk.replace('play','')
            kit.playonyt(tk)

                                #
        elif 'search' in query:
            
            speak("what we do search")
            s=takecommand()
            sk=s.replace('search','')
            kit.search(sk)

    
    # YOU CAN ALSO ADD MORE CONDITIONS AND FUNCTION TO MAKE MORE ENHANCED VOICE ASSISTANT
    
    # I ALSO TRY TO ADD MORE CONDITIONS AND FUNCTION TO MAKE PROJECT MORE DEEPER 
    

# ---------------------------------------------------------------- END OF PROJECT ----------------------------------------------------------------
        
            
        
        
               
            
        
        
    
    
 




