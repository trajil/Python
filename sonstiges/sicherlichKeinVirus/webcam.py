import cv2
import time

# Initialize the camera
cam_port = 0
cam = cv2.VideoCapture(cam_port)

folder_path = "webcam/"

# Check if camera opened successfully
if not cam.isOpened():
    print("Error: Camera could not be opened")
else:
    number_of_pics = 1000
    for i in range(number_of_pics):
        result, image = cam.read()
        if result:
            pic_name = f"{folder_path}shot{i}.png"
            cv2.imwrite(pic_name, image)
            time.sleep(0.5)
        else:
            print("No image detected. Please! try again")

# Release the camera
cam.release()
