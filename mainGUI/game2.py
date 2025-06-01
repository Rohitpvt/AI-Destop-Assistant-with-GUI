import speech_recognition as sr1
from choose_ur_own_adv_jarvis import *
import datetime
global answer_name





recognizer = sr1.Recognizer()


def get_user_choice(prompt, valid_choices, ui, first_time=False):
    if first_time:
        speak(ui,f'''Hi!{answer_name} \n>>You have to make some correct decisions and find the TREASURE CHEST in order to win the game! Say 'Exit' at anytime to quit the game! Now move ahead and choose your own adventure!''')

        ui.terminalPrint("")
        ui.terminalPrint("You are in a jungle, and there are 2 ways, either you can go left or you can explore other side of the jungle!")
        speak(ui, "You are in a jungle, and there are 2 ways, either you can go left or you can explore other side of the jungle!")
        ui.terminalPrint("")

    while True:
        ui.terminalPrint(prompt)
        speak(ui, prompt)
        with sr1.Microphone() as source:
            recognizer.energy_threshold = 400
            recognizer.pause_threshold = 0.5
            ui.updateGifs("listening")
            ui.terminalPrint("Listening...")
            audio = recognizer.listen(source)
        try:
            ui.updateGifs("loading")
            choice = recognizer.recognize_google(audio, language="en-in").lower()
            if choice in valid_choices:
                ui.terminalPrint(f"\nYou choose: {choice.capitalize()}")
                speak(ui, f"You choose: {choice}")
                return choice
            else:
                ui.terminalPrint("Sorry, I didn't understand your choice. Please try again.")
                speak(ui, "Sorry, I didn't understand your choice. Please try again.")
        except sr1.UnknownValueError:
            ui.terminalPrint("Sorry, I didn't catch that. Please try again.")
            speak(ui, "Sorry, I didn't catch that. Please try again.")
        except sr1.RequestError:
            ui.terminalPrint(ui.updateGifs, "There was an error with the speech recognition service.")


def passw():
    current_time = datetime.datetime.now(datetime.timezone.utc)
    ist = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    current_time_ist = current_time.astimezone(ist)
    current_time_str = current_time_ist.strftime("%H%M")

    answer = str(current_time_str)
    return answer



def chest(ui, lives=3):
    global password
    # lives = 3
    if lives > 0:
        ui.terminalPrint(f"You have {str(lives)} lives remaining!")
        speak(ui, "Enter the correct 4 digit code")
        ui.current_task = "adv-time"
        ui.terminalPrint("Enter the correct 4 digit code: ")
        while True:
            if ui.current_task == "time-input":

                ans = ui.text2
                if ans.isnumeric():
                    if len(ans) == 4:
                        password = passw()
                        if ans == password:
                            ui.terminalPrint("You have successfully unlocked the treasure chest and found the treasure! YOU HAVE WON")
                            speak(ui, "You have successfully unlocked the treasure chest and found the treasure! YOU HAVE WON")
                            ui.current_task = None
                            break
                        elif ans != password:
                            lives -= 1
                            ui.terminalPrint(f"Incorrect Guess! You have {str(lives)} lives remaining!")
                            speak(ui, f"Incorrect Guess! You have {str(lives)} lives remaining!")
                            if lives == 0:
                                ui.terminalPrint("You were unable to guess the code and the traps got activated!")
                                speak(ui, "You were unable to guess the code and the traps got activated!")
                                gameover(ui)
                                break
                            else:
                                ui.terminalPrint("Enter the correct 4 digit code: ")
                                chest(ui,lives)
                                break
                    else:
                        ui.terminalPrint("The secret code is of 4 digit!")
                        speak(ui, "The secret code is of 4 digit!")
                        ui.terminalPrint("Enter the correct 4 digit code: ")
                        chest(ui, lives)
                        break
                else:
                    ui.terminalPrint("Enter Numbers Only!")
                    speak(ui, "Enter Numbers Only!")
                    ui.terminalPrint("Enter the correct 4 digit code: ")
                    chest(ui, lives)
                    break





def play_explore(ui):
    valid_choices11 = ['tunnel', 'river','exit']
    choice11 = get_user_choice("Now, you have two options:\n1) Follow the map's direction to a maze-like network of tunnels.\n2) Choose the path indicated by the map that leads to an underground river.\nSay 'Spikes' or 'Crack'.",valid_choices11, ui)
    if choice11 == 'tunnel':
        tunnel(ui)
        gameover(ui)
    elif choice11 == 'river':
        river(ui)
        gameover(ui)
    elif choice11 == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint('invalid')



