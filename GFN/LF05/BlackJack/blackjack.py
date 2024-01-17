import random
import os

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

message_welcome = "Get ready to lose all your money!"

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
players = ["player", "computer"]
score_player = 0
score_computer = 0
current_round = 0

game_on = True
first_round = True

def turn(player):
    print(f"###placeholder turn###")
    
    if player == "player":
        while score_player < 21:
            askPlayerForCard()
    else:
        askComputerForCard()

def firstRound(first_round):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"###placeholder firstRound###")
    print(logo, message_welcome, "\n")
    global score_player,score_computer     
    
    # resetting the scores after each game...
    score_player = 0
    score_computer = 0
    
    # stopping the code from repeating the first round
    first_round = False
    
    for i in players:
        draw(i) 
        draw(i) 
        
    printCurrentScore()
    return first_round
    
    
def draw(player):
    print(f"###placeholder draw###")
    global score_computer, score_player
    drawn_card = random.choice(cards)
    print(player,"card: ", drawn_card)
    if player == "player":
        score_player += drawn_card
        if drawn_card == 11:
            score_player = drawn_ace(score_player)
    elif player == "computer":
        score_computer += drawn_card
        if drawn_card == 11:
            score_computer = drawn_ace(score_computer)
        
        
def drawn_ace(score):
    print(f"###placeholder ACE###")
    if score > 21:
        return score - 10
    return score
        
def checkWinning(game_on):
    print(f"###placeholder checkWinning###")
    if (score_computer > score_player and score_computer <= 21) or (score_player > 21):
        print("Computer won!")
        game_on = False
    elif (score_player > score_computer and score_player <= 21) or (score_computer > 21):
        print("Player won!")
        game_on = False
    elif (score_computer == score_player and score_player <= 21):
        print("DRAW!")
        game_on = False
    
    return game_on
        
def askPlayerForCard():
    print(f"###placeholder askPlayerForCard###")
    print("\nYou have: ", score_player, "points right now, do you want to draw another card?\n 'D' to draw\n 'P' to pass ")
    question_to_draw = input("").lower()
    
    if question_to_draw == 'd':
        draw(players[0])
    elif question_to_draw == 'p':
        print("Next round...")
    else:
        print("Wrong input! Try again")
        #askPlayerForCard()

def askComputerForCard():
    print(f"###placeholder askComputerForCard###")    
    if score_computer <= 15:
        draw(players[1])
    
def askForReplay():
    print(f"###placeholder askForReplay###")
    global game_on, first_round
    question = input("Wanna replay? press Y\n").lower()
    if question == 'y':
        first_round = True
        game_on = True
    else:
        game_on = False

def printCurrentScore():
    print("Score-Player: >> ", score_player, " <<Score-Computer: >> ", score_computer, " <<")



while game_on:
    
    if first_round:
        first_round = firstRound(first_round)
    
    turn(players[0])
    turn(players[1])
    
    printCurrentScore()
    game_on = checkWinning(game_on)
    if not game_on:
        askForReplay()