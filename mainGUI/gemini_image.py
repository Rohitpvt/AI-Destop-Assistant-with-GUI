import tkinter as tk
from tkinter import filedialog
import speech_recognition as sr
import pyttsx3
import time
from PIL import Image
import google.generativeai as genai
recognizer = sr.Recognizer()



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(updategif, text):
    updategif("speaking")
    engine.say(text)
    engine.runAndWait()

def askprompt(terminalPrint, updategif):
    while True:
        with sr.Microphone() as source:
            terminalPrint("What do you want to ask related to this Image?")
            speak(updategif, "What do you want to ask related to this Image?")
            recognizer.pause_threshold = 0.7
            recognizer.energy_threshold = 300
            recognizer.adjust_for_ambient_noise(source)
            updategif("listening")
            terminalPrint("\nListening...")
            audio = recognizer.listen(source)
        try:
            updategif("loading")
            prompt = recognizer.recognize_google(audio, language="en-in").lower()
            terminalPrint(f"You said: {prompt}")
            speak(updategif, f"You said: {prompt}")
            terminalPrint("Analysing Image..")
            speak(updategif,"Analysing Image.." )
            return prompt
        except sr.UnknownValueError:
            terminalPrint("Sorry, I couldn't understand your audio.")
            speak(updategif, "Sorry, I couldn't understand your audio.")
            speak(updategif, "Say it again")
            askprompt(terminalPrint, updategif)
        except sr.RequestError as e:
            terminalPrint(f"Speech recognition request failed: {e}")
            speak(updategif, "An error occurred:")
        except Exception as e:
            terminalPrint(f"An error occurred: {e}")
            speak(updategif, "An error occurred:")


def geminiimg(terminalPrint, updategif):

    root = tk.Tk()
    root.withdraw()

    terminalPrint("Please Choose the Image ('.jpg','.png','.jpeg')")
    speak(updategif, "Please choose the image")



    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

    if file_path:
        genai.configure(api_key='AIzaSyAbxN27L7V1D9qHkQFVQ350zsHoRcb5mKk')

        model = genai.GenerativeModel('gemini-pro-vision')
        img = Image.open(file_path)
        user_prompt = askprompt(terminalPrint, updategif)

        updategif("loading")
        response = model.generate_content([user_prompt, img])
        response.resolve()
        terminalPrint(f"\n{response.text.strip()}")
        speak(updategif, response.text.strip())
    else:
        terminalPrint("No file selected")
        speak(updategif,"No file selected")

