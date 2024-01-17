rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

plus = '''    
   _   
 _| |_ 
|_   _|
  |_|  
  '''

# Schreiben Sie Ihren Programmcode unter dieser Zeile 👇

while True:
        
    print("\n\nWillkommen bei Stein,Papier,Schere.\n\n")

    import random
    import webbrowser
    urla = 'https://www.youtube.com/watch?v=hPr-Yc92qaY'
    urlb = 'https://www.youtube.com/watch?v=SxNCudPrSMg'
    urlc = 'https://www.youtube.com/watch?v=19dD18sSA4E'
    urld = 'https://www.youtube.com/shorts/o2RYTg6urK0'

    auswahl = input("Bitte wähle aus was DU nimmst:\n(1)Für Stein\n(2)Für Papier\n(3)Für Schere\nBitte Zahl eingeben:")


    computer = random.randint (1,3)


    if auswahl == "1" and computer == 1:
        print("\n\nUnentschieden")
        print((rock)+(plus)+(rock))
        print(webbrowser.open_new(urlc))
    

    elif auswahl == "1" and computer == 2:
        print("\n\nComputer gewinnt")
        print((rock)+(plus)+(paper))
        print(webbrowser.open_new(urla))

    elif auswahl == "1" and computer == 3:
        print("\n\nDu gewinnst")
        print((rock)+(plus)+(scissors))
        print(webbrowser.open_new(urlb))

    elif auswahl == "2" and computer == 1:
        print("\n\nDu gewinnst")
        print((paper)+(plus)+(rock))
        print(webbrowser.open_new(urlb))

    elif auswahl == "2" and computer == 2:
        print("\n\nUnentschieden")
        print((paper)+(plus)+(paper))
        print(webbrowser.open_new(urlc))

    elif auswahl == "2" and computer == 3:
        print("\n\nComputer gewinnt")
        print((paper)+(plus)+(scissors))
        print(webbrowser.open_new(urla))

    elif auswahl == "3" and computer == 1:
        print("\n\nComputer gewinnt")
        print((scissors)+(plus)+(rock))
        print(webbrowser.open_new(urla))

    elif auswahl == "3" and computer == 2:
        print("\n\nDu gewinnst")
        print((scissors)+(plus)+(paper))
        print(webbrowser.open_new(urlb))

    elif auswahl == "3" and computer == 3:
        print("\n\nUnentschieden")
        print((scissors)+(plus)+(scissors))
        print(webbrowser.open_new(urlc))

    else:
        print("\n\nBist du zu blöd zum lesen!!!")
        print(webbrowser.open_new(urld))
    
    wiederholen = input("Möchten Sie das Programm wiederholen? (j/n): ")
    if wiederholen.lower() != "j":
        break