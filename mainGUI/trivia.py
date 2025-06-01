import sys

import requests
import html
import sqlite3
global correct_alpha
global options_with_bullet
import random
import speech_recognition as sr
import pyttsx3
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(ui, text):
    ui.updateGifs("speaking")
    engine.say(text)
    engine.runAndWait()


def takeAnswer(ui):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.5
        r.energy_threshold = 300
        ui.updateGifs("listening")
        ui.terminalPrint("Listening...\n")
        audio = r.listen(source)
    try:
        ui.updateGifs("loading")
        user_input = r.recognize_google(audio, language="en-in").upper()
        ui.terminalPrint(f"You said: {user_input}\n")
        return user_input
    except sr.UnknownValueError:
        ui.terminalPrint("Sorry, I couldn't understand the audio.")
        speak(ui, "Sorry, I couldn't understand the audio.")
        speak(ui, "Try again")
        return takeAnswer(ui)
    except sr.RequestError as e:
        ui.terminalPrint(f"Error making the speech recognition request: {e}")
        return None





def get_player_info(ui, cursor, conn):

    while True:
        ui.terminalPrint("Please enter your name: ")
        speak(ui, "Please enter your name: ")
        ui.current_task = "name-trivia"
        while True:
            if ui.current_task == "trivia-start":
                name = ui.text2

                if name.lower() == "admin":
                    admin_password = input("Enter admin password: ")
                    delete_leaderboard(ui, cursor, admin_password, conn)
                    break

                elif name.isalpha():
                    cursor.execute("SELECT * FROM leaderboard WHERE name=?", (name,))
                    existing_player = cursor.fetchone()

                    if existing_player:
                        ui.terminalPrint(f"Welcome back, {name.capitalize()}! Your current high score is {existing_player[2]} points.")
                        speak(ui, f"Welcome back, {name.capitalize()}! Your current high score is {existing_player[2]} points.")
                        ui.terminalPrint("\nYou have 1 attempt for each question and 2 lives per game!")
                        speak(ui, "\nYou have 1 attempt for each question and 2 lives per game!")
                        return name, existing_player[2]
                    else:
                        ui.terminalPrint(f"Welcome {name.capitalize()} to the Trivia game!\nYou have 1 attempts for each question and 2 lives per game!")
                        speak(ui, f"Welcome {name.capitalize()} to the Trivia game!\nYou have 1 attempts for each question and 2 lives per game!")
                        return name, 0



                else:
                    ui.terminalPrint("Only alphabets allowed!")

#
ADMIN_PASSWORD = "adminadmin123*"
def delete_leaderboard(ui, cursor, password, conn):
    if password == ADMIN_PASSWORD:
        confirm = input("Are you sure you want to delete all entries from the leaderboard? (Yes/No): ").lower()
        if confirm == "yes":
            cursor.execute("DELETE FROM leaderboard")
            ui.terminalPrint("All entries deleted from the leaderboard.")
            conn.commit()
            print("done")
            ui.close()
            sys.exit()
        else:
            ui.terminalPrint("Deletion canceled.")
            ui.close()
    else:
        ui.terminalPrint("Incorrect admin password. Deletion canceled.")
        ui.close()


def update_leaderboard(ui, name, score, cursor, conn):
    name2 = str(name)
    cursor.execute("SELECT * FROM leaderboard WHERE name=?", (name2,))
    existing_player = cursor.fetchone()

    if existing_player:

        cursor.execute("UPDATE leaderboard SET score=? WHERE name=?", (score, name2))
        ui.terminalPrint(f"Updated {name2.capitalize()}'s score to {score}")

    else:

        cursor.execute("INSERT INTO leaderboard (name, score) VALUES (?, ?)", (name2, score))
        ui.terminalPrint(f"Added {name2.capitalize()} to the leaderboard with a score of {score}")

    conn.commit()



