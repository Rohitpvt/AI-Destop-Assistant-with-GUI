import random
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(updategif, text):
    updategif("speaking")
    engine.say(text)
    engine.runAndWait()


def take_answer(terminalPrint, updategif):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.5
        r.energy_threshold = 300
        updategif("listening")
        terminalPrint("Listening...\n")
        audio = r.listen(source)
    try:
        updategif("loading")
        user_input = r.recognize_google(audio, language="en-in").lower()
        return user_input
    except sr.UnknownValueError:
        terminalPrint("Sorry, I couldn't understand the audio.")
        speak(updategif, "Sorry, I couldn't understand the audio.")
        return take_answer(terminalPrint, updategif)
    except sr.RequestError as e:
        terminalPrint(updategif, f"Error making the speech recognition request: {e}")
        return None


def get_user_choice(terminalPrint, updategif):

    while True:
        try:
            terminalPrint("Say 'Stone/Paper/Scissors' or 'Exit' to quit:")
            user_choice = take_answer(terminalPrint, updategif)
            if user_choice.lower() in ['stone', 'paper', 'scissors', 'exit']:
                return user_choice.lower()
            else:
                terminalPrint("Invalid choice. Please choose stone, paper, or scissors (say 'exit' to end).")
                speak(updategif, "Invalid choice")
        except Exception:
            terminalPrint("Some error Occurred! Try Again!")
            speak(updategif, "Please try again.")


def get_computer_choice(user_choice, terminalPrint, updategif):
    choices = ['stone', 'paper', 'scissors']
    try:
        if user_choice.lower() == 'stone':

            if random.random() < 0.7:
                return random.choice(['stone', 'paper'])
            else:
                return random.choice(choices)

        elif user_choice.lower() == 'paper':
            if random.random() < 0.7:
                return random.choice(['paper', 'scissors'])
            else:
                return random.choice(choices)

        elif user_choice.lower() == 'scissors':
            if random.random() < 0.7:
                return random.choice(['scissors', 'stone'])
            else:
                return random.choice(choices)
    except Exception:
        terminalPrint("Some error Occurred! Try Again!")
        speak(updategif, "Please try again.")


def determine_winner(user_choice, computer_choice, terminalPrint, updategif):
    try:
        if user_choice == computer_choice:
            speak(updategif, "It's a tie!")
            return 'It\'s a tie!'
        elif (user_choice == 'stone' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'stone') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            speak(updategif, "You win!")
            return 'You win!'
        else:
            speak(updategif, "You lose!")
            return 'You lose!'
    except Exception:
        terminalPrint("Some error Occurred! Try Again!")
        speak(updategif, "Please try again.")

def mainRPS(ui):

    user_wins = 0
    ui.terminalPrint("Welcome to Stone, Paper, Scissors!\n")
    speak(ui.updateGifs, "Welcome to Stone, Paper, Scissors!\n")
    while True:

        try:

            user_choice = get_user_choice(ui.terminalPrint, ui.updateGifs)

            if user_choice == 'exit':
                ui.terminalPrint("Quitting the game!")
                speak(ui.updateGifs, "Quitting the game!")
                ui.current_task = None
                break

            computer_choice = get_computer_choice(user_choice, ui.terminalPrint, ui.updateGifs)

            ui.terminalPrint(f"You chose {user_choice.capitalize()}.")
            speak(ui.updateGifs, f"You chose {user_choice}.")
            ui.terminalPrint(f"\nThe computer chose {computer_choice.capitalize()}.")
            speak(ui.updateGifs, f"The computer chose {computer_choice}.")

            result = determine_winner(user_choice, computer_choice, ui.terminalPrint, ui.updateGifs)
            ui.terminalPrint(result)

            if result == 'You win!':
                user_wins += 1

            ui.terminalPrint(f"User wins: {user_wins} rounds")
        except Exception:
            ui.terminalPrint("Some error Occurred! Try Again!")
            speak(ui.updateGifs, "Please try again.")

