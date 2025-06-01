import os
import random
import speech_recognition as sr1
import pyttsx3
recognizer = sr1.Recognizer()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',value=200)

def speak(updategif, text):
    updategif("speaking")
    engine.say(text)
    engine.runAndWait()

def read_question_sets(file_name):
    question_sets = []
    with open(file_name, 'r') as file:
        question_set = []
        for line in file:
            line = line.strip()
            if line:
                question_set.append(line)
            else:
                if question_set:
                    question_sets.append(question_set)
                    question_set = []
        if question_set:  
            question_sets.append(question_set)
    return question_sets

def display_question_set(question_set, terminalPrint, updategif):
    for line in question_set:
        terminalPrint("")
        terminalPrint(line)


def generate_random_percentages():
    option1_percentage = random.randint(20, 80)
    option2_percentage = 100 - option1_percentage
    return option1_percentage, option2_percentage

def get_user_choice(pass_count, terminalPrint, updategif):
    while True:
        with sr1.Microphone() as source:
            updategif("listening")
            terminalPrint("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            recognizer.pause_threshold = 0.7
            recognizer.energy_threshold = 300
            audio = recognizer.listen(source)

        try:
            updategif("loading")
            choice = recognizer.recognize_google(audio, language="en-in").lower()
            if choice in ['option a','option b','next','exit']:
                if pass_count == 4 and choice == 'next':
                    terminalPrint("You used all your Passes. Please choose option A, B, or 'exit'.")
                    speak(updategif,"You used all your Passes. Please choose option A, B, or 'exit'.")
                else:
                    terminalPrint(f"You choose: {choice.capitalize()}")
                    speak(updategif, f"You choose: {choice}")
                    return choice
            else:
                terminalPrint("Say 'OPTION A','OPTION B' OR 'NEXT' to skip the question, 'EXIT' to exit.")
                speak(updategif, "Say 'OPTION A','OPTION B' OR 'NEXT' to skip the question, 'EXIT' to exit.")
        except sr1.UnknownValueError:
            terminalPrint("Sorry, I didn't catch that. Please try again.")
            speak(updategif, "Sorry, I didn't catch that. Please try again.")
        except sr1.RequestError:
            terminalPrint("There was an error with the speech recognition service.")



def chooseoneMAIN(ui):
   
    current_directory = os.path.dirname(os.path.abspath(__file__))
    

    file_name = os.path.join(current_directory, 'question_sets.txt')

   
    question_sets = read_question_sets(file_name)

    
    random.shuffle(question_sets)

    
    pass_count = 0

    ui.terminalPrint("Welcome to Choose One Option Game!")
    speak(ui.updateGifs, "Welcome to Choose One Option Game!")

   
    while question_sets:
       
        question_set = question_sets.pop(0)

       
        display_question_set(question_set, ui.terminalPrint, ui.updateGifs)
        speak(ui.updateGifs, question_set)
        ui.terminalPrint("Say 'OPTION A','OPTION B' OR 'NEXT' to skip the question, 'EXIT' to exit.")

       
        user_choice = get_user_choice(pass_count, ui.terminalPrint, ui.updateGifs)

       
        if user_choice.lower() == 'exit':
            ui.terminalPrint("Game ended.")
            speak(ui.updateGifs, "Game ended.")
            ui.current_task = None
            break

       
        elif user_choice.lower() == 'next':
            if pass_count < 4:
                pass_count += 1
                if pass_count <= 2:
                    ui.terminalPrint(f"You have {4 - pass_count} Passes left.")
                    ui.terminalPrint("")
                elif pass_count == 3:
                    ui.terminalPrint(f"You have {4 - pass_count} Pass left.")
                    ui.terminalPrint("")
                elif pass_count == 4:
                    ui.terminalPrint("You used all your Passes, Now you have to make a Choice")

                    ui.terminalPrint("")
                continue
            else:
                ui.terminalPrint("You've used all your Passes. Please make a choice.")
                speak(ui.updateGifs, "You've used all your Passes. Please make a choice.")
                ui.terminalPrint("")
                continue

        
        elif user_choice.lower() in ['option a', 'option b']:

            option1_percentage, option2_percentage = generate_random_percentages()
            ui.terminalPrint(f"{option1_percentage:.2f}% People chosen Option A")
            ui.terminalPrint(f"{option2_percentage:.2f}% People chosen Option B")
            ui.terminalPrint("")
            speak(ui.updateGifs, f"{option1_percentage:.2f}% People chosen Option A")
            speak(ui.updateGifs, f"{option2_percentage:.2f}% People chosen Option B")
            
          
        else:
            ui.terminalPrint("Unexpected error occurred. Please try again.")
            speak(ui.updateGifs, "Unexpected error occurred. Please try again.")