def play_spikes(ui):
    valid_choices12 = ['note','exit']
    choice12=get_user_choice(" Just say 'NOTE' to listen to it.", valid_choices12, ui)
    if choice12 == 'note':
        note(ui)
        chest(ui)
    elif choice12 == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint('invalid!')






def play_bridge2(ui):
    valid_choices10 = ['spikes', 'crack', 'exit']
    choice10 = get_user_choice("So now you have 2 options:\n1) Proceed down the corridor with the uncertain spikes on the floor.\n2) Take the path with the cracked roof and floor.\nSay 'Spikes' or 'Crack'.",valid_choices10, ui)
    if choice10 == 'spikes':
        spikes(ui)
        play_spikes(ui)
    elif choice10 == 'crack':
        crack(ui)
        gameover(ui)
    elif choice10 == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint('invalid')



def play_sound(ui):
    valid_choices9 = ['bridge', 'explore','exit']
    choice9 = get_user_choice("So now you have 2 options:\n1) You can cross the bridge.\n2) Explore rest of the cavern.\nSay 'Bridge' or 'Explore'.",valid_choices9, ui)
    if choice9 == 'bridge':
        bridge2(ui)
        play_bridge2(ui)
    elif choice9 == 'explore':
        explore(ui)
        play_explore(ui)
    elif choice9 == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint('invalid')



def play_boat(ui):
    valid_choices8 = ['note','exit']
    choice8 = get_user_choice("Say 'NOTE' to listen it.", valid_choices8, ui)
    if choice8 == "note":
        note(ui)
        chest(ui)
    elif choice8 == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint('invalid')

def play_throwstone(ui):
    valid_choices7 = ['bridge', 'boat','exit']
    choice7 = get_user_choice("Now you have 2 options:\n1) You can use the Bridge\n2) You can use the boat. Say 'Bridge' or 'Boat'.",valid_choices7, ui)

    if choice7 == 'bridge':
        bridge(ui)
        gameover(ui)
    elif choice7 == 'boat':
        boat(ui)
        play_boat(ui)
    elif choice7 == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint("invalid")





def play_goclose(ui):
    valid_choices5 = ['throw stone', 'sneak' , 'exit']
    choice5=get_user_choice("So now you have two options:\n1) You can distract the deadly creature by throwing a stone in the lake in front of the the creature.\n2) You can try to silently sneak from the side of the creature without being noticed.\nSay 'Throw Stone' or 'Sneak.'",valid_choices5, ui)

    if choice5 == 'throw stone':
        throwstone(ui)
        play_throwstone(ui)
    elif choice5 == 'sneak':
        sneak(ui)
        gameover(ui)
    elif choice5 == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint("invalid")






def play_deadbody(ui):
    valid_choices4 = ['make sound', 'go close','exit']
    choice4 = get_user_choice("So now you have two options: \n 1) You can make a sound so that, that unknown creature moves and you can identify it. \n 2) Go close to the shadow and identify the unknown creature. \n Say 'Make sound' or 'Go close'.",valid_choices4, ui)
    if choice4 == 'make sound':
        makesound(ui)
        gameover(ui)
    elif choice4 == 'go close':
        goclose(ui)
        play_goclose(ui)
    elif choice4 == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint("invalid")




def play_cave(ui):
    valid_choices3 = ['dead body', 'sound','exit']
    choice3 = get_user_choice("Which way will you choose? Say 'Dead Body' or 'Sound'.", valid_choices3, ui)

    if choice3 == 'dead body':
        deadbody(ui)
        play_deadbody(ui)
    elif choice3 == 'sound':
        sound(ui)
        play_sound(ui)
    elif choice3 == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint("invalid!")



def play_path(ui):
    valid_choices=['note','exit']
    choice=get_user_choice("Say 'Note' to listen it.",valid_choices, ui)
    if choice == 'note':
        note2(ui)
        chest2(ui)
    elif choice == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint('invalid')


def play_step(ui):
    valid_choices = ['corridor','room','exit']
    choice=get_user_choice("So now you have 2 options:\n1) You can go to the well-lit corridor!\n2) You can go to the well-lit room with chests. Say 'Corridor' or 'Room'.",valid_choices, ui)
    if choice == 'corridor':
        path(ui)
        play_path(ui)
    elif choice == 'room':
        room(ui)
        gameover(ui)
    elif choice == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint("invalid")


