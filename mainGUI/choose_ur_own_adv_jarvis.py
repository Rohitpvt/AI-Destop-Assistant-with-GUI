import pyttsx3
import pygame


def playsound(sound_file):

    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.quit()



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(ui, text):
    ui.updateGifs("speaking")
    engine.say(text)
    engine.runAndWait()
def name3(ui):
    ui.terminalPrint("Welcome to the choose your own adventure game!")
    speak(ui, "Welcome to the choose your own adventure game!")
    ui.terminalPrint("Please enter your name: ")
    ui.current_task = "name-adv"
    while True:
        if ui.current_task == "adv-start":
            if ui.text2.isalpha():

                ui.terminalPrint(f'''Hi! {ui.text2.capitalize()} \n>>You have to make some correct decisions and find the TREASURE CHEST in order to win the game! Say 'Exit' at anytime to quit the game!
                                                Now move ahead and choose your own adventure!''')

                ui.terminalPrint("")
                return ui.text2

            else:
                ui.terminalPrint("Enter letters only!")
                speak(ui,"Enter letters only!")
                ui.terminalPrint("\nPlease enter your name: ")
                ui.current_task = "name-adv"

    #name = input("Please enter your name: ").capitalize()
    # if name.isalpha() == True:
    #     ui.terminalPrint(f'''Hi! {name} \n>>You have to make some correct decisions and find the TREASURE CHEST in order to win the game! Say 'Exit' at anytime to quit the game!
    #                                          Now move ahead and choose your own adventure!''')
    #
    #     speak(ui, f'''Hi!{name} \n>>You have to make some correct decisions and find the TREASURE CHEST in order to win the game! Say 'Exit' at anytime to quit the game! Now move ahead and choose your own adventure!''')
    #
    #     ui.terminalPrint("")
    #     start(ui)
    # else:
    #     ui.terminalPrint("Enter letters only!")
    # return name

def start(ui):
    ui.terminalPrint("")
    ui.terminalPrint("You are in a jungle, and there are 2 ways, either you can go left or you can explore other side of the jungle!")
    speak(ui, "You are in a jungle, and there are 2 ways, either you can go left or you can explore other side of the jungle!")
    ui.terminalPrint("")



def left(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You are walking in the jungle and It led you to a small clearing where you discovered a old and moss-covered cave entrance.
    The entrance exuded a malicious aura, and you could hear whispers in the wind, like the agonized moans of trapped souls.''')

    speak(ui, '''You are walking in the jungle and It led you to a small clearing where you discovered a old and moss-covered cave entrance.
        The entrance exuded a malicious aura, and you could hear whispers in the wind, like the agonized moans of trapped souls.''')
    ui.terminalPrint("")




def right(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You are walking in the jungle and after sometime you arrived to an ancient, overgrown monument of a king in the silent jungle.''')
    speak(ui, '''You are walking in the jungle and after sometime you arrived to an ancient, overgrown monument of a king in the silent jungle.''')
    playsound('./sounds/right.mp3')
    ui.terminalPrint('''You have two choices: Enter the monument and discover its secrets, but beware of possible dangers, or move back.''')

    speak(ui, '''You have two choices: Enter the monument and discover its secrets, but beware of possible dangers, or move back.''')

    ui.terminalPrint("")


def follow(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You follow the inscription and reach a broken doorway with two paths: one leading further into a dimly lit corridor and the other going down into a dark, barely visible basement. Your choice could be life or death.''')
    speak(ui,'''You follow the inscription and reach a broken doorway with two paths: one leading further into a dimly lit corridor and the other going down into a dark, barely visible basement. Your choice could be life or death.''')
    ui.terminalPrint("")




def corridor(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You enter a mysterious room filled with pictures showing the monument's history and a deadly war. As you move forward, you see two chambers with traps, but one of them has a correct path to avoid the trap.''')

    speak(ui, '''You enter a mysterious room filled with pictures showing the monument's history and a deadly war. As you move forward, you see two chambers with traps, but one of them has a correct path to avoid the trap.''')
    ui.terminalPrint("")


def left2(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''As you entered in the chamber, there was many blood slicked on the walls and floor. You chose the wrong the chamber, TRAP ACTIVATED!!! Spikes come up and tears you apart.''')
    speak(ui, '''As you entered in the chamber, there was many blood slicked on the walls and floor. You chose the wrong the chamber, TRAP ACTIVATED!!! Spikes come up and tears you apart.''')
    ui.terminalPrint("")


def right2(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You come into a room with dead bodies but avoid traps. Ahead, there are two corridors leading to two doors: one to a library and the other deeper into the monument for more research.
     You have two choices: go to the library with helpful books to reach treasure or continue down the quiet corridor.''')
    speak(ui,'''You come into a room with dead bodies but avoid traps. Ahead, there are two corridors leading to two doors: one to a library and the other deeper into the monument for more research.
     You have two choices: go to the library with helpful books to reach treasure or continue down the quiet corridor.''')
    ui.terminalPrint("")


