import pyttsx3
import speech_recognition as sr
import eel
import time




def speak(text):
  engine = pyttsx3.init('sapi5')
  voices = engine.getProperty('voices')
  engine.setProperty('voice', voices[0].id)
  engine.setProperty('rate', 153) 
  eel.Displaymessage(text)
  engine.say(text)
  engine.runAndWait()
   
def takecommand():  
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        eel.Displaymessage("Listening...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        
        audio=r.listen(source,10,6)
        
    try:
        print("Recognizing")
        eel.Displaymessage("Recognizing")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}")
        eel.Displaymessage(query)
        
        
        
    except Exception as e:
        return ""    
    
    return query.lower() 

@eel.expose
def allCommands():
    query=takecommand()
    print(query)
    
    if "open " in query:
        from backend.features import opencommand
        opencommand(query)
        
    elif "on youtube":
        from backend.features import playyoutube
        playyoutube(query)
        
    else:
        print("nrunning")    

    
    eel.showcontainer() 
# text=takecommand()
# speak(text)