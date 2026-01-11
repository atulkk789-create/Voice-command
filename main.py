import os
import eel
from backend.features import*
from backend.speak import*
eel.init("frontend")
playassi()
os.system('start msedge.exe --app="http://localhost:8000/index.html"')
eel.start('index.html',mode=None,host='localhost',block=True)