def display_leaderboard(ui, cursor):
    cursor.execute("SELECT * FROM leaderboard ORDER BY score DESC")
    leaderboard = cursor.fetchall()

    if leaderboard:
        ui.terminalPrint("\nLeaderboard:")
        for rank, (player_id, name, score) in enumerate(leaderboard, start=1):
            ui.terminalPrint(f"{rank}. {name}: {score}")

    else:
        ui.terminalPrint("Leaderboard is empty.")

def get_questions(ui):


    api_url = "https://opentdb.com/api.php?amount=50&difficulty=easy&type=multiple"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        return data["results"]
    else:
        ui.terminalPrint(f"Error: {response.status_code}")
        return None

def fifty_fifty(ui, options, correct_answer):

    incorrect_options = [opt for opt in options if opt != correct_answer]
    eliminated_options = random.sample(incorrect_options, 2)
    remaining_options = [opt for opt in options if opt not in eliminated_options]
    global options_with_bullet
    options_with_bullet = {}
    for i, option in enumerate(remaining_options, start=65):
        ui.terminalPrint(f"{chr(i)}. {option}")
        key = chr(i)
        options_with_bullet[key] = option

    speak(ui, options_with_bullet)
    return correct_answer,remaining_options

def ask_the_audience(ui, options, correct_answer):
    ui.updateGifs("loading")
    ui.terminalPrint("\nGetting Audience's answers......")
    time.sleep(4)
    audience_votes = {}
    global options_with_bullet
    if random.random() < 0.75:

        correct_percentage = random.uniform(50, 70)
        audience_votes[correct_answer] = correct_percentage


        remaining_percentage = 100 - correct_percentage


        incorrect_options = [opt for opt in options if opt != correct_answer]


        for option in incorrect_options:
            option_percentage = random.uniform(0, remaining_percentage)
            audience_votes[option] = option_percentage
            remaining_percentage -= option_percentage
        audience_votes[incorrect_options[-1]] += remaining_percentage

        options_with_bullet = {}

        for i, (option, percentage) in enumerate(audience_votes.items(), start=65):
            ui.terminalPrint(f"{chr(i)}. {option} : {'■' * int(percentage)} ({percentage:.2f}%)")
            key = chr(i)
            options_with_bullet[key] = option

        speak(ui, options_with_bullet)
    else:


        for option in options:
            option_percentage = random.uniform(0, 100)
            audience_votes[option] = option_percentage


        total_percentage = sum(audience_votes.values())
        for option in options:
            audience_votes[option] = (audience_votes[option] / total_percentage) * 100

        options_with_bullet = {}

        for i, (option, percentage) in enumerate(audience_votes.items(), start=65):
            ui.terminalPrint(f"{chr(i)}. {option} : {'■' * int(percentage)} ({percentage:.2f}%)")
            key = chr(i)
            options_with_bullet[key] = option

        speak(ui, options_with_bullet)
    return correct_answer, options

def flip_the_question(ui, options, correct_answer):
    new_question = get_questions(ui)[0]
    decoded_question = html.unescape(new_question["question"])
    new_correct_answer = html.unescape(new_question["correct_answer"])

    new_incorrect_answers = [html.unescape(ans) for ans in new_question["incorrect_answers"]]
    new_options = [new_correct_answer] + new_incorrect_answers

    ui.terminalPrint(f"\nNew Question: {decoded_question}")
    speak(ui, f"New Question:{decoded_question}")

    random.shuffle(new_options)
    global options_with_bullet
    options_with_bullet = {}
    for i, option in enumerate(new_options, start=65):
        ui.terminalPrint(f"{chr(i)}. {option}")
        key = chr(i)
        options_with_bullet[key] = option

    speak(ui, options_with_bullet)
    return new_correct_answer, new_options


