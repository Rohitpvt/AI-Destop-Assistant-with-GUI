import json
import random
import re
import pyttsx3
from bard_AI import bardai
import time


def load_json(file):
    with open(file) as bot_responses:

        return json.load(bot_responses)



response_data = load_json("C:/Users/ASUS/OneDrive - Vivekananda Institute of Professional Studies/PROJECTS/Python/Gary 2.0 + UI/mainGUI/responses.json")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(updategif, text):
    updategif("speaking")
    engine.say(text)
    engine.runAndWait()


def get_response(input_string, updategif, terminalPrint):

    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []


    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]


        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1


        if 2 <= required_score <= 3:

            for word in split_message:

                if word in response["user_input"]:
                    response_score += 1

        elif required_score == len(required_words):
            for word in split_message:

                if word in response["user_input"]:
                    response_score += 1


        score_list.append(response_score)

    best_response = max(score_list)
    response_index = score_list.index(best_response)


    if best_response != 0:
        bot_responses = response_data[response_index]["bot_response"]
        selected_response = random.choice(bot_responses)
        if selected_response.startswith("\nReady"):
            terminalPrint(selected_response)
            speak(updategif,"here is the list of functions i can perform")
            time.sleep(10)
        else:
            terminalPrint(selected_response)
            speak(updategif, selected_response)
        return selected_response

    else:
        bardai(terminalPrint, input_string, updategif)
