import ctypes
import os

# Get the current working directory
current_directory = os.getcwd()

# Set the relative path of the wallpaper image
wallpaper_path = current_directory + "\webcam\shot1.png"


# Set the style of the wallpaper
# 0: Center, 1: Stretch, 2: Tile, 6: Fit
wallpaper_style = 0

# Load the image
SPI_SETDESKWALLPAPER = 20
image = ctypes.c_wchar_p(wallpaper_path)

# Set the wallpaper
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image, wallpaper_style)