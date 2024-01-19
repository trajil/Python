import os
import time

def seite1():
    os.system('cls')  # Für Windows: os.system('cls')
    print('''
 ____                                 _           _      ____      _                _    _   
|  _ \ _   _  __      ___   _ _ __ __| | ___  ___| |_   / ___| ___| |__   __ _  ___| | _| |_ 
| | | | | | | \ \ /\ / / | | | '__/ _` |/ _ \/ __| __| | |  _ / _ \ '_ \ / _` |/ __| |/ / __|
| |_| | |_| |  \ V  V /| |_| | | | (_| |  __/\__ \ |_  | |_| |  __/ | | | (_| | (__|   <| |_ 
|____/ \__,_|   \_/\_/  \__,_|_|  \__,_|\___||___/\__|  \____|\___|_| |_|\__,_|\___|_|\_\\__|\n\n\n''')

    print("Herzlichen Glückwunsch, du warst dumm genug meine Datei zu öffnen.")
    print("Nun hast du den Salat...\n")
    print("Du wirst schnell feststellen, dass es keine Möglichkeit gibt, dieses Programm zu schließen.")
    print("Ich rate dir, meinen Anweisungen zu folgen und keine Dummheiten zu machen.")
    print("Es ist vermutlich besser zu kooperieren, um deine Daten und Passwörter zu schützen.\n\n")
    
    name = input("Gib bitte deinen Namen ein, damit ich weiß, mit wem ich es zu tun habe: ")
    print("Die Eingabe wird verarbeitet...")
    
    # Timer für 5 Sekunden
    time.sleep(5)

    return name

def seite2(name):
    os.system('cls')  # Für Windows: os.system('cls')
    print(f"Hallo {name},\n")
    print("mein Name ist B1uez0ne, ich würde mich selbst als Hacktivisten bezeichnen.")
    print("Ich bekämpfe die Bösen und helfe den Armen, ähnlich wie Robin Hood")
    print("Keine Sorge, du wirst noch früh genug herausfinden, zu welcher Art Mensch du gehörst\n\n")
    print("Um dir zu demonstrieren, wie ernst diese Sache hier ist, werde ich dir ein kleines Beispiel liefern\n\n\n")

    
    return name

# Start the loop
while True:
    name = seite1()  # Speichere die Rückgabewerte von seite1() in name
    name = seite2(name)  # Speichere die Rückgabewerte von seite2() in name

    # Add a condition to exit the loop (you can modify this condition based on your requirements)
    user_input = input("Möchtest du fortfahren? (ja/nein): ").lower()
    if user_input != 'ja':
        break
