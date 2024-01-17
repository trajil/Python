import os
clear = lambda: os.system('cls')
clear()

import random

######### variabelen 
leben_start=3
herzen_auf_map = 5
Gegner_pr = 80

##############################

leben=["🖤🖤🖤🖤🖤🖤","🧡🖤🖤🖤🖤🖤","🧡🧡🖤🖤🖤","🧡🧡🧡🖤🖤","🧡🧡🧡🧡🖤","🧡🧡🧡🧡🧡"]

hohe= random.randint(10,20)
breite=random.randint(10,50)
player="O"

mapX=[]
for row in range(hohe):
    mapY=[]
    for column in range(breite):
        mapY.append("⚫")
    mapX.append(mapY)

gold_x=random.randint(1, hohe)
gold_y=random.randint(1, breite)
mapX[gold_x][gold_y] = "💰"


man_X =random.randint(1, hohe)
man_Y =random.randint(1, breite)
mapX[man_X][man_Y] = "🧔"
gold=False


herz_x =[]
herz_y =[]
for i in range(herzen_auf_map):
    herz_x.append(random.randint(1, hohe))
    herz_y.append(random.randint(1, breite))
    mapX[herz_x [i]][herz_y [i]] = "🧡"

while not(gold):

    for row in range(hohe):
        for column in range(breite):
            print(mapX[row][column], end=" ")
        print()

    print(leben[leben_start])
    con=input("WASD bewegt dich                                                 ")
   
    if con == "w":
        mapX[man_X][man_Y] = "⚫"
        man_X=man_X - 1
    mapX[man_X][man_Y] = "🧔"  

    if con == "s":
        mapX[man_X][man_Y] = "⚫"
        man_X=man_X +1
    mapX[man_X][man_Y] = "🧔"

    if con == "a":
        mapX[man_X][man_Y] = "⚫"
        man_Y=man_Y - 1
    mapX[man_X][man_Y] = "🧔"
    
    if con == "d":
        mapX[man_X][man_Y] = "⚫"
        man_Y=man_Y + 1
    mapX[man_X][man_Y] = "🧔"
    
    
    for i in range (herzen_auf_map):
        print(leben_start)
        if man_X == herz_x[i] and man_Y == herz_y[i] and leben_start < 5:
            leben_start=leben_start + 1
            print("+1 🧡")
            herzen_auf_map= herzen_auf_map - 1
            herz_x[i].remove()
            herz_y[i].remove()
            
        elif man_X == herz_x[i] and man_Y == herz_y[i] and leben_start >= 5 :
            mapX[man_X][man_Y] = "🧡"
            print("du hast maximales leben")
        
    if leben == 0:
        clear()
        print("du bist tot")
        break
   
    clear()
    
    
    if man_X == gold_x and man_Y== gold_y:
        



        print ("        ██████  ██    ██     ██   ██  █████  ███████ ████████             ")
        print ("        ██   ██ ██    ██     ██   ██ ██   ██ ██         ██                ")
        print ("        ██   ██ ██    ██     ███████ ███████ ███████    ██                ")
        print ("        ██   ██ ██    ██     ██   ██ ██   ██      ██    ██                ")
        print ("        ██████   ██████      ██   ██ ██   ██ ███████    ██                ")
        print ("                                                                          ")
        print ("                                                                          ")
        print (" ██████  ███████ ██     ██  ██████  ███    ██ ███    ██ ███████ ███    ██ ")
        print ("██       ██      ██     ██ ██    ██ ████   ██ ████   ██ ██      ████   ██ ")
        print ("██   ███ █████   ██  █  ██ ██    ██ ██ ██  ██ ██ ██  ██ █████   ██ ██  ██ ")
        print ("██    ██ ██      ██ ███ ██ ██    ██ ██  ██ ██ ██  ██ ██ ██      ██  ██ ██ ")
        print (" ██████  ███████  ███ ███   ██████  ██   ████ ██   ████ ███████ ██   ████ ")
        print ("                                                                          ")
        gold=True


