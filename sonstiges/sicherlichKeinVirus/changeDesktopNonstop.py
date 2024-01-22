import ctypes
import os
import time
current_directory = os.getcwd()
picture_exists = False
wallpaper_path_check = current_directory + f"\webcam\shot1.png"

def checkForPictureExistence(picture_exists):
    while not picture_exists:
        picture_exists = os.path.isfile(wallpaper_path_check)
        if picture_exists:
            print("picture_exists")
            break
        else:
            print("no such file...")
        time.sleep(1)
    return picture_exists
        
def changeDesktopNonstop():
    for each in range(240):
        wallpaper_path = current_directory + f"\webcam\shot{each}.png"
        wallpaper_style = 0

        SPI_SETDESKWALLPAPER = 20
        image = ctypes.c_wchar_p(wallpaper_path)

        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image, wallpaper_style)
        time.sleep(0.5)
                
picture_exists = checkForPictureExistence(picture_exists)
if picture_exists: changeDesktopNonstop()