import random
import time
from tkinter import *

#-----------------------------------#

game_open = Tk()
game_open.geometry("1920x1080")

animal_options = ['Dog','Cat','Lion','Tiger','Elephant',
                  'Zebra','Parrot','Panda','Chicken','Duck','Turkey']
chosen_word = ""

def scramble_word(word):
    letters = list(word)
    random.shuffle(letters)
    return ''.join(letters)

def new_game():
    global chosen_word
    chosen_word = random.choice(animal_options)
    lbl_word.config(text=scramble_word)
    lbl_result.config(text='')

def check_word():
    guessed_word = entry_guess.get().lower()

#--------------------------------#
game_open.mainloop()
