import webbrowser

import pyttsx3



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(updategif, text):
    updategif("speaking")
    engine.say(text)
    engine.runAndWait()

replace_words = ["youtube", "search" ,"Search", " on ", "YouTube", " in " , "google" , "Google" , "browser" , "play" , "spotify" , "Spotify" , " for ", "gary" , "Gary", "Garry", "garry"]
def perform_google_search(command, terminalPrint, updategif):
    for i in replace_words:
        command = command.replace(i,"")

    search_url = f"https://www.google.com/search?q={command}"
    terminalPrint(f"Searching Google for: {command}")
    speak(updategif, f"Searching Google for: {command}")
    webbrowser.open(search_url)


