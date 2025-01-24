#This pokemon themed hangman is based on the first 151 original Pokemon! Hope ypu enjoy!
#Note! Mr. Mime and Farfetch'd are renamed to "mrmime" and "farfetchd" for the sake of the code.

#Functions
from tkinter import *
from tkinter import messagebox
import random
from PIL import ImageTk, Image

    #***Part One: Functions of my game***

#Guessing function
def guess_button():
    global attempts
    letter = user_entry.get().lower()
    if letter.isalpha() and len(letter) == 1:
#Check is a letter was guessed already
        if letter in guess_already:
            messagebox.showerror("Note", "No way you guessed {} again...".format(letter.upper()))
            user_entry.delete(0, len(letter)+1)
#Places correct letter in its spot
        elif letter in random_poke:
            for i in range(len(random_poke)):
                if letter == random_poke[i]:
                    blanks_list[i] = letter
                    label_word.config(text = " ".join(blanks_list).upper())
                    guess_already.append(letter)
                    user_entry.delete(0, len(letter)+1)
            if attempts > 0 and "_" not in blanks_list:
                messagebox.showinfo("Note", "Your guess was correct!")
                
#Incorrect guesses leading to Pikachu's demise.
        elif letter not in random_poke:
            attempts -= 1
            if attempts == 5:
                background.config(image = pika_2)
                user_entry.delete(0, len(letter)+1)
            elif attempts == 4:
                background.config(image = pika_3)
                user_entry.delete(0, len(letter)+1)
            elif attempts == 3:
                background.config(image = pika_4)
                user_entry.delete(0, len(letter)+1)
            elif attempts == 2:
                background.config(image = pika_5)
                user_entry.delete(0, len(letter)+1)
            elif attempts == 1:
                background.config(image = pika_6)
                user_entry.delete(0, len(letter)+1)
            elif attempts == 0:
                background.config(image = pika_7)
                user_entry.delete(0, len(letter)+1)
                messagebox.showerror("Note",
                                     "You failed Pikachu! The Pokemon was {}.".format(random_poke.upper()))
                reset()

#Reset function      
def reset():
    global random_poke, attempts, blanks, blanks_list, guess_already
    random_poke = random.choice(pokemon).lower()
    attempts = 6
    guess_already = []
    blanks = "_ " * len(random_poke)
    blanks_list = blanks.split()
    label_word.config(text = blanks)
    background.config(image = pika_1)
    print("A wild {} has appeared!".format(random_poke.upper()))

    #***Part Two: Visual properties and words of my game, including window***
window = Tk()

#Images and pika_<#> as variables
image1 = Image.open("pika1.png").resize((975,525), Image.LANCZOS)
pika_1 = ImageTk.PhotoImage(image1) 
image2 = Image.open("pika2.png").resize((975,525), Image.LANCZOS)
pika_2 = ImageTk.PhotoImage(image2) 
image3 = Image.open("pika3.png").resize((975,525), Image.LANCZOS)
pika_3 = ImageTk.PhotoImage(image3) 
image4 = Image.open("pika4.png").resize((975,525), Image.LANCZOS)
pika_4 = ImageTk.PhotoImage(image4) 
image5 = Image.open("pika5.png").resize((975,525), Image.LANCZOS)
pika_5 = ImageTk.PhotoImage(image5) 
image6 = Image.open("pika6.png").resize((975,525), Image.LANCZOS)
pika_6 = ImageTk.PhotoImage(image6) 
image7 = Image.open("pika7.png").resize((975,525), Image.LANCZOS)
pika_7 = ImageTk.PhotoImage(image7) 

#Word Bank
pokemon = ["bulbasaur", "ivysaur", "venusaur", "charmander", "charmeleon", "charizard", "squirtle",
         "wartortle", "blastoise", "caterpie", "metapod", "butterfree", "weedle", "kakuna", "beedrill",
         "pidgey", "pidgeotto", "pidgeot", "rattata", "raticate", "spearow", "fearow", "ekans", "arbok",
         "pikachu", "raichu", "sandshrew", "sandslash", "nidorina", "nidoqueen", "nidoran", "nidorino",
         "nidoking", "clefairy", "clefable", "vulpix", "ninetales", "jigglypuff", "wigglytuff", "zubat", "golbat",
         "oddish", "gloom", "vileplume", "paras", "parasect", "venonat", "venomoth", "diglett", "dugtrio", "meowth",
         "persian", "psyduck", "golduck", "mankey", "primeape", "growlithe", "arcanine", "poliwag", "poliwhirl",
         "poliwrath", "abra", "kadabra", "alakazam", "machop", "machoke", "machamp", "bellsprout", "weepinbell",
         "victreebel", "tentacool", "tentacruel", "geodude", "graveler", "golem", "ponyta", "rapidash", "slowpoke",
         "slowbro", "magnemite", "magneton", "farfetchd", "doduo", "dodrio", "seel", "dewgong", "grimer", "muk",
         "shellder", "cloyster", "gastly", "haunter", "gengar", "onix", "drowzee", "hypno", "krabby", "kingler", "voltorb",
         "electrode", "exeggcute", "exeggutor", "cubone", "marowak", "hitmonlee", "hitmonchan", "lickitung", "koffing",
         "weezing", "rhyhorn", "rhydon", "chansey", "tangela", "kangaskhan", "horsea", "seadra", "goldeen", "seaking",
         "staryu", "starmie", "mrmime", "scyther", "jynx", "electabuzz", "magmar", "pinsir", "tauros", "magikarp",
         "gyarados", "lapras", "ditto", "eevee", "vaporeon", "jolteon", "flareon", "porygon", "omanyte", "omastar",
         "kabuto", "kabutops", "aerodactyl", "snorlax", "articuno", "zapdos", "moltres", "dratini", "dragonair",
         "dragonite", "mewtwo", "mew" ]

#Make window
window.geometry("975x525")
window.resizable(width=False, height=False)
window.title("Who'sThatPokemon?!!")
window.iconbitmap("poke.ico")

#Variables
random_poke = random.choice(pokemon).lower()
attempts = 6
guess_already = []
blanks = "_ " * len(random_poke)
blanks_list = blanks.split()

#Make widgets
background = Label(window, image = stage1)
label_word = Label(window, text = blanks,
               font = ("Comic Sans MS", 30), background = "white")
user_entry = Entry(window, width = 5)
guess = Button(window, text = "Guess", width = 7,
               font = ("Comic Sans MS", 15), command = guess_button)
reset_button = Button(window, text = "Reset", width = 7,
               font = ("Comic Sans MS", 15), command = reset)

#Place widgets
background.place(x = 0, y = 0)
guess.pack(side = BOTTOM, pady = 20)
user_entry.pack(side = BOTTOM)
label_word.pack(side = BOTTOM, pady = 10)
reset_button.pack(side = TOP, pady = 10)

print("A wild {} has appeared!".format(random_poke.upper()))

window.mainloop()