def library(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You picked the corridor leading to the library with tall bookshelves. As you decided to select a book to get hint for reaching treasure, it set off a trap, causing the roof and shelves to collapse on you.''')
    speak(ui,  '''You picked the corridor leading to the library with tall bookshelves. As you decided to select a book to get hint for reaching treasure, it set off a trap, causing the roof and shelves to collapse on you.''')
    playsound('./sounds/library , key.mp3')
    ui.terminalPrint('''You couldn't escape in time''')
    speak(ui,  '''You couldn't escape in time''')
    ui.terminalPrint("")


def continue1(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''As you moved on to silent corridor , suddenly the floor starts cracking and breaks down because the floor was weak''')
    speak(ui,  '''As you moved on to silent corridor , suddenly the floor starts cracking and breaks down because the floor was weak''')
    playsound('./sounds/continue1.mp3')
    ui.terminalPrint('''Then you reached to the dark unknown basement which you barely can see anything.''')
    speak(ui, '''Then you reached to the dark unknown basement which you barely can see anything.''')
    ui.terminalPrint("")



def basement(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''Driven by curiosity, you head down into the dark basement. You find a torch on the wall and take it. As you go deeper, it gets colder, and the air feels heavier.''')
    speak(ui,  '''Driven by curiosity, you head down into the dark basement. You find a torch on the wall and take it. As you go deeper, it gets colder, and the air feels heavier.''')
    playsound('./sounds/basement.mp3')
    ui.terminalPrint('''The only light is from your torch. Then, you come to a point where the path splits. On the left is a narrow, twisting corridor, and on the right, there's a faint bluish light.''')

    speak(ui,  '''The only light is from your torch. Then, you come to a point where the path splits. On the left is a narrow, twisting corridor, and on the right, there's a faint bluish light.''')
    ui.terminalPrint("")



def left3(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You decided to go left and found a chamber with ancient stuff and a chest. But there's a problem - you see a pressure plate on the floor that might set off a trap.''')
    speak(ui,  '''You decided to go left and found a chamber with ancient stuff and a chest. But there's a problem - you see a pressure plate on the floor that might set off a trap.''')
    ui.terminalPrint("")



def step(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''Stepping on a plate, a secret door in the wall revealed two corridors. One corridor was lit with torches, and the other corridor led to a well-lit room filled with ancient chests containing valuable items.''')
    speak(ui, '''Stepping on a plate, a secret door in the wall revealed two corridors. One corridor was lit with torches, and the other corridor led to a well-lit room filled with ancient chests containing valuable items.''')
    ui.terminalPrint("")


def bypass(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You advanced down the corridor ignoring the plate''')
    speak(ui,  '''You advanced down the corridor ignoring the plate''')
    playsound('./sounds/bypass (1).mp3')
    ui.terminalPrint('''Unaware of a hidden tripwire. It triggered a wall of spears that struck you.''')
    speak(ui,  '''Unaware of a hidden tripwire. It triggered a wall of spears that struck you.''')
    playsound('./sounds/bypass.mp3')
    ui.terminalPrint('''You didn't feel at that moment.''')
    speak(ui,  '''you didn't feel at that moment.''')
    ui.terminalPrint("")

def key(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You attempted to reach for the key and as soon as you picked up the key, it triggered a hidden mechanism which closed the door, and the walls and roof collapsed.''')
    speak(ui,  '''You attempted to reach for the key and as soon as you picked up the key, it triggered a hidden mechanism which closed the door, and the walls and roof collapsed.''')
    playsound('./sounds/key.mp3')
    ui.terminalPrint('''You couldn't escape. Your quest for the large key ended tragically as the room's defenses proved too formidable.''')

    speak(ui,  '''You couldn't escape. Your quest for the large key ended tragically as the room's defenses proved too formidable.''')
    ui.terminalPrint("")

def leave(ui):
    ui.terminalPrint("")
    ui.terminalPrint(''' You moved back, leaved the area and again you reached the point where two paths were seen, left and right, now you continued to walk on left path. ''')
    speak(ui,  ''' You moved back, leaved the area and again you reached the point where two paths were seen, left and right, now you continued to walk on left path. ''')
    playsound('./sounds/leave.mp3')
    ui.terminalPrint("")


def left4(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''As you were walking left path, you found a chamber with ancient stuff and a chest. But there's a problem - you see a pressure plate on the floor that might set off a trap.''')
    speak(ui,  '''As you were walking left path, you found a chamber with ancient stuff and a chest. But there's a problem - you see a pressure plate on the floor that might set off a trap.''')
    ui.terminalPrint("")




def right3(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You decided to move forward instead of entering the dark corridor on the left. At the end of the corridor, you found a peaceful room with very valuable things. 
    In the center, there was a large magical key that could potentially help you to open the King's treasure.''')

    speak(ui,  '''You decided to move forward instead of entering the dark corridor on the left. At the end of the corridor, you found a peaceful room with very valuable things. 
    In the center, there was a large magical key that could potentially help you to open the King's treasure.''')
    ui.terminalPrint("")


