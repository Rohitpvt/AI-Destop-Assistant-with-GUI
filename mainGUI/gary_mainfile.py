from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5. QtCore import QThread
from PyQt5.QtCore import QTimer, QTime
from garyMainGUI import Ui_MainGui
from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import pyautogui
from AppOpener import *
from bard_AI import bardai
from game2 import play_game
from googlesearch import perform_google_search
from imagineDONE import *
from remember import *
from spotifysearch import search_on_spotify
from talk_with_assistant import get_response
from ytsearch import perform_youtube_search
from trivia import *
from RPS import mainRPS
from Choose_one import *
from gemini_image import *
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    ui.updateGifs("speaking")
    engine.say(text)
    engine.runAndWait()


def greetme(ui):

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        ui.terminalPrint("Good Morning!")
        speak("Good Morning!")
    elif hour >= 12 and hour < 17:
        ui.terminalPrint("Good Afternoon!")
        speak("Good Afternoon!")
    else:
        ui.terminalPrint("Good Evening!")
        speak("Good Evening!")

def screenshot():
    ui.updateGifs("speaking")
    pyautogui.hotkey('win', 'prtscr')
    ui.terminalPrint("Screenshot taken!")
    speak("Screenshot taken!")
class garyMain(QThread):
    def __init__(self):
        self.greeted = False
        super(garyMain, self).__init__()




    def run(self):

        while True:

            self.takeCommand()
            self.otherreq()








    def sleepgary(self):
        ui.terminalPrint("I am going to Sleep Mode. Say 'Wake Up Gary' to wake me up.")
        speak("I am going to Sleep Mode. Say 'Wake Up Gary' to wake me up.")
        ui.updateGifs("sleeping")
        while True:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.pause_threshold = 0.5
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)

            try:

                command = r.recognize_google(audio, language="en-in").lower()

                if "wake up" in command:

                    ui.terminalPrint("I am ready!")
                    speak("I am ready!")
                    self.takeCommand()
                    break
                else:
                    continue
            except Exception:
                pass




    def takeCommand(self):

        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            r.pause_threshold = 0.7
            r.energy_threshold = 300
            if not self.greeted:
                greetme(ui)
                self.greeted = True
            ui.terminalPrint("How can I help you?")
            speak("How can I help you?")
            ui.updateGifs("listening")
            ui.terminalPrint("Listening...")
            audio = r.listen(source)

        try:
            ui.updateGifs("loading")
            command = r.recognize_google(audio, language="en-in").lower()
            ui.terminalPrint(f"You said: {command}")


            if "image" in command and ("search" in command or "recognition" in command or "recogniser" in command or "analyser" in command or "analyzer" in command or "recognizer" in command):
                geminiimg(ui.terminalPrint, ui.updateGifs)


            elif "open" in command:
                app_name_start = command.find("open") + len("open")
                if app_name_start != -1:
                    app_name = command[app_name_start:].strip()
                    app_list = give_appnames(upper=False)

                    if app_name.lower() in app_list:
                        open(app_name, match_closest=True)
                        speak(f"Opening {app_name}!")
                    else:
                        ui.terminalPrint(f"{app_name.capitalize()} is not available on this system!")
                        speak(f"{app_name} is not available on this system!")





            elif "imagine" in command or "generate" and "image" in command:
                #imagine(ui.terminalPrint, command)

                imagine(ui.terminalPrint, command, ui.model_in, ui.updateGifs, "prodia")


            elif "garry" in command or "gary" in command or "tell me" in command:
                bardai(ui.terminalPrint, command, ui.updateGifs)

            elif "search" in command and "google" in command:
                perform_google_search(command, ui.terminalPrint, ui.updateGifs)


            elif "ss" in command or "screenshot" in command:
                screenshot()


            elif "search" in command and "youtube" in command:
                perform_youtube_search(command, ui.terminalPrint, ui.updateGifs)




            elif "play" in command and "game" in command:

                speak("Choose from the options below!")
                ui.terminalPrint("\nEnter '1' for 'Stone, Paper, Scissors'\nEnter '2' for 'Choose one Option Game'\nEnter '3' for 'Choose your own adventure'\nEnter '4' for 'Trivia'\nEnter '5' to go back\n")
                ui.terminalPrint("\nChoose the option: ")
                ui.model_in("game-option")





            elif "play" in command or "play" and "spotify" in command or "search" and "spotify" in command:
                search_on_spotify(command, ui.terminalPrint, ui.updateGifs)
                ui.terminalPrint("While you enjoy your music,")
                speak("While you enjoy your music,")
                self.sleepgary()


            elif "erase everything from your memory" in command or "forget everything" in command or "erase everything" in command or "delete everything" in command or "delete everything from remember" in command or "erase the remember list" in command or "remove everything from remember list" in command or "remove everything from your memory" in command:
                erase(ui.terminalPrint, ui.updateGifs)

            elif "what do you remember" in command or "what things do you remember" in command or "todo list" in command or "to do list" in command or "remember list" in command:
                list_memory(ui.terminalPrint, ui.updateGifs)

            elif "remember" in command:
                remember(command, ui.terminalPrint, ui.updateGifs)

            elif "sleep" in command:
                self.sleepgary()

            elif "bye" in command or "goodbye" in command or "go offline" in command or "quit" in command or "exit" in command:
                ui.terminalPrint("Bye. Have a great day.")
                speak("Bye. Have a great day.")
                ui.close()
                sys.exit()

            else:
                get_response(command, ui.updateGifs, ui.terminalPrint)
                self.takeCommand()


        except sr.UnknownValueError:
            ui.terminalPrint("Sorry, I couldn't understand your audio.")
            speak("Sorry, I couldn't understand your audio.")
            speak("Say it again")
            self.takeCommand()
        except sr.RequestError as e:
            ui.terminalPrint(f"Speech recognition request failed: {e}")
        except Exception as e:
            ui.terminalPrint(f"An error occurred: {e}")


    def otherreq(self):

        r1 = sr.Recognizer()

        with sr.Microphone() as source:
            r1.adjust_for_ambient_noise(source)
            r1.pause_threshold = 0.5
            r1.energy_threshold = 300
            ui.terminalPrint("\nDo you have any other request? (Yes/No)")
            speak("Do you have any other request?")
            ui.terminalPrint("\nListening...")
            ui.updateGifs("listening")
            audio = r1.listen(source)


        try:
            ui.updateGifs("loading")
            req = r1.recognize_sphinx(audio).lower()

            if req == "yes":

                ui.terminalPrint(f"You said: {req}")
                self.takeCommand()

            elif req == "no":
                ui.terminalPrint(f"You said: {req}")
                ui.terminalPrint("\nGoodbye! Will see you later. ")
                speak("Goodbye! Will see you later. ")

                ui.close()
                sys.exit()

            else:
                self.otherreq()
        except sr.UnknownValueError:
            ui.terminalPrint("Sorry, I couldn't understand your audio.")
            speak("Sorry, I couldn't understand your audio.")
            speak("Say it again")
            self.takeCommand()
        except sr.RequestError as e:
            ui.terminalPrint(f"Speech recognition request failed: {e}")
        except Exception as e:
            ui.terminalPrint(f"An error occurred: {e}")






















