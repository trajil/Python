import random

# Step 3

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

game_on = True

statement_right = "Right choice of a letter!"
statement_wrong = "Wrong choice of a letter!"
statement_alzheimer = "We already had that one, Captain Alzheimer..."
statement_error = "Please choose only 1 letter at a time!"
question_replay = "Wanna replay? Press Y/N"
statement_winner = "We have a Bingo!"
statement_loser = "Sorry, you've lost."

word_list = ["Dragonball", "JavaScript", "Python", "Programmieren"]

def turn():
    global alive_current
    global letters_used
    if len(guess) != 1:
        print(statement_error)
        return None
    if guess in letters_used:
        print(statement_alzheimer)
        return None
    
    
    letters_used.append(guess)
    
    
    if guess in chosen_word.lower():
        print(statement_right)
        for i in range(len(chosen_word.lower())):
            if i == 0 and chosen_word[0].lower() == guess:
                display[0] = guess.upper()
            if i != 0 and chosen_word[i].lower() == guess:
                display[i] = guess
    else:
        print(statement_wrong)
        
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
    chosen_word = random.choice(word_list)
    print(chosen_word)
    alive_current = len(chosen_word) + 5
    display = ["_" for _ in chosen_word]
    game_finished = False
    letters_used = []
    
    while alive_current > 0 and not game_finished:
        guess = input("Guess a letter: ").lower()
        turn()
        
        # display.append("_")
        print("Lives left: ", alive_current)
        print(display)
        checkDisplay()

    if game_finished:
        print(statement_winner)
    if alive_current < 1:
        print(statement_loser)    
    
    
    game_on = questionReplay()        
    input("")