def path(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You chose the torchlit path and entered a room adorned with diamonds and gold. It led to Curiosity drove you to explore it. Inside, you found a treasure chest, but the room was full of traps.
    One wrong move could be deadly. To open the chest, you needed a combination of letters, and a note on the wall might have the answer.''')

    speak(ui, '''You chose the torchlit path and entered a room adorned with diamonds and gold. It led to Curiosity drove you to explore it. Inside, you found a treasure chest, but the room was full of traps.
    One wrong move could be deadly. To open the chest, you needed a combination of letters, and a note on the wall might have the answer.''')
    ui.terminalPrint("")



def note2(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''Solve this riddle to open the treasure chest: 
    "I'm a word you possess, but you can't touch or hold me, a label that carries your history and meaning. I'm unique to you, but I'm not physical. You answer to me, but I'm not a question. What am I?"\n\nNOTE: YOU ONLY HAVE 3 LIVES''')

    speak(ui, '''Solve this riddle to open the treasure chest: 
    "I'm a word you possess, but you can't touch or hold me, a label that carries your history and meaning. I'm unique to you, but I'm not physical. You answer to me, but I'm not a question. What am I?"\n\nNOTE: YOU ONLY HAVE 3 LIVES''')

    ui.terminalPrint("")




def room(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You entered the room filled with countless ancient chests and decided to open one. After checking four chests with no success as they were locked, the fifth one revealed an Ancient precious Artifact. 
    When you picked it up, this triggered hidden trap, unlocking all the chests and releasing a swarm of scorpions from them. With no escape, you were overwhelmed by the scorpions and met your demise.''')

    speak(ui, '''You entered the room filled with countless ancient chests and decided to open one. After checking four chests with no success as they were locked, the fifth one revealed an Ancient precious Artifact. 
    When you picked it up, this triggered hidden trap, unlocking all the chests and releasing a swarm of scorpions from them. With no escape, you were overwhelmed by the scorpions and met your demise.''')
    ui.terminalPrint("")







def enter_monument(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You enter the dark monument and find strange hallways and chambers. You discover two paths: one path with a mysterious inscription on the wall and the other path leading deeper into the monument.''')

    speak(ui,  '''You enter the dark monument and find strange hallways and chambers. You discover two paths: one path with a mysterious inscription on the wall and the other path leading deeper into the monument.''')
    ui.terminalPrint("")

def cave(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''As you explore the cave, you saw many skeletons hanging on the wall and you could see countless skeletal remains, their hollow eyes seeming to follow your every move. 
	Then you saw 2 ways. One way, there are many dead bodies on the floor and second way, you could hear some disturbing and spooky sounds!''')

    speak(ui, '''As you explore the cave, you saw many skeletons hanging on the wall and you could see countless skeletal remains, their hollow eyes seeming to follow your every move. 
	Then you saw 2 ways. One way, there are many dead bodies on the floor and second way, you could hear some disturbing and spooky sounds!''')

    ui.terminalPrint("")



def moveback(ui):
    start(ui)

def deadbody(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You followed the path which was littered with the lifeless bodies of human. The ground was slick with an unknown substance. 
    Suddenly, without warning, the entrance of the path behind you collapsed with a deafening crash.''')
    speak(ui, '''You followed the path which was littered with the lifeless bodies of human. The ground was slick with an unknown substance. 
    Suddenly, without warning, the entrance of the path behind you collapsed with a deafening crash.''')
    playsound('./sounds/deadbody.mp3')
    ui.terminalPrint('''You turned in shock, realizing that you were now trapped in this lifeless corridor. You are moving forward.
    In the dim light, a shadowy figure of an unknown creature flickered on the periphery of your vision. 
    Your heart raced as you faced a crucial decision, each option fraught with uncertainty.''')

    speak(ui,  '''You turned in shock, realizing that you were now trapped in this lifeless corridor. You are moving forward.
    In the dim light, a shadowy figure of an unknown creature flickered on the periphery of your vision. 
    Your heart raced as you faced a crucial decision, each option fraught with uncertainty.''')

    ui.terminalPrint("")