########################################################################

startExecution = garyMain()
class guiOfGary(QWidget):
    def __init__(self):
        self.current_task = None
        self.text2 = None
        super(guiOfGary, self).__init__()

        self.garyUI = Ui_MainGui()
        self.garyUI.setupUi(self)
        self.runAllMovies()
        self.setupTime()
        self.garyUI.enter.clicked.connect(self.on_enter_clicked)

    def setupTime(self):

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)


        font = QFont('DS-Digital', 50)
        font.setBold(True)
        self.garyUI.Time.setFont(font)
        self.garyUI.Time.setStyleSheet("color: white; background-color: transparent;")

    def updateTime(self):

        current_time = QTime.currentTime()


        time_str = current_time.toString("hh:mm")


        self.garyUI.Time.setPlainText(time_str)



    def runAllMovies(self):
        self.garyUI.astrogif = QtGui.QMovie("C:\\Users\\ASUS\\OneDrive - Vivekananda Institute of Professional Studies\\PROJECTS\\Python\\Gary 2.0 + UI\\GUI resc\\astro mov.gif")
        self.garyUI.astro.setMovie(self.garyUI.astrogif)
        self.garyUI.astrogif.start()

        self.garyUI.rocketgif = QtGui.QMovie("C:\\Users\\ASUS\\OneDrive - Vivekananda Institute of Professional Studies\\PROJECTS\\Python\\Gary 2.0 + UI\\GUI resc\\rocket up down.gif")
        self.garyUI.rocket.setMovie(self.garyUI.rocketgif)
        self.garyUI.rocketgif.start()

        self.garyUI.listeninggif = QtGui.QMovie("C:\\Users\\ASUS\\OneDrive - Vivekananda Institute of Professional Studies\\PROJECTS\\Python\\Gary 2.0 + UI\\GUI resc\\Listening AI.gif")
        self.garyUI.listening.setMovie(self.garyUI.listeninggif)
        self.garyUI.listeninggif.start()

        self.garyUI.loadinggif = QtGui.QMovie("C:\\Users\\ASUS\\OneDrive - Vivekananda Institute of Professional Studies\\PROJECTS\\Python\\Gary 2.0 + UI\\GUI resc\\Loading.gif")
        self.garyUI.loading.setMovie(self.garyUI.loadinggif)
        self.garyUI.loadinggif.start()

        self.garyUI.speakinggif = QtGui.QMovie("C:\\Users\\ASUS\\OneDrive - Vivekananda Institute of Professional Studies\\PROJECTS\\Python\\Gary 2.0 + UI\\GUI resc\\AI Speaking.gif")
        self.garyUI.speaking.setMovie(self.garyUI.speakinggif)
        self.garyUI.speakinggif.start()

        self.garyUI.sleepinggif = QtGui.QMovie("C:\\Users\\ASUS\\OneDrive - Vivekananda Institute of Professional Studies\\PROJECTS\\Python\\Gary 2.0 + UI\\GUI resc\\Sleeping.gif")
        self.garyUI.sleeping.setMovie(self.garyUI.sleepinggif)
        self.garyUI.sleepinggif.start()

        startExecution.start()


    def updateGifs(self, state):

        if state == "listening":
            self.garyUI.listening.raise_()
            self.garyUI.loading.hide()
            self.garyUI.speaking.hide()
            self.garyUI.sleeping.hide()
            self.garyUI.listening.show()

        elif state == "speaking":
            self.garyUI.speaking.raise_()
            self.garyUI.loading.hide()
            self.garyUI.listening.hide()
            self.garyUI.sleeping.hide()
            self.garyUI.speaking.show()

        elif state == "loading":
            self.garyUI.loading.raise_()
            self.garyUI.listening.hide()
            self.garyUI.speaking.hide()
            self.garyUI.sleeping.hide()
            self.garyUI.loading.show()

        elif state == "sleeping":

            self.garyUI.sleeping.raise_()
            self.garyUI.Time.raise_()
            self.garyUI.loading.hide()
            self.garyUI.speaking.hide()
            self.garyUI.listening.hide()
            self.garyUI.sleeping.show()
            self.garyUI.Time.show()
            self.garyUI.Title.raise_()

        else:
            pass



    def terminalPrint(self, text):
        self.garyUI.output.appendPlainText(text)

    def onTextChanged(self):
        self.text2 = self.garyUI.input.toPlainText()


    def model_in(self, current_task):

        if current_task == "prodia":
            self.current_task = current_task + "-model"



            ui.terminalPrint("Enter Model Name from above list: ")

            while self.current_task == "prodia-model" or self.current_task == "prodia-generate":
                continue


        elif current_task == "game-option":
            self.current_task = "game-input"
            ui.terminalPrint("Enter the option from above: ")


            while self.current_task is not None:
                continue


    def on_enter_clicked(self):
        if self.current_task == "prodia-model":
            models_list = {'Default': 'v1-5-pruned-emaonly.safetensors [d7049739]',
                           'Anime': 'EimisAnimeDiffusion_V1.ckpt [4f828a15]',
                           'Animated': 'revAnimated_v122.safetensors [3f4fefd9]',
                           'Cartoon': 'toonyou_beta6.safetensors [980f6b15]',
                           'Cyberpunk': 'shoninsBeautiful_v10.safetensors [25d8c546]',
                           'Photography': 'ICantBelieveItsNotPhotography_seco.safetensors [4e7a3dfd]',
                           'Logo': 'dreamshaper_8.safetensors [9d40847d]',
                           'Realistic': 'absolutereality_v181.safetensors [3d9d4d2b]',
                           "Nature": 'epicrealism_naturalSinRC1VAE.safetensors [90a4c676]',
                           'Anything': 'anythingV5_PrtRE.safetensors [893e49b9]'}

            self.text2 = self.garyUI.input.toPlainText().title()
            self.garyUI.input.clear()
            self.current_task = "prodia-generate"

            if self.text2 in models_list.keys():
                generate(ui, self.text2)

            else:
                ui.terminalPrint("You have chosen the incorrect Model! Try again from start!")
                self.current_task = None


        elif self.current_task == "game-input":
            self.text2 = self.garyUI.input.toPlainText()
            self.garyUI.input.clear()
            if self.text2.isdigit():
                self.text2 = int(self.text2)
                if self.text2 == 1:
                    self.current_task = "game-start"
                    thread = threading.Thread(target=mainRPS, args=(ui,))
                    thread.start()
                elif self.text2 == 2:
                    self.current_task = "game-start"
                    thread = threading.Thread(target=chooseoneMAIN, args=(ui,))
                    thread.start()
                elif self.text2 == 3:
                    self.current_task = "game-start"
                    thread = threading.Thread(target=play_game, args=(ui,))
                    thread.start()
                elif self.text2 == 4:
                    self.current_task = "game-start"
                    thread = threading.Thread(target=main, args=(ui,))
                    thread.start()
                elif self.text2 == 5:
                    self.current_task = None
                else:
                    ui.terminalPrint("Choose the correct option from the game menu!")
                    speak("Choose the correct option from the game menu!")
                    ui.terminalPrint("Please enter again from above menu: ")

        elif self.current_task == "name-adv":
            self.text2 = self.garyUI.input.toPlainText()
            self.garyUI.input.clear()
            self.current_task = "adv-start"







        elif self.current_task == "name-trivia":
            self.text2 = self.garyUI.input.toPlainText()
            self.garyUI.input.clear()
            if self.text2.isalpha():
                ui.terminalPrint("")
                self.current_task = "trivia-start"
            else:

                ui.terminalPrint("Enter letters only!")




        elif self.current_task == "adv-time":
            self.text2 = self.garyUI.input.toPlainText()
            self.garyUI.input.clear()

            self.current_task = "time-input"

        elif self.current_task == "name-riddle":
            self.text2 = self.garyUI.input.toPlainText()
            self.garyUI.input.clear()

            self.current_task = "name-riddle-input"



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(r'C:\Users\ASUS\OneDrive - Vivekananda Institute of Professional Studies\PROJECTS\Python\Gary 2.0 + UI\GUI resc\gary final icon.ico'))
    ui = guiOfGary()
    ui.show()

    sys.exit(app.exec_())
