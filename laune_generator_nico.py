nameneingabe = input("\n\n\nBitte gebe dein Namen ein: ")

print(f"\n\n\nHey {nameneingabe}\n\n\nJetzt musst du deine aktuelle Laune angeben.\n\n1: Extrem gute Laune\n2: Sehr gute Laune\n3: Gute Laune\n4: Geht So\n5: Lass mich bitte\n6: Zieh Leine oder ich Box dich weg\n\n")

launeeingabe = int(input("\nBitte gebe nun deine Laune ein: "))
    
match launeeingabe:
    case 1: 
        print("\n\nSehr gut, dann kannst du mir während ich programmiere,\nein argentinisches Rumpsteak kaufen gehen und zubereiten.\nDanach räume die Wohnung auf und putz mein Auto.\n\n\n\n")

    case 2:
        print("\n\nSehr schön, dann kannst du mir was zum Essen machen\nUnd die Wohnung putzen\n\n\n\n")

    case 3:
        print("\n\nSuper, mach mir bitte was zu Essen\n\n\n\n")

    case 4:
        print("\n\nHallo, du siehst müde aus, ruhe dich gerne 10 Minuten aus.\nUnd dann mach was zu essen oder putz die Wohnung\n\n\n\n")

    case 5:
        print("\n\nWas ist los? Du siehst Kacke aus.\nAber weißt du was noch Kacke aussieht?\nRichtig, der Inhalt in meinem Magen\nKannst du mir bitte was zum Essen machen.\n\n\n\n")

    case 6:
        print("\n\nJunge, welcher LKW hat dich überfahren?\naber ja komm ran, dann baller ich dir eine\n\n\n\n")

    case _:
        print("\n\nDu bist ja zu blöd um eine Zahl zwischen 1 und 6 einzugeben!\n\n\n\n")
    