def sound(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You went down the path with the spooky sounds. As you went forward, the strange noises became louder. After a while, you found out that the spooky and mysterious sounds were just some bats and rats.''')
    speak(ui,  '''You went down the path with the spooky sounds. As you went forward, the strange noises became louder. After a while, you found out that the spooky and mysterious sounds were just some bats and rats.''')
    playsound('./sounds/sound.mp3')
    ui.terminalPrint('''Among them, you found a key on the floor and picked it up. With a relieved sigh, you kept going deeper into the cave. 
             The path twisted and turned, taking you through narrow passages and into dimly lit rooms. 
	         Finally, you reached a huge underground cavern with an old, shaky bridge over a gap. ''')

    speak(ui,'''Among them, you found a key on the floor and picked it up. With a relieved sigh, you kept going deeper into the cave. The path twisted and turned, taking you through narrow passages and into dimly lit rooms. 
    Finally, you reached a huge underground cavern with an old, shaky bridge over a gap. ''')
    ui.terminalPrint("")

def bridge2(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You walked carefully on the wobbly bridge to a hidden room.''')
    speak(ui,"You walked carefully on the wobbly bridge to a hidden room.")
    playsound('./sounds/bridge2.mp3')
    ui.terminalPrint('''In that room, you found an old dusty journal with strange clues about where the pirate's treasure might be. 
    The journal hinted at a secret path further in the cave. Following the clues, you moved through narrow spots and dark rooms. At last, you came to a big stone door with a keyhole. 
    You put the key in the lock which you got earlier, turned it, and the door opened. Once the door swung open, you faced two paths. 
    In one corridor, there were spikes on the floor, but you couldn't tell if they were active or not. The other corridor led straight ahead, but the roof and floor had dangerous cracks.''')

    speak(ui, '''In that room, you found an old dusty journal with strange clues about where the pirate's treasure might be. 
    The journal hinted at a secret path further in the cave. Following the clues, you moved through narrow spots and dark rooms. At last, you came to a big stone door with a keyhole. 
    You put the key in the lock which you got earlier, turned it, and the door opened. Once the door swung open, you faced two paths. 
    In one corridor, there were spikes on the floor, but you couldn't tell if they were active or not. The other corridor led straight ahead, but the roof and floor had dangerous cracks.''')

    ui.terminalPrint("")


def spikes(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You chose to go down the corridor with spikes and accidentally you stepped on a pressure plate, and the roof above the corridor collapsed which destroyed all the traps and made a way for you. 
    Moving ahead, you faced a long, dark corridor ahead. It was getting colder, and you could hear water dripping somewhere far away.''')
    speak(ui,  '''You chose to go down the corridor with spikes and accidentally you stepped on a pressure plate, and the roof above the corridor collapsed which destroyed all the traps and made a way for you. 
    Moving ahead, you faced a long, dark corridor ahead. It was getting colder, and you could hear water dripping somewhere far away.''')

    playsound('./sounds/spikes.mp3')

    ui.terminalPrint('''It led you to an underground dock, where a haunting quietness enveloped an ancient pirate ship that appeared ghostly. 
    Curiosity drove you to explore it. Inside, you found a treasure chest, but the room was full of traps. One wrong move could be deadly. 
    To open the chest, you needed a four-digit code, and a note on the wall might have the answer.''')

    speak(ui,  '''It led you to an underground dock, where a haunting quietness enveloped an ancient pirate ship that appeared ghostly. 
    Curiosity drove you to explore it. Inside, you found a treasure chest, but the room was full of traps. One wrong move could be deadly. 
    To open the chest, you needed a four-digit code, and a note on the wall might have the answer.''')

    ui.terminalPrint("")


def crack(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You chose the corridor that led straight ahead, despite the ominous cracks. But, oh no! As you walked, you unknowingly triggered a pressure plate.''')
    speak(ui,  "You chose the corridor that led straight ahead, despite the ominous cracks. But, oh no! As you walked, you unknowingly triggered a pressure plate.")
    playsound('./sounds/crack.mp3')
    ui.terminalPrint('''In an instant, the roof above you came crashing down, and there was no way to escape.''')
    speak(ui,  "In an instant, the roof above you came crashing down, and there was no way to escape.")
    playsound('./sounds/crack2.mp3')


    ui.terminalPrint("")



def explore(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''Instead of crossing the bridge, you explored the cave's dark corners. There, you spotted a rusty lever half-buried in the floor. 
    With a powerful effort, you pulled it, and the ground trembled. A massive stone door slowly creaked open, revealing a dimly lit chamber. 
    It held pirate relics – dusty maps, tattered flags, and shining trinkets. Amid these treasures, you found a map that hinted at the pirate's loot and marked two paths deeper into the cave.''')

    speak(ui,  '''Instead of crossing the bridge, you explored the cave's dark corners. There, you spotted a rusty lever half-buried in the floor. 
    With a powerful effort, you pulled it, and the ground trembled. A massive stone door slowly creaked open, revealing a dimly lit chamber. 
    It held pirate relics – dusty maps, tattered flags, and shining trinkets. Amid these treasures, you found a map that hinted at the pirate's loot and marked two paths deeper into the cave.''')

    ui.terminalPrint("")


