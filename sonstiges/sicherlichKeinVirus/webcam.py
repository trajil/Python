import cv2
import time
import os
from pathlib import Path

Path("webcam/").mkdir(parents=True, exist_ok=True)
folder_path = "webcam/"
number_of_pics = 240

current_directory = os.getcwd()

#Initialize the camera
cam_port = 0
print(f"trying port {cam_port}")
portlimit = 10
cam = cv2.VideoCapture(cam_port)
start_program = 0

# Trying out ports 0 - 9
while not cam.isOpened():
        print(f"Error: Camera{cam_port} could not be opened")
        time.sleep(60)
        cam_port += 1
        print(f"trying port {cam_port}")
        cam = cv2.VideoCapture(cam_port)
        if cam_port > portlimit: break
        
if cam.isOpened():
    for i in range(number_of_pics):
        print(f"working on port {cam_port}")
        result, image = cam.read()
        if result:
            pic_name = f"{folder_path}shot{i}.png"
            cv2.imwrite(pic_name, image)
            if start_program == 0:
                time.sleep(0.5)
                path = current_directory + '\changeDesktopNonstop.py'
                os.startfile(path)
                start_program += 1
            time.sleep(0.5)
        else:
            print("No image detected. Please! try again")

    
cam.release()