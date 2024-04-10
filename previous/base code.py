import tkinter as tk
import random

#base code
#-------------------------------------------------------------------------------------------
animals = ['dog', 'cat', 'lion', 'tiger', 'elephant', 'giraffe', 'zebra', 'monkey',
            'snake', 'rhinoceros', 'hippopotamus', 'crocodile', 'kangaroo', 'penguin',
              'koala', 'camel', 'panda', 'cheetah', 'bear', 'wolf']
current_word = ""
score = 0

#scrambling of words
def scramble_word(word):
    letters = list(word)
    random.shuffle(letters)
    return ''.join(letters)

#starting a new game
def new_game():
    global current_word, score
    current_word = random.choice(animals)
    scrambled_word = scramble_word(current_word)
    lbl_word.config(text=scrambled_word)
    lbl_result.config(text="")
    lbl_score.config(text=f"Score: {score}")
    front_page.pack_forget()
    settings_page.pack_forget()
    main_page.pack()

#checker if the player is able to correctly guess the animal
def check_word():
    global score
    guessed_word = entry_guess.get().lower()
    if guessed_word == current_word:
        lbl_result.config(text="Correct!")
        score += 1
        lbl_score.config(text=f"Score: {score}")
        entry_guess.delete(0, tk.END)
        restart_game()
    else:
        lbl_result.config(text="Incorrect. Try again!")

#restart
def restart_game():
    main_page.pack_forget()
    new_game()

#back button basically
def back_to_front_page():
    main_page.pack_forget()
    front_page.pack()
    settings_page.pack()
#exit
def exit_game():
    exit()

#the settings menu
def settings():
    settings_label = tk.Label(settings_page, text="Settings", font=("Helvetica", 35))
    settings_label.pack()

    mode = tk.Label(settings_page, text ="Mode")
    mode.pack()

    win_mode = tk.Button(settings_page, text ="Windowed Mode")
    win_mode.pack()

    full_mode = tk.Button(settings_page, text ="Fullscreen Mode")
    full_mode.pack()

    front_page.pack_forget()
    settings_button.pack_forget()
#--------------------------------------------------------------------------------------

#base window
root = tk.Tk()
root.title("Animal Word Scramble Game")
root.geometry("920x480")
root.minsize(920, 480)
root.maxsize(1920, 1080)


front_page = tk.Frame(root)
front_page.pack()

settings_page = tk.Frame(root)
settings_page.pack()

welcome_label = tk.Label(front_page, text="Welcome to Word Scramble Game!", font=("Helvetica", 35))
welcome_label.pack(pady=20)

start_button = tk.Button(front_page, text="Start", command=new_game)
start_button.pack()


settings_button = tk.Button(settings_page, text="Settings", command=settings)
settings_button.pack()

exit_button = tk.Button(front_page, text="Exit", command=exit_game)
exit_button.pack()

main_page = tk.Frame(root)

#maybe.... -----------------
lbl_word = tk.Label(main_page, text="", font=('Arial', 24))
lbl_word.pack()

entry_guess = tk.Entry(main_page, font=('Arial', 14))
entry_guess.pack()

btn_check = tk.Button(main_page, text="Check", command=check_word)
btn_check.pack()

lbl_result = tk.Label(main_page, text="", font=('Arial', 16))
lbl_result.pack()

lbl_score = tk.Label(main_page, text="", font=('Arial', 16))

btn_new_game = tk.Button(main_page, text="New Word", command=restart_game)
btn_new_game.pack()

btn_back = tk.Button(main_page, text="Back", command=back_to_front_page)
btn_back.pack()

main_page.pack_forget()
#-----------------------------------------

root.mainloop()
