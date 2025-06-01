
global final_answer
import pyttsx3

import google.generativeai as genai
#from TM import terminalPrint







replace_words = ['hey garry', 'garry', 'gary', 'tell me','gehri','gaary']

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



def speak(updategif, text):
    updategif("speaking")
    engine.say(text)
    engine.runAndWait()


def bardai(terminalPrint, command, updategif):



    for i in replace_words:
        command = command.replace(i, "")
    updategif("loading")
    terminalPrint("\nPlease wait, I'm Thinking..")
    speak(updategif, "Please wait, I am Thinking")

    try:
        updategif("loading")
        genai.configure(api_key='AIzaSyAbxN27L7V1D9qHkQFVQ350zsHoRcb5mKk')


        model = genai.GenerativeModel('gemini-pro')

        answer = model.generate_content(command)


        if "Gemini" and "Google" in answer.text.strip():
            #print("1")
            final_answer = answer.text.strip().replace("Gemini", "Gary")
            final_answer2 = final_answer.replace("Google", "Aman, Rohit and Gurjyot")
        elif "Gemini" in answer.text.strip():
            #print("2")
            final_answer2 = answer.text.strip().replace("Gemini", "Gary")
        elif "Google" in answer.text.strip():
            #print("3")
            final_answer2 = answer.text.strip().replace("Google", "Aman, Rohit and Gurjyot")
        elif "Google" and "I do not have a name." in answer.text.strip() or "Google" and "I do not have a name," in answer.text.strip():
            #print("4")
            final_answer = answer.text.strip().replace("Google", "Aman, Rohit and Gurjyot")
            final_answer2 = final_answer.replace("I do not have a name", "My name is Gary")
        elif "I do not have a name." in answer.text.strip() or "I do not have a name," in answer.text.strip():
            #print("5")
            final_answer2 = answer.text.strip().replace("I do not have a name", "My name is Gary")
        else:
            final_answer2 = answer.text.strip()
        words = final_answer2.split()
        full_stop_count = 0
        spoken_words = []
        for word in words:
            spoken_words.append(word)
            if word.endswith('.'):
                full_stop_count += 1


                if full_stop_count == 4:
                    break

        terminalPrint("\nResult:\n")
        finalans3 = ' '.join(spoken_words)
        terminalPrint(finalans3.strip())
        speak(updategif, finalans3)

    except Exception as e:
        terminalPrint(f"\nAn error occurred: {e}")
        speak(updategif, "An error occurred")
