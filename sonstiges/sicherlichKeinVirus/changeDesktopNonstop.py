import ctypes
import os
import time
current_directory = os.getcwd()


for each in range(1000):
    wallpaper_path = current_directory + f"\webcam\shot{each}.png"
    wallpaper_style = 0

    SPI_SETDESKWALLPAPER = 20
    image = ctypes.c_wchar_p(wallpaper_path)

    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image, wallpaper_style)
    time.sleep(0.5)