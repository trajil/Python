import os
        
for filename in os.listdir('webcam/'):
    if os.path.isfile(os.path.join('webcam', filename)):
        os.remove(os.path.join('webcam', filename))