import random

# Step 1
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.



statement_right = "Right choice of a letter!"
statement_wrong = "Wrong choice of a letter!"
statement_error = "Please choose only 1 letter at a time!"

word_list = ["Dragonball", "JavaScript", "Python", "Programmieren"]
chosen_word = random.choice(word_list)


while True:
    guess = input("Guess a letter: ")

    # Check if the input is exactly one character
    if len(guess) == 1:
        if guess in chosen_word:
            print(statement_right)
        else:
            print(statement_wrong)
        break
    else:
        print(statement_error)

