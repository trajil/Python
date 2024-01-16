import random

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

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
players = ["player", "computer"]
score_player = 0
score_computer = 0

game_on = True
first_round = True

def turn(player):
    print(f"placeholder turn")

def firstRound(first_round):
    print(f"placeholder firstRound")
    first_round = False
    
    for i in players:
        draw(i) 
        draw(i) 
    
    return first_round
    
    
def draw(player):
    global score_computer, score_player
    drawn_card = random.choice(cards)
    print(player,"card: ", drawn_card)
    if player == "player":
        score_player += drawn_card
        #return score_player
    elif player == "computer":
        score_computer += drawn_card
        #return score_computer 
        
def checkWinning(game_on):
    if score_computer > score_player:
        print("Computer won!")
        game_on = False
    elif score_computer < score_player:
        print("Player won!")
        game_on = False
    else:
        print("DRAW!")
        game_on = False
    
    return game_on
        
def askPlayerForCard():
    print(f"placeholder askPlayerForCard")
    
def askForReplay():
    global game_on, first_round
    question = input("Wanna replay? press Y\n").lower()
    if question == 'y':
        first_round = True
        game_on = True
    else:
        game_on = False

def printCurrentScore():
    print("Score-Player: ", score_player, "Score-Computer: ", score_computer)


print(logo)

while game_on:
    
    if first_round:
        firstRound(first_round)
    printCurrentScore()
    draw()
    
    turn()
    
    checkWinning(game_on)
    askForReplay()