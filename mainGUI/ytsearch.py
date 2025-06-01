import webbrowser


import pyttsx3
replace_words = ["youtube", "search" ,"Search", " on ", "YouTube", " in " , "google" , "Google" , "browser" , "play" , "spotify" , "Spotify" , " for ", "gary" , "Gary", "Garry", "garry"]



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(updategif, text):
    updategif("speaking")
    engine.say(text)
    engine.runAndWait()

def perform_youtube_search(command, terminalPrint, updategif):
    for i in replace_words:
        command = command.replace(i, "")
    updategif("loading")
    web = f"https://www.youtube.com/results?search_query={command}"
    terminalPrint(f"Searching YouTube for: {command}")
    speak(updategif, f"Searching YouTube for: {command}")
    webbrowser.open(web)

