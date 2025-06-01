import pyttsx3





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(updategif, text):
    updategif("speaking")
    engine.say(text)
    engine.runAndWait()



replace_words=['garry','gary','remember that','remember']

remember_list = "remember.txt"
def erase(terminalPrint, updategif):
    with open(remember_list, "w+"):
        pass
    terminalPrint("I have erased everything from my memory!")
    speak(updategif, "I have erased everything from my memory!")


def get_next_serial_number():
    try:
        with open(remember_list, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        with open(remember_list, "w") as file:
            lines = []

    return len(lines) + 1



def remember(command, terminalPrint, updategif):
    next_serial_number = get_next_serial_number()
    for i in replace_words:
        command = command.replace(i,"")
    if len(command) == 0:
        terminalPrint("Please Specify that what should I remember")
        speak(updategif, "Please Specify that what should I remember")
    else:
        item_with_serial = f"{next_serial_number}. {command}\n"
        with open(remember_list, "a") as file:
            file.write(item_with_serial)

        terminalPrint(f"I will remember that you said:{command}")
        speak(updategif, f"I will remember that you said:{command}")


def list_memory(terminalPrint, updategif):
    try:
        with open(remember_list, "r") as file:
            lines = file.readlines()
            if lines:
                terminalPrint("Here are the things I remember:")
                speak(updategif, "Here are the things I remember:")
                for line in lines:
                    line = line.strip()
                    terminalPrint(line)
                    speak(updategif, line)
            else:
                terminalPrint("I don't remember anything.")
                speak(updategif, "I don't remember anything.")
    except FileNotFoundError:
        terminalPrint("I don't remember anything.")
        speak(updategif, "I don't remember anything.")