def tunnel(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You picked the map's path into a twisty maze of tunnels. The passages got tighter and confusing. Soon, you were trapped in a small chamber with no way out.
    You accidentally triggered a hidden switch''')
    speak(ui,  '''You picked the map's path into a twisty maze of tunnels. The passages got tighter and confusing. Soon, you were trapped in a small chamber with no way out.
    You accidentally triggered a hidden switch''')
    playsound('./sounds/tunnel.mp3')
    ui.terminalPrint('''And the walls started closing in. You panicked as the walls pressed on, and you couldn't escape. 
    No matter how hard you pushed, the walls squeezed you against them, ending your journey in a suffocating squeeze.''')

    speak(ui,  '''And the walls started closing in. You panicked as the walls pressed on, and you couldn't escape. 
    No matter how hard you pushed, the walls squeezed you against them, ending your journey in a suffocating squeeze.''')
    ui.terminalPrint("")


def river(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You took the river route marked on the map. In a small, shaky boat, you tackled rough water. The river got wilder, and you struggled to steer.
    Suddenly, the river turned sharply, and you went over an underground waterfall.''')
    speak(ui, '''You took the river route marked on the map. In a small, shaky boat, you tackled rough water. The river got wilder, and you struggled to steer.
     Suddenly, the river turned sharply, and you went over an underground waterfall.''')
    playsound('./sounds/river.mp3')
    ui.terminalPrint('''Your boat plunged down, and you sank into the churning water below. The waterfall's strong pull was too much, and you couldn't swim back up. The river took your life, and your fate remained a secret in the cave's depths.''')

    speak(ui, '''You took the river route marked on the map. In a small, shaky boat, you tackled rough water. The river got wilder, and you struggled to steer.
    Suddenly, the river turned sharply, and you went over an underground waterfall. Your boat plunged down, and you sank into the churning water below. 
    The waterfall's strong pull was too much, and you couldn't swim back up. The river took your life, and your fate remained a secret in the cave's depths.''')

    ui.terminalPrint("")


def makesound(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''As you hesitated, you made a noise—just a tiny sound. But that sound caught the attention of something sinister nearby.
	A horrifying creature, hidden in the thick mist, rushed toward you with frightening speed. It looked like a twisted nightmare, all sharp claws and menacing eyes.
	Before you could react, the creature attacked you.''')
    speak(ui, '''As you hesitated, you made a noise—just a tiny sound. But that sound caught the attention of something sinister nearby.
    	A horrifying creature, hidden in the thick mist, rushed toward you with frightening speed. It looked like a twisted nightmare, all sharp claws and menacing eyes.
    	Before you could react, the creature attacked you.''')
    playsound('./sounds/makesound.mp3')
    ui.terminalPrint('''Its claws tore into your flesh, causing excruciating pain. You realized you were in a life-or-death struggle.
    But the creature just didn't stop, and eventually, it overpowered you.''')

    speak(ui, ''' Its claws tore into your flesh, causing excruciating pain. You realized you were in a life-or-death struggle.
    But the creature just didn't stop, and eventually, it overpowered you.''')

    ui.terminalPrint("")


def gameover(ui):
    ui.terminalPrint("")
    ui.terminalPrint("YOU ARE DEAD NOW! GAME OVER!")
    speak(ui, "You are dead now! GAME OVER!")
    ui.terminalPrint("")
    ui.current_task = None

def goclose(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You moved quietly toward the shadowy figure, trying to get a better look. gradually, you could see a frightening creature with large, bloody teeth. 
    Your heart raced as you realized just how dangerous this creature could be. That creature was busy in eating flesh of a human. ''')
    speak(ui, '''You moved quietly toward the shadowy figure, trying to get a better look. gradually, you could see a frightening creature with large, bloody teeth. 
    Your heart raced as you realized just how dangerous this creature could be. That creature was busy in eating flesh of a human. ''')
    playsound('./sounds/deep monster growl.mp3')
    ui.terminalPrint('''Its menacing presence, highlighted by those sharp, bloody teeth, sent a shiver of fear down your spine, making it clear that you were in a very risky situation. 
    The creature wasn't looking in your direction, so it didn't know you were there.''')

    speak(ui, '''Its menacing presence, highlighted by those sharp, bloody teeth, sent a shiver of fear down your spine, making it clear that you were in a very risky situation. 
    The creature wasn't looking in your direction, so it didn't know you were there.''')
    ui.terminalPrint("")


def throwstone(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You grabbed a sharp-edged stone and tossed it into the nearby lake.''')
    speak(ui, '''You grabbed a sharp-edged stone and tossed it into the nearby lake.''')
    playsound('./sounds/throwstone.mp3')
    ui.terminalPrint('''The creature, filled with anger, immediately rushed towards the disturbance. 
    Now, your path is clear and you are moving forward. As you continued forward, your path brought you to a crucial moment. 
    To reach the other side of the cave, you had to cross a rickety, ancient bridge hanging above a furious, churning river below.
	The bridge, worn by the ages, wobbled and groaned with every step. It felt like it might collapse at any moment. Beneath, in the turbulent waters, you noticed an old and fragile boat gently rocking.
	You faced a dilemma: crossing the shaky bridge was risky, where one wrong move could send you into the unforgiving waters. 
	On the other hand, the boat presented its own set of mysteries and potential dangers as you contemplated your next move in this spine-tingling abyss.''')

    speak(ui, '''The creature, filled with anger, immediately rushed towards the disturbance. 
    Now, your path is clear and you are moving forward. As you continued forward, your path brought you to a crucial moment. 
    To reach the other side of the cave, you had to cross a rickety, ancient bridge hanging above a furious, churning river below.
    The bridge, worn by the ages, wobbled and groaned with every step. It felt like it might collapse at any moment. Beneath, in the turbulent waters, you noticed an old and fragile boat gently rocking.
    You faced a dilemma: crossing the shaky bridge was risky, where one wrong move could send you into the unforgiving waters. 
    On the other hand, the boat presented its own set of mysteries and potential dangers as you contemplated your next move in this spine-tingling abyss.''')

    ui.terminalPrint("")


