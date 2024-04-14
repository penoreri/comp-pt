import tkinter as tk
import random

#base code
#-------------------------------------------------------------------------------------------
countries = ['singapore', 'russia', 'thailand', 'philippines', 'china', 'vietnam', 'japan', 'afghanistan',
            'cambodia', 'indonesia']

current_word = ""
score = 0

#scrambling of words
def scramble_word(word):
    letters = list(word)
    random.shuffle(letters)
    return ''.join(letters)

#starting a new game
def new_game():
    global current_word
    current_word = random.choice(countries)
    scrambled_word = scramble_word(current_word)
    lbl_word.config(text=scrambled_word)
    lbl_result.config(text="")
    lbl_score.config(text=f"Score: {score}")
    front_page.pack_forget()
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
    global score
    main_page.pack_forget()
    front_page.pack()
    score = 0
            
    
#exit
def exit_game():
    print ("Thanks for playing Country Scramble!")
    exit()

#please change the facts in these countries please lmao
def word_hint():
    if current_word == 'philippines':
        lbl_hint.config(text="This country is known for 'sana all'")
    elif current_word == 'indonesia':
        lbl_hint.config(text="This is a country where MLBB is well-known")
    elif current_word == 'singapore':
        lbl_hint.config(text="This is a country known for being the richest country in SEA")
    elif current_word == 'russia':
        lbl_hint.config(text="This is a country that is known to be the biggest in terms of land mass")
    elif current_word == 'afghanistan':
        lbl_hint.config(text="This is a country that is well-known for you know people")
    elif current_word == 'vietnam':
        lbl_hint.config(text="This is a country that is known for it's cofee")
    elif current_word == 'japan':
        lbl_hint.config(text="This is a country that is known for it's unique culture and of course anime")
    elif current_word == 'china':
        lbl_hint.config(text="This is a country that is known for cheap material branding lol")
    elif current_word == 'cambodia':
        lbl_hint.config(text="This is a country that is known well idk")
    elif current_word == 'thailand':
        lbl_hint.config(text="This is a country that is known people being transgender")
    else:
        lbl_hint.config(text='')
        
#--------------------------------------------------------------------------------------

#base window
root = tk.Tk()
root.title("Animal Word Scramble Game")
root.geometry("920x480")
root.config(bg = 'purple')
root.maxsize(920, 480)




front_page = tk.Frame(root, bg = 'purple', width = 920, height = 480)
front_page.pack()

welcome_label = tk.Label(front_page, text="Country Scramble!", font=("Helvetica", 35, 'bold'),
                         bg = 'purple', fg = 'white',)
welcome_label.pack(pady=75, padx=200)

start_button = tk.Button(front_page, text="Start", font=('Helvetica', 15, 'bold'), bg = 'purple', fg = 'white', bd = 0,
                         relief = 'sunken', activebackground ='purple', activeforeground = 'black', command=new_game)
start_button.pack()

exit_button = tk.Button(front_page, text="Exit", font=('Helvetica', 15, 'bold'), bg = 'purple', fg = 'white', bd = 0,
                        relief = 'sunken', activebackground ='purple', activeforeground = 'black', command=exit_game)
exit_button.pack()


main_page = tk.Frame(root, bg = 'purple', width = 920, height = 480)

lbl_score = tk.Label(main_page, text="", font=('Arial', 16, 'bold'), bg = 'purple', fg = 'white')
lbl_score.pack(pady = 10)

lbl_word = tk.Label(main_page, text="", font=('Arial', 20, 'bold'), bg = 'purple', fg = 'white')
lbl_word.pack(pady = 10)

entry_guess = tk.Entry(main_page, font=('Arial', 14, 'bold'), bd = 0 , bg = 'white', fg = 'black', justify = 'center')
entry_guess.pack()

btn_check = tk.Button(main_page, text="Check", font=('Arial', 16, 'bold'), bg = '#301934', fg = 'white', bd = 0,
                        relief = 'sunken', activebackground ='white', activeforeground = 'black', command=check_word)
btn_check.pack()

lbl_result = tk.Label(main_page, text="", font=('Arial', 16, 'bold'), bg = 'purple', fg = 'white')
lbl_result.pack()

btn_new_game = tk.Button(main_page, text="New Country", font=('Arial', 16, 'bold'), bg = '#301934', fg = 'white', bd = 0,
                        relief = 'sunken', activebackground ='white', activeforeground = 'black', command=restart_game)
btn_new_game.pack()

btn_back = tk.Button(main_page, text="Back", font = ('Arial', 16, 'bold'), bg = '#301934', fg = 'white', bd = 0,
                        relief = 'sunken', activebackground ='white', activeforeground = 'black', command=back_to_front_page)
btn_back.pack()

lbl_hint = tk.Label(main_page, text="", font=('Arial', 10, 'bold'), bg = 'purple', fg = 'white')
lbl_hint.pack()

main_page.pack_forget()


root.mainloop()
