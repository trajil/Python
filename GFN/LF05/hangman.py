import random

# Step 2

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

game_on = True

statement_right = "Right choice of a letter!"
statement_wrong = "Wrong choice of a letter!"
statement_alzheimer = "We already had that one, Captain Alzheimer..."
statement_error = "Please choose only 1 letter at a time!"
question_replay = "Wanna replay? Press Y/N"

word_list = ["Dragonball", "JavaScript", "Python", "Programmieren"]
chosen_word = random.choice(word_list)
alive_begin, alive_current = len(chosen_word) + 5, len(chosen_word) + 5

letters_used = []
display = []


def turnCheck(guess):
    while True:
        print(guess)
        if len(guess) == 1:
            if guess in chosen_word:
                print(statement_right)
            else:
                print(statement_wrong)
            break
        else:
            print(statement_error)
    return guess


def inputJustOneLetter():
    global alive_current
    global letters_used
    if len(guess) != 1:
        print(statement_error)
        return None
    if guess in letters_used:
        print(statement_alzheimer)
        return None
    letters_used.append(guess)
    if guess in chosen_word:
        print(statement_right)
       
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
    
    



print(chosen_word)
while game_on:
    while alive_current > 0:
        guess = input("Guess a letter: ").lower()
        inputJustOneLetter()
        
        display.append("_")
        print("Lives left: ", alive_current)
        print(display)


    game_on = questionReplay()
    input("")