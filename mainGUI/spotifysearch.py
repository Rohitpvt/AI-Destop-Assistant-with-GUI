
import pyttsx3
import pyautogui
import time
from AppOpener import *
import webbrowser

replace_words = ["youtube", "search" ,"Search", " on ", "YouTube", " in " , "google" , "Google" , "browser" , "play" , "spotify" , "Spotify" , " for ", "gary" , "Gary", "Garry", "garry"]
app_list=give_appnames(upper=False)







engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(updategif, text):
    updategif("speaking")
    engine.say(text)
    engine.runAndWait()

def search_on_spotify(command, terminalPrint, updategif):
    for i in replace_words:
        command = command.replace(i, "")
    command1=command.strip()

    if "spotify" in app_list:
        updategif("loading")

        speak(updategif, f"Searching {command} on Spotify App!")
        updategif("loading")
        open('spotify', match_closest=True)

        time.sleep(5)

        pyautogui.hotkey('ctrl', 'l')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)

        pyautogui.write(str(command1))

        for key in ['enter', 'tab', 'enter', 'enter']:
            time.sleep(2)
            pyautogui.press(key)

        terminalPrint(f"\nSearching Spotify for: {command1}")
        time.sleep(5)
    else:
        terminalPrint("You dont have spotify installed on this device!\nSwitching to Spotify Web Player")
        speak(updategif, "You dont have spotify installed on this device!. Switching to Spotify Web Player")
        updategif("loading")
        web = f"https://open.spotify.com/search/{command1}"
        terminalPrint(f"Searching {command1} on Spotify Web Player!")
        speak(updategif, f"Searching {command} on Spotify Web Player!")
        webbrowser.open(web)



