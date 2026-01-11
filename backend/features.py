import os
import re
from colorama import Cursor
from playsound import playsound
import eel
import pywhatkit as kit
import sqlite3
import webbrowser

from backend.config import Assistant_name
from backend.speak import speak


con=sqlite3.connect("python.db")
cursor=con.cursor()

#playingassistantsound

def playassi():
    music_dir="C:\\Users\\hp\\OneDrive\\Desktop\\Project python\\frontend\\resources\\start_sound.mp3" 
    playsound(music_dir)
    
@eel.expose
def micsound():
    music_dir="C:\\Users\\hp\\OneDrive\\Desktop\\Project python\\frontend\\resources\\mixkit-select-click-1109 (1).mp3"
    playsound(music_dir)
    
    
def opencommand(query):
    query=query.replace(Assistant_name,"")   
    query=query.replace("hello","") 
    query=query.replace("open","")
    query.lower()
    
    app_name=query.strip()
    if app_name != "":

        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")

        
        
def playyoutube(query):
    search_term=extract_term(query) 
    speak("playing"+search_term+"on youtube")  
    kit.playonyt(search_term)     
    
    
    
def extract_term(command):
        #define regularexpressionpattern to capturethe song name
        pattern=r'play\s+(.*?)\s+on\s+youtube'
        #use re.research to find the match in the command
        match=re.search(pattern,command,re.IGNORECASE)
        #if a match is found,return the extracted song name;otherwise return none
        return match.group(1) if match else None
        
        