def sneak(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You were sneaking up on the creature from behind, trying not to make a sound. But then, by mistake, your foot crunched some dry leaves, making a noise. 
    The creature heard it and turned around, its eyes filled with anger and hunger. It charged straight at you with a growl. 
    It looked like a twisted nightmare, all sharp claws and menacing eyes. Before you could react, the creature attacked you. 
    Its claws tore into your flesh, causing excruciating pain. You realized you were in a life-or-death struggle.
    But the creature just didn't stop, and eventually, it overpowered you. ''')

    speak(ui, '''You were sneaking up on the creature from behind, trying not to make a sound. But then, by mistake, your foot crunched some dry leaves, making a noise. 
    The creature heard it and turned around, its eyes filled with anger and hunger. It charged straight at you with a growl. 
    It looked like a twisted nightmare, all sharp claws and menacing eyes. Before you could react, the creature attacked you. 
    Its claws tore into your flesh, causing excruciating pain. You realized you were in a life-or-death struggle.
    But the creature just didn't stop, and eventually, it overpowered you. ''')

    ui.terminalPrint("")


def bridge(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''Choosing the wobbly bridge felt brave, but it turned terrifying. The bridge broke, plunging you into the rushing sea. In moments, a massive, fearsome shark appeared. 
    It attacked quickly, you realized you were in a life-or-death struggle. But the bloody shark just didn't stop, and eventually, it overpowered you in the dangerous waters.''')

    speak(ui, '''Choosing the wobbly bridge felt brave, but it turned terrifying. The bridge broke, plunging you into the rushing sea. In moments, a massive, fearsome shark appeared. 
    It attacked quickly, you realized you were in a life-or-death struggle. But the bloody shark just didn't stop, and eventually, it overpowered you in the dangerous waters.''')

    ui.terminalPrint("")


def boat(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You chose the weak boat and floated towards the distant light. It led you to the open sea.''')
    speak(ui, '''You chose the weak boat and floated towards the distant light. It led you to the open sea.''')
    playsound('./sounds/boat.mp3')
    ui.terminalPrint('''In the distance, a massive, very old pirate ship caught your eye. Curiosity drove you to explore it. Inside, you found a treasure chest, but the room was full of traps. 
    One wrong move could be deadly. To open the chest, you needed a four-digit code, and a note on the wall might have the answer.''')

    speak(ui, '''In the distance, a massive, very old pirate ship caught your eye. Curiosity drove you to explore it. Inside, you found a treasure chest, but the room was full of traps. One wrong move could be deadly. 
    To open the chest, you needed a four-digit code, and a note on the wall might have the answer.''')

    ui.terminalPrint("")

def note(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''Solve this riddle to open the treasure chest:\n"I'm always moving, but I never get anywhere. I can be wasted, spent, or even saved. I can fly without wings and keep you on track. I am always watching you, I know when you are sad and when you are happy."\n\nNOTE: YOU ONLY HAVE 3 LIVES''')
    speak(ui, '''Solve this riddle to open the treasure chest:\n"I'm always moving, but I never get anywhere. I can be wasted, spent, or even saved. I can fly without wings and keep you on track. I am always watching you, I know when you are sad and when you are happy."\n\nNOTE: YOU ONLY HAVE 3 LIVES''')

    ui.terminalPrint("")


################################################################################################### EXPLORE PART ##########################################################################################

def explore2(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You chose to explore the monument, where you faced a decision. One room had inviting lights and something precious, 
    while the other was a staircase which goes down to the basement area which was dark , lil bit of light was there.''')

    speak(ui, '''You chose to explore the monument, where you faced a decision. One room had inviting lights and something precious, 
    while the other was a staircase which goes down to the basement area which was dark , lil bit of light was there.''')
    ui.terminalPrint("")

def light(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You chose the room with the light, adorned with torches and a beautiful gold chandelier above. As you admired the room's beauty, You accidentally pressed a pressure plate,
     causing a hidden space on the wall to rotate halfway. It revealed two paths that changed your course. One path led to a long red room with blood stains, while the other led to a room infested with dangerous spiders.''')

    speak(ui, '''You chose the room with the light, adorned with torches and a beautiful gold chandelier above. As you admired the room's beauty, You accidentally pressed a pressure plate,
     causing a hidden space on the wall to rotate halfway. It revealed two paths that changed your course. One path led to a long red room with blood stains, while the other led to a room infested with dangerous spiders.''')
    ui.terminalPrint("")

