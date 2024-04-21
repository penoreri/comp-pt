import tkinter as tk
import random

#different functions
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
    global hint_count
    main_page.pack_forget()
    lbl_hint.config(text='')
    hint_count = 0
    new_game()

#back button basically
def back_to_front_page():
    global score, hint_count
    main_page.pack_forget()
    front_page.pack()
    score = 0
    hint_count = 0
    lbl_hint.config(text='')
            
    
#exit
def exit_game():
    print ("Thanks for playing Country Scramble!")
    exit()

global hint_count
hint_count = 0

def word_hint(count):
    global hint_count
    hint_count = count
    
    #getting name length of the country
    word_length = len(current_word)
    
    #showing the hint
    if count < word_length:
        lbl_hint.config(text=f'{lbl_hint["text"]} {current_word[count]}')
        hint_count +=1
        
#--------------------------------------------------------------------------------------

#base window
root = tk.Tk()
root.title("Country Scramble")
root.geometry("920x480")
root.config(bg = '#C39BD3')
root.maxsize(920, 480)

front_page = tk.Frame(root, bg = '#C39BD3', width = 920, height = 480)
front_page.pack()

welcome_label = tk.Label(front_page, text="Country Scramble!", font=("Helvetica", 35, 'bold'),
                         bg = '#C39BD3', fg = '#EBDEF0',)
welcome_label.pack(pady=75, padx=200)

start_button = tk.Button(front_page, text="Start", font=('Helvetica', 15, 'bold'), bg = '#C39BD3', fg = '#EBDEF0', bd = 0,
                         relief = 'sunken', activebackground ='#C39BD3', activeforeground = '#EBDEF0', command=new_game)
start_button.pack()

exit_button = tk.Button(front_page, text="Exit", font=('Helvetica', 15, 'bold'), bg = '#C39BD3', fg = '#EBDEF0', bd = 0,
                        relief = 'sunken', activebackground ='#C39BD3', activeforeground = '#EBDEF0', command=exit_game)
exit_button.pack()


main_page = tk.Frame(root, bg = '#C39BD3', width = 920, height = 480)

lbl_score = tk.Label(main_page, text="", font=('Arial', 16, 'bold'), bg = '#C39BD3', fg = '#EBDEF0')
lbl_score.pack(pady = 10)

lbl_word = tk.Label(main_page, text="", font=('Arial', 20, 'bold'), bg = '#C39BD3', fg = '#EBDEF0')
lbl_word.pack(pady = 10)

entry_guess = tk.Entry(main_page, font=('Arial', 14, 'bold'), bd = 0 , bg = 'white', fg = 'black', justify = 'center')
entry_guess.pack()

btn_check = tk.Button(main_page, text="Check", font=('Arial', 16, 'bold'), bg = '#A569BD', fg = '#EBDEF0', bd = 0,
                        relief = 'sunken', activebackground ='white', activeforeground = 'black', command=check_word)
btn_check.pack()

lbl_result = tk.Label(main_page, text="", font=('Arial', 16, 'bold'), bg = '#C39BD3', fg = '#EBDEF0')
lbl_result.pack()

btn_new_game = tk.Button(main_page, text="New Country", font=('Arial', 16, 'bold'), bg = '#A569BD', fg = '#EBDEF0', bd = 0,
                        relief = 'sunken', activebackground ='white', activeforeground = 'black', command=restart_game)
btn_new_game.pack()

btn_back = tk.Button(main_page, text="Back", font = ('Arial', 16, 'bold'), bg = '#A569BD', fg = 'white', bd = 0,
                        relief = 'sunken', activebackground ='white', activeforeground = 'black', command=back_to_front_page)
btn_back.pack(pady= 2)

hint_btn = tk.Button(main_page, text="Hint", font = ('Arial', 16, 'bold'), bg = '#A569BD', fg = 'white', bd = 0,
                        relief = 'sunken', activebackground ='white', activeforeground = 'black', width = 4, command=lambda: word_hint(hint_count))
hint_btn.pack(pady= 2)

lbl_hint = tk.Label(main_page, text="", font=('Arial', 14, 'bold'), bg = '#C39BD3', fg = 'white')
lbl_hint.pack()

main_page.pack_forget()

root.mainloop()