def ask_the_expert(ui, options, correct_answer, options_with_bullet):
    ui.updateGifs("loading")
    ui.terminalPrint("Expert is thinking.....")
    time.sleep(4)
    if random.random() < 0.8:
        correct = correct_answer
        for key, value in options_with_bullet.items():
            if value == correct:
                ui.terminalPrint(f"\nMaybe the answer is: {key}. {correct_answer}")
                speak(ui, f"Maybe the answer is: OPTION {key}. {correct_answer}")
    else:
        incorrect_options = [opt for opt in options if opt != correct_answer]
        inc_ans=random.choice(incorrect_options)
        for key, value in options_with_bullet.items():
            if value == inc_ans:
                ui.terminalPrint(f"\nMaybe the answer is: {key}. {inc_ans}")
                speak(ui, f"Maybe the answer is: OPTION {key}. {inc_ans}")
    return correct_answer, options


def main(ui):

    conn = sqlite3.connect("leaderboard.db")

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leaderboard (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            score INTEGER
        )
    ''')
    ui.terminalPrint("Welcome to Trivia!")
    speak(ui,"Welcome to Trivia!")
    player_name, player_score = get_player_info(ui, cursor, conn)
    questions = get_questions(ui)
    current_score = 0

    if not questions:
        return

    max_attempts = 1
    max_lives = 2
    available_lifelines = {'\n50-50': fifty_fifty,
                           '\nASK THE AUDIENCE': ask_the_audience,
                           '\nFLIP THE QUESTION': flip_the_question,
                           '\nASK THE EXPERT': ask_the_expert}

    for question in questions:
        decoded_question = html.unescape(question["question"])
        correct_answer = html.unescape(question["correct_answer"])
        incorrect_answers = [html.unescape(ans) for ans in question["incorrect_answers"]]
        options = [correct_answer] + incorrect_answers
        ui.terminalPrint(f"\nQuestion: {decoded_question}")
        speak(ui, f"\nQuestion: {decoded_question}")

        optionsABCD = ['A', 'B', 'C', 'D']
        optionsAB = ['A', 'B']
        random.shuffle(options)
        global options_with_bullet
        options_with_bullet = {}
        for i, option in enumerate(options, start=65):
            ui.terminalPrint(f"{chr(i)}. {option}")
            key = chr(i)
            options_with_bullet[key] = option
        speak(ui, options_with_bullet)

        attempts = 0
        while attempts < max_attempts:

            ui.terminalPrint("\nSay 'Option A/B/C/D' or 'correct full answer' or 'Exit' to quit the game\nOR\nSay 'Lifeline' to choose a lifeline!")
            user_answer = takeAnswer(ui)

            if user_answer == "EXIT":
                ui.terminalPrint(f"Game Over. Your final score: {current_score}")
                speak(ui, f"Game Over. Your final score: {current_score}")
                if current_score > player_score:
                    update_leaderboard(ui, player_name, current_score, cursor, conn)
                    display_leaderboard(ui, cursor)

                else:
                    ui.terminalPrint("No changes in leaderboard!")
                    display_leaderboard(ui, cursor)
                ui.current_task = None
                return
            elif user_answer == "LIFELINE":
                if len(available_lifelines) == 0:
                    ui.terminalPrint("No Lifelines left!")
                    speak(ui, "No Lifelines left!")
                else:
                    speak(ui, "Available Lifelines")
                    ui.terminalPrint("Available Lifelines:")
                    ui.terminalPrint(f"\n{''.join(available_lifelines.keys())}")

                    while True:
                        ui.terminalPrint("\nChoose a lifeline or say 'back' to go back: ")
                        chosen_lifeline = takeAnswer(ui)

                        if chosen_lifeline == "BACK":
                            break



                        elif "\n"+chosen_lifeline in available_lifelines:
                            if chosen_lifeline == "ASK THE EXPERT":
                                chosen_lifeline2 = "\n" + chosen_lifeline
                                correct_answer, options = available_lifelines[chosen_lifeline2](ui, options, correct_answer, options_with_bullet)
                                del available_lifelines[chosen_lifeline2]
                                break
                            else:
                                chosen_lifeline2 = "\n"+chosen_lifeline
                                correct_answer, options = available_lifelines[chosen_lifeline2](ui, options, correct_answer)
                                del available_lifelines[chosen_lifeline2]
                                break

                        elif chosen_lifeline == "50 50" or "5050" or "FIFTY FIFTY" or "FIFTY-FIFTY":
                            if "\n50-50" in available_lifelines.keys():
                                correct_answer, options = available_lifelines["\n50-50"](ui, options, correct_answer)
                                del available_lifelines["\n50-50"]
                                break
                            else:
                                ui.terminalPrint("Invalid lifeline. Please choose from the available lifelines.")
                                speak(ui, "Invalid lifeline. Please choose from the available lifelines.")


                        else:
                            ui.terminalPrint("Invalid lifeline. Please choose from the available lifelines.")
                            speak(ui, "Invalid lifeline. Please choose from the available lifelines.")


            elif user_answer.startswith("OPTION") and len(user_answer) == 8:
                global correct_alpha
                if len(options_with_bullet) == 4:

                    selected_option = user_answer[7:].strip().upper()
                    for key, value in options_with_bullet.items():
                        if value == correct_answer:

                            correct_alpha = key

                    if selected_option == correct_alpha:
                        ui.terminalPrint("Correct answer!")
                        speak(ui, "Correct answer!")
                        current_score += 1

                        break
                    elif selected_option not in optionsABCD:
                        ui.terminalPrint("Invalid answer. Please choose from the options.")
                        speak(ui, "Invalid answer. Please choose from the options.")
                    else:
                        ui.terminalPrint("Incorrect answer.")
                        speak(ui, "Incorrect answer.")
                        attempts += 1
                        ui.terminalPrint(f"You have {(max_attempts) - (attempts)} attempts left!")
                        speak(ui, f"You have {(max_attempts) - (attempts)} attempts left!")

                else:
                    selected_option = user_answer[7:].strip().upper()
                    for key, value in options_with_bullet.items():
                        if value == correct_answer:

                            correct_alpha = key

                    if selected_option == correct_alpha:
                        ui.terminalPrint("Correct answer!")
                        speak(ui, "Correct answer!")
                        current_score += 1

                        break
                    elif selected_option not in optionsAB:
                        ui.terminalPrint("Invalid answer. Please choose from the options.")
                        speak(ui, "Invalid answer. Please choose from the options.")
                    else:
                        ui.terminalPrint("Incorrect answer.")
                        speak(ui, "Incorrect answer.")
                        attempts += 1
                        ui.terminalPrint(f"You have {(max_attempts) - (attempts)} attempts left!")
                        speak(ui, f"You have {(max_attempts) - (attempts)} attempts left!")

            elif user_answer.lower() in [option.lower() for option in options]:
                if user_answer.lower() == correct_answer.lower():
                    ui.terminalPrint("Correct answer!")
                    speak(ui, "Correct answer!")
                    current_score += 1

                    break
                else:
                    ui.terminalPrint("Incorrect answer.")
                    speak(ui, "Incorrect answer.")
                    attempts += 1
            else:
                ui.terminalPrint("Invalid answer. Please choose from the options.")
                speak(ui, "Invalid answer. Please choose from the options.")

        if attempts == max_attempts:
            ui.terminalPrint(f"\nThe correct answer is: {correct_answer}")
            speak(ui, f"The correct answer is: {correct_answer}")
            max_lives -= 1
            ui.terminalPrint(f"\nYou have {max_lives} lives left for this trivia!")


            if max_lives == 0:
                break
    ui.terminalPrint(f"Game Over. Your final score: {current_score}")
    speak(ui, f"Game Over. Your final score: {current_score}")
    if current_score > player_score:
        update_leaderboard(ui, player_name, current_score, cursor, conn)
        display_leaderboard(ui, cursor)
    else:
        ui.terminalPrint("No changes in leaderboard!")
        display_leaderboard(ui, cursor)
    ui.current_task = None
    return
