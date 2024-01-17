import random
import os

# DEBUG_MODE
print_placeholders = False

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
winner = ""
score_player = 0
score_computer = 0
current_round = 0
money = 500
bet = 0

game_on = True
first_round = True



### TURN LOGICS ###
def firstRound(first_round):
    if print_placeholders: print(f"###placeholder firstRound###")
    print(logo, message_welcome, "\n")
    global score_player,score_computer, winner   
    # resetting the scores after each game...
    score_player = 0
    score_computer = 0
    winner = ""
    # stopping the code from repeating the first round
    first_round = False
    for i in players:
        draw(i) 
        draw(i) 
        
    printCurrentScore()
    return first_round
    
def turn(player):
    if print_placeholders: print(f"###placeholder turn###")
    
    drawing = True
    if player == "player":
        while score_player < 21 and drawing:
            drawing = askPlayerForCard(drawing)
    else:
        askComputerForCard()
    
def draw(player):
    if print_placeholders: print(f"###placeholder draw###")
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
    if print_placeholders: print(f"###placeholder ACE###")
    if score > 21:
        return score - 10
    return score
        
def checkWinning(game_on):
    global winner
    if print_placeholders: print(f"###placeholder checkWinning###")
    if (score_computer > score_player and score_computer <= 21) or (score_player > 21):
        print("Computer won!")
        printCurrentScore()
        game_on = False
        winner = players[1]
    elif (score_player > score_computer and score_player <= 21) or (score_computer > 21):
        print("Player won!")
        printCurrentScore()
        game_on = False
        winner = players[0]
    elif (score_computer == score_player and score_player <= 21):
        print("DRAW!")
        printCurrentScore()
        game_on = False
        winner = "nobody"
    return game_on
        
        
        
### MONEY LOGIC ###
def bankStart(bet):
    os.system('cls' if os.name == 'nt' else 'clear')
    bet = 0
    if print_placeholders: print(f"###placeholder bankStart###")
    printCurrentMoney()
    
    bet = askPlayerForMoney(bet)
    print("Your bet: ", bet)
    return bet
       
def bankEnd(money, bet, winner):
    if print_placeholders: print(f"###placeholder bankEnd###")
    
    match winner:
        case "player":
            money = money + bet
        case "computer":
            money = money - bet
        case "nobody":
            money = money
    
    return money 
        
        
        
# ASKING PLAYER AND COMPUTER
def askPlayerForMoney(bet):
    if print_placeholders: print(f"###placeholder askPlayerForMoney###")
    bet = bet
    bet = int(input("How much money do you want to bet?"))
    if bet > money: bet = money
    return bet
        
def askPlayerForCard(drawing):
    if print_placeholders: print(f"###placeholder askPlayerForCard###")
    print("\nYou have: ", score_player, "points right now, do you want to draw another card?\n 'D' to draw\n 'P' to pass ")
    question_to_draw = input("").lower()
    
    if question_to_draw == 'd':
        draw(players[0])
        
    elif question_to_draw == 'p':
        print("Next round...")
        drawing = False
    else:
        print("Wrong input! Try again")
    return drawing

def askComputerForCard():
    if print_placeholders: print(f"###placeholder askComputerForCard###")    
    if score_computer <= 15:
        draw(players[1])
    
def askForReplay():
    if print_placeholders: print(f"###placeholder askForReplay###")
    global game_on, first_round
    question = input("Wanna replay? press Y\n").lower()
    if question == 'y' and money <= 0:
        print("You actually need money, honey...")
        game_on = False
    elif question == 'y' and money > 1500:
        print("Sir, please cash out and don't come back again!")
        game_on = False
    elif question == 'y':
        first_round = True
        game_on = True
    else:
        game_on = False



### PRINTING OUT ###
def printCurrentScore():
    if print_placeholders: print(f"###placeholder printCurrentScore###")
    print("Score-Player: >> ", score_player, " <<Score-Computer: >> ", score_computer, " <<")

def printCurrentMoney():
    if print_placeholders: print(f"###placeholder printCurrentMoney###")
    if money > 0:
        print(f"You have {money} $ right now ")
    else:
        print("YOU ARE BROKE!")


### MAIN ###
while game_on and (money > 0 and money < 1500):
    if first_round:
        bet = bankStart(money)
        first_round = firstRound(first_round)
       
    turn(players[0])
    turn(players[1])
    
    printCurrentScore()
    game_on = checkWinning(game_on)
    if not game_on:
        money = bankEnd(money,bet,winner)
        printCurrentMoney()
        askForReplay()