def basement2(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''Driven by curiosity, you head down into the dark basement. You find a torch on the wall and take it. As you go deeper, it gets colder, and the air feels heavier.''')
    speak(ui, '''Driven by curiosity, you head down into the dark basement. You find a torch on the wall and take it. As you go deeper, it gets colder, and the air feels heavier.''')
    playsound('./sounds/Basement2.mp3')
    ui.terminalPrint('''The only light is from your torch. Then, you come to a point where the path splits. On the left there's a room of mirrors and on the right, is a narrow, twisting corridor.''')

    speak(ui, '''The only light is from your torch. Then, you come to a point where the path splits. On the left there's a room of mirrors and on the right, is a narrow, twisting corridor.''')
    ui.terminalPrint("")

def blood(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You chose the room where many blood stains were there. You moved half of the corridor and you found some dead bodies on the floor which blocked your way. You tried to shift them so that you go further. 
    But , you noticed there were two staircase holes, left and right, below bodies which go downwards into the basement. The staircase size was very narrow, and dark inside. Your choice could be life or death.''')

    speak(ui, '''You chose the room where many blood stains were there. You moved half of the corridor and you found some dead bodies on the floor which blocked your way. You tried to shift them so that you go further. 
    But , you noticed there were two staircase holes, left and right, below bodies which go downwards into the basement. The staircase size was very narrow, and dark inside. Your choice could be life or death.''')
    ui.terminalPrint("")

def spider(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You chose the room with cobwebs and dangerous spiders. Among the chests, you hoped to find something valuable in the ancient ones, so you opened one. Unfortunately, it triggered a hidden trap that blocked the entrance with a collapsing roof. 
    A small hole in the wall began leaking oil, and a fallen torch ignited the oil. The fire spread rapidly, and though you tried to clear the blocked path, it took too long, and you perished in the flames.''')

    speak(ui, '''You chose the room with cobwebs and dangerous spiders. Among the chests, you hoped to find something valuable in the ancient ones, so you opened one. Unfortunately, it triggered a hidden trap that blocked the entrance with a collapsing roof. 
    A small hole in the wall began leaking oil, and a fallen torch ignited the oil. The fire spread rapidly, and though you tried to clear the blocked path, it took too long, and you perished in the flames.''')
    ui.terminalPrint("")


def left5(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You chose the left path and found yourself in a room filled with big, clean mirrors. Shards of glass littered the floor, and as you carefully examined the mirrors, you noticed all but two reflected your image.\nBreaking one of these fake mirrors revealed two options:
    A path leading to a collection of captivating old paintings holding the king's secret\nOR\nA long corridor that seemed to lead to the promise of sunlight and potential escape from the monument.''')

    speak(ui, '''You chose the left path and found yourself in a room filled with big, clean mirrors. Shards of glass littered the floor, and as you carefully examined the mirrors, you noticed all but two reflected your image. Breaking one of these fake mirrors revealed two options: 
    A path leading to a collection of captivating old paintings holding the king's secret OR A long corridor that seemed to lead to the promise of sunlight and potential escape from the monument.''')
    ui.terminalPrint("")


def corridor2(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You decided to move forward in the narrow and twisting corridor instead of entering the room of mirror on the left. 
    At the end of the corridor, you found a peaceful room with different chest and gold everywhere. In the center, there was a large map with the 'X' marked on it that could potentially lead you to the King's treasure.''')

    speak(ui, '''You decided to move forward in the narrow and twisting corridor instead of entering the room of mirror on the left. 
    At the end of the corridor, you found a peaceful room with different chest and gold everywhere. In the center, there was a large map with the 'X' marked on it that could potentially lead you to the King's treasure.''')

    ui.terminalPrint("")

def map1(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You found the map with the X mark and picked it up, eager to continue your journey. However, your joy was short-lived as you heard a mechanism activate. Unfortunately, the map triggered a trap, causing holes in the floor to release deadly green gas, which turned out to be poisonous. 
    The room's door sealed shut, leaving you with no escape. Your quest for the map ended in tragedy as the poisonous gas filled the room, and you took your final breath.''')
    speak(ui, '''You found the map with the X mark and picked it up, eager to continue your journey. However, your joy was short-lived as you heard a mechanism activate. Unfortunately, the map triggered a trap, causing holes in the floor to release deadly green gas, which turned out to be poisonous. 
    The room's door sealed shut, leaving you with no escape. Your quest for the map ended in tragedy as the poisonous gas filled the room, and you took your final breath.''')
    ui.terminalPrint("")

