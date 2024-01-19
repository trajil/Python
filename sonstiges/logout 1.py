import time 
import datetime as dt
import webbrowser

jetzt = dt.datetime.now()
print( jetzt.strftime("%A %H:%M"))

print("--------------------------------------------------------------------")
print("bitte log dich auf der webseit an\nden broser bitte nicht schlißsen\nsonnst wird man von der Webseite ausgeloggt \nseite öffnet gleich")
print("--------------------------------------------------------------------")
print("in 5sec gehts weiter")
time.sleep(5)
webbrowser.open("https://lernplattform.gfn.de/login/index.php")
input("Enter drücken")

start=True
print ("skipt läuft jetzt")
while start==True:
    
    jetzt = dt.datetime.now()
    zeit_dezimal = (int(jetzt.strftime("%H")))+ (int(jetzt.strftime("%M"))/60)
    
    wochentag = jetzt.strftime("%a")
    
    print("letzter Chek :", end="")
    print(jetzt.strftime("%H:%M"))
    if (wochentag == "Sonday" or wochentag == "Saturday"):
        print("es ist Wochenende")
        start=False
    else:
        if zeit_dezimal > 16.6 and zeit_dezimal < 23 :
            print("du hast feierabent")
            webbrowser.open("https://lernplattform.gfn.de/?stoppen=1/")
            print("du wurdest ausgeloggt")
            start=False
    time.sleep(5*60)
input()
























