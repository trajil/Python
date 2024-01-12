import random
from art import logo 
from art import stages 

game_on = True

statement_right = "Right choice of a letter!"
statement_wrong = "Wrong choice of a letter!"
statement_alzheimer = "We already had that one, Captain Alzheimer..."
statement_error = "Please choose only 1 letter at a time!"
question_replay = "Wanna replay? Press Y/N"
statement_winner = "We have a Bingo!"
statement_loser = "Sorry, you've lost."

filler_length = 50
filler = ":"


def turn():
    global alive_current
    global letters_used
    if len(guess) != 1:
        print("\n" ,filler_length * filler, "\n" ,statement_error)
        return None
    if guess in letters_used:
        print("\n" ,filler_length * filler, "\n" ,statement_alzheimer)
        return None
    
    
    letters_used.append(guess)
    
    
    if guess in chosen_word.lower():
        print("\n" ,filler_length * filler, "\n" ,statement_right)
        for i in range(len(chosen_word.lower())):
            if i == 0 and chosen_word[0].lower() == guess:
                display[0] = guess.upper()
            if i != 0 and chosen_word[i].lower() == guess:
                display[i] = guess
    else:
        print("\n" ,filler_length * filler, "\n" ,statement_wrong)
        
        alive_current -= 1

    return guess



def questionReplay():
    replay = input(question_replay).lower()
    if replay == "y":
        return True
    elif replay == "n":
        return False 
    else:
        print("Invalid input!")
        return False
    
def checkDisplay():
    global game_finished
    if display.count("_") == 0:
        game_finished = True
    
while game_on:
    
    
    # loading wordlist
    with open("C:\Projekte\Python\GFN\LF05\wordlist.txt") as w:
        lines = w.readlines()
    word_list_txt = []
    for line in lines:
        word_list_txt.append(line.strip())
                              
    print(logo)
    chosen_word = random.choice(word_list_txt)
    print("Debug_mode: ",chosen_word)
    alive_current = len(stages) -1 
    #alive_current = len(chosen_word) + 5
    display = ["_" for _ in chosen_word]
    game_finished = False
    letters_used = []
    
    while alive_current > 0 and not game_finished:
        guess = input("Guess a letter: ").lower()
        turn()
        
        # display.append("_")
        print("Lives left: ", alive_current)
        print(stages[alive_current])
        print(display)
        checkDisplay()

    if game_finished:
        print(statement_winner)
    if alive_current < 1:
        print(statement_loser)    
        
    game_on = questionReplay()        
    input("")