def chest2(ui, lives=3):
    global answer_name

    if lives > 0:
        ui.terminalPrint(f"You have {str(lives)} lives remaining!")
        speak(ui, "Enter the correct answer")
        ui.current_task = "name-riddle"
        ui.terminalPrint("Enter the correct answer: ")

        while True:

            if ui.current_task == "name-riddle-input":


                enter_answer = ui.text2
                if enter_answer.isalpha():
                    if enter_answer.lower() == answer_name.lower():
                        ui.terminalPrint("You have successfully unlocked the treasure chest and found the treasure! YOU HAVE WON")
                        speak(ui, "You have successfully unlocked the treasure chest and found the treasure! YOU HAVE WON")
                        ui.current_task = None
                        break
                    elif enter_answer.lower() != answer_name.lower():
                        lives -= 1
                        ui.terminalPrint(f"Incorrect Guess! You have {str(lives)} lives remaining!")
                        speak(ui, f"Incorrect Guess! You have {str(lives)} lives remaining!")
                        if lives == 0:
                            ui.terminalPrint("You were unable to guess the correct answer and the traps got activated!")
                            speak(ui, "You were unable to guess the correct answer and the traps got activated!")
                            gameover(ui)
                            break
                        else:
                            ui.terminalPrint("Enter the correct answer: ")
                            chest2(ui, lives)
                            break
                else:
                    ui.terminalPrint("Enter Alphabets only!")
                    speak(ui, "Enter Alphabets only!")
                    ui.terminalPrint("Enter the correct answer: ")
                    chest2(ui, lives)
                    break



def play_left3(ui):
    valid_choices = ['step','bypass','exit']
    choice = get_user_choice("You have 2 choices:\n1) You can Step on the plate\n2) Bypass the plate. Say 'Step' or 'Bypass'.",valid_choices, ui)
    if choice == 'step':
        step(ui)
        play_step(ui)
    elif choice == 'bypass':
        bypass(ui)
        gameover(ui)
    elif choice == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint("invalid")







def play_right3(ui):
    valid_choices = ['key','leave','exit']
    choice = get_user_choice("You must choose: Try to obtain the large key or leave the room. Say 'Key' or 'Leave'.",valid_choices, ui)
    if choice == "key":
        key(ui)
        gameover(ui)
    elif choice == "leave":
        leave(ui)
        left4(ui)
        play_left3(ui)
    elif choice == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint('invalid')









def play_basement(ui):
    valid_choices = ['left','light','exit']
    choice = get_user_choice("Which way will you choose? Say 'Left' or 'Light'.",valid_choices, ui)
    if choice == 'left':
        left3(ui)
        play_left3(ui)
    elif choice == 'light':
        right3(ui)
        play_right3(ui)
    elif choice == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint("invalid")


def play_right2(ui):
    valid_choices = ['library','continue','exit']
    choice = get_user_choice("What will you choose? Say 'Library' or 'Continue'.",valid_choices, ui)
    if choice == 'library':
        library(ui)
        gameover(ui)
    elif choice == 'continue':
        continue1(ui)
        basement(ui)
        play_basement(ui)
    elif choice == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint("invalid")



def play_corridor(ui):
    valid_choices=['left chamber','right chamber','exit']
    choice= get_user_choice("Which chamber will you choose? Say 'Left Chamber' or 'Right Chamber'.",valid_choices, ui)
    if choice == 'left chamber':
        left2(ui)
        gameover(ui)
    elif choice == 'right chamber':
        right2(ui)
        play_right2(ui)
    elif choice == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint("invalid")


def play_follow(ui):
    valid_choices=['corridor','basement','exit']
    choice = get_user_choice("What will it be? Say 'Corridor' or 'Basement'.",valid_choices, ui)
    if choice == 'corridor':
        corridor(ui)
        play_corridor(ui)
    elif choice == 'basement':
        basement(ui)
        play_basement(ui)
    elif choice == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint("invalid")

def play_entermonument(ui):
    valid_choices=['follow','explore','exit']
    choice = get_user_choice("What will you do?\nSay 'Follow' to follow the mysterious inscription on the wall!\nOR\nSay 'Explore' to explore the rest of the monument!",valid_choices, ui)
    if choice == 'follow':
        follow(ui)
        play_follow(ui)
    elif choice == 'explore':
        explore2(ui)
        play_explore2(ui)
    elif choice == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint('invalid')




def play_right(ui):
    valid_choices= ['enter','move back','exit']
    choice = get_user_choice("What will you do? Say 'Enter' or 'Move back'.",valid_choices, ui)
    if choice == 'enter':
        enter_monument(ui)
        play_entermonument(ui)
    elif choice == 'move back':
        moveback(ui)
        play_moveback(ui)
    elif choice == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint("invalid")