def leave1(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You decided not to take the map. You moved back, leaved the area and again you reached the point where two paths were seen, left path and corridor path, now you continued to walk on left path.''')
    speak(ui, '''You decided not to take the map. You moved back, leaved the area and again you reached the point where two paths were seen, left path and corridor path, now you continued to walk on left path.''')
    ui.terminalPrint("")

def left6(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''Now you are on the left path and found yourself in a room filled with big, clean mirrors. Shards of glass littered the floor, and as you carefully examined the mirrors, you noticed all but two reflected your image. 
    Breaking one of these fake mirrors revealed two options:\nA path leading to a collection of captivating old paintings holding the king's secret\nOR\na long corridor that seemed to lead to the promise of sunlight and potential escape from the monument. ''')

    speak(ui, '''Now you are on the left path and found yourself in a room filled with big, clean mirrors. Shards of glass littered the floor, and as you carefully examined the mirrors, you noticed all but two reflected your image. 
    Breaking one of these fake mirrors revealed two options: a path leading to a collection of captivating old paintings holding the king's secret OR a long corridor that seemed to lead to the promise of sunlight and potential escape from the monument. ''')
    ui.terminalPrint("")


def painting(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You chose the path with the intriguing paintings that seemed to depict both current and past events. While engrossed in reading them, you accidentally triggered a tripwire. 
    Rather than another trap, two paintings fell, revealing a secret passage. One path was going to the dark room with no sign of light, and the other led to a well-lit room filled with ancient chests containing valuable items.''')
    speak(ui, '''You chose the path with the intriguing paintings that seemed to depict both current and past events. While engrossed in reading them, you accidentally triggered a tripwire. 
    Rather than another trap, two paintings fell, revealing a secret passage. One path was going to the dark room with no sign of light, and the other led to a well-lit room filled with ancient chests containing valuable items.''')
    ui.terminalPrint("")

def escape(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''As you continued down the corridor with the pleasant sounds of birds and waterfalls growing louder''')
    speak(ui, '''As you continued down the corridor with the pleasant sounds of birds and waterfalls growing louder''')
    playsound('./sounds/escape.mp3')
    ui.terminalPrint('''You approached what appeared to be the exit bathed in sunlight. 
    However, it turned out to be a mirage, and you heard an unfamiliar, unsettling noise. Realizing the danger, you narrowly avoided falling into a deadly pit inhabited by ravenous creatures. 
    But just as you thought you were safe, the ground beneath you collapsed, and you fell into the pit. The hungry creatures swarmed over you, making you their meal.''')

    speak(ui, '''You approached what appeared to be the exit bathed in sunlight. However, it turned out to be a mirage, and you heard an unfamiliar, unsettling noise. Realizing the danger, you narrowly avoided falling into a deadly pit inhabited by ravenous creatures. 
    But just as you thought you were safe, the ground beneath you collapsed, and you fell into the pit. The hungry creatures swarmed over you, making you their meal.''')
    ui.terminalPrint("")

def leftstairs(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You picked the left stairs and went down into total darkness. It was so dark that not even a lit light helped. The stairs were uneven, and you slipped, but held onto the wall. 
    Sadly, you accidentally pressed a button, and the walls on both sides began closing in, risking your life. You tried to go back upstairs, but the space narrowed, leaving no escape. 
    The walls joined together, and you were crushed to death''')

    speak(ui, '''You picked the left stairs and went down into total darkness. It was so dark that not even a lit light helped. The stairs were uneven, and you slipped, but held onto the wall. 
    Sadly, you accidentally pressed a button, and the walls on both sides began closing in, risking your life. You tried to go back upstairs, but the space narrowed, leaving no escape. 
    The walls joined together, and you were crushed to death''')
    ui.terminalPrint("")

def rightstairs(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You chose the right stairs and descended into complete darkness. It was so dark that even a lit light couldn't penetrate it. 
    As you continued down, you noticed a distant glow of light. Approaching it, you realized you had reached the basement''')

    speak(ui, '''You chose the right stairs and descended into complete darkness. It was so dark that even a lit light couldn't penetrate it. 
    As you continued down, you noticed a distant glow of light. Approaching it, you realized you had reached the basement''')
    ui.terminalPrint("")

def mineshaft(ui):
    ui.terminalPrint("")
    ui.terminalPrint('''You chose the dark room, which was filled with mineshaft equipment. In the darkness, you found a beam of light and a mirror. Adjusting the mirror illuminated the room. 
    Amidst mining tools, you spotted an unusual floor pattern and used a shovel to find out the reason behind unusual floor pattern. And after sometime of digging, you find out the King's Treasure Chest which was locked! 
    However, the room was filled with traps. One wrong move could be deadly. To open the chest, you needed a combination of letters, and a note on the wall might have the answer.''')

    speak(ui,  '''You chose the dark room, which was filled with mineshaft equipment. In the darkness, you found a beam of light and a mirror. Adjusting the mirror illuminated the room. 
    Amidst mining tools, you spotted an unusual floor pattern and used a shovel to find out the reason behind unusual floor pattern. And after sometime of digging, you find out the King's Treasure Chest which was locked! 
    However, the room was filled with traps. One wrong move could be deadly. To open the chest, you needed a combination of letters, and a note on the wall might have the answer.''')
    ui.terminalPrint("")
