def play_moveback(ui):

    valid_choices = ['left', 'explore','exit']
    choice1 = get_user_choice("Which way will you choose? Say 'left' or 'explore'.", valid_choices, ui)

    if choice1 == 'left':
        left(ui)
        play_left(ui)
    elif choice1 == 'explore':
        right(ui)
        play_right(ui)
    elif choice1 == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint("Invalid choice. Game over.")


def play_left(ui):
    valid_choices2 = ['enter', 'move back','exit']
    choice2 = get_user_choice("Do you dare to enter this cave of the damned? Say 'Enter' or 'Move Back'.",valid_choices2, ui)

    if choice2 == "enter":
        cave(ui)
        play_cave(ui)
    elif choice2 == "move back":
        moveback(ui)
        play_moveback(ui)
    elif choice2 == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint("Invalid")


def play_game(ui): #TODO

    global answer_name

    answer_name = name3(ui)
    #print(answer_name)
    valid_choices = ['left', 'explore','exit']
    choice1 = get_user_choice("What you will do? Say 'left' or 'explore'.", valid_choices, ui, True)
    if choice1 == 'left':
        left(ui)
        play_left(ui)
    elif choice1 == 'explore':
        right(ui)
        play_right(ui)
    elif choice1 == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint("Invalid choice. Game over.")


########################################################## EXPLORE PART ####################################################

def play_explore2(ui):
    validchoices=['light','basement','exit']
    choice = get_user_choice("Which way would you like to go?\n1) The room with light\n2) Basement.\nSay 'Light' or 'Basement'.",validchoices, ui)
    if choice == "light":
        light(ui)
        play_light(ui)
    elif choice == "basement":
        basement2(ui)
        play_basement2(ui)
    elif choice == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint("invalid")

def play_basement2(ui):
    validchoices = ['left','corridor','exit']
    choice = get_user_choice("Which way will you choose? Say 'Left' or 'Corridor'.",validchoices, ui)
    if choice == "left":
        left5(ui)
        play_left5(ui)
    elif choice == "corridor":
        corridor2(ui)
        play_corridor2(ui)
    elif choice == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint('invalid')


def play_corridor2(ui):
    validchoices = ['map','leave','exit']
    choice = get_user_choice("Now you have 2 options:\n1) Try to obtain the large map\n2) Leave the room. Say 'Map' or 'Leave'.",validchoices, ui)
    if choice == "map":
        map1(ui)
        gameover(ui)
    elif choice == "leave":
        leave1(ui)
        left6(ui)
        play_left5(ui)
    elif choice == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint("invalid")



def play_left5(ui):
    validchoices = ['painting','escape','exit']
    choice = get_user_choice("Which path will you take? Say 'Painting' or 'Escape'.",validchoices, ui)
    if choice == "painting":
        painting(ui)
        play_painting(ui)
    elif choice == "escape":
        escape(ui)
        gameover(ui)
    elif choice == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint('invalid')



def play_light(ui):
    validchoices=['blood','spider','exit']
    choice = get_user_choice("Which way will you proceed? Say 'Blood' or 'Spider'.",validchoices, ui)
    if choice == "blood":
        blood(ui)
        play_blood(ui)
    elif choice == "spider":
        spider(ui)
        gameover(ui)
    elif choice == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint("invalid")



def play_blood(ui):
    validchoices = ['left stairs','right stairs','left stair','right stair','exit']
    choice = get_user_choice("Which staircase will you choose? Say 'Left Stairs' or 'Right Stairs'.",validchoices, ui)
    if choice == "left stairs" or choice == "left stair":
        leftstairs(ui)
        gameover(ui)
    elif choice == "right stairs" or choice == "right stair":
        rightstairs(ui)
        basement2(ui)
        play_basement2(ui)
    elif choice == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint("invalid")



def play_painting(ui):
    validchoices = ['dark room','chest','exit']
    choice = get_user_choice("Which path will you choose? Say 'Dark Room' or 'Chest'.",validchoices, ui)
    if choice == "dark room":
        mineshaft(ui)
        play_path(ui)
    elif choice == "chest":
        room(ui)
        gameover(ui)
    elif choice == 'exit':
        ui.terminalPrint('Exiting from Game!')
        speak(ui, 'Exiting from Game!')
        ui.current_task = None
    else:
        ui.terminalPrint("invalid")





