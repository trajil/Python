import win32api 

win32api.keybd_event(0x5B, 0, ) # LWIN
win32api.keybd_event(0x44, 0, ) # D
win32api.keybd_event(0x5B, 0, 2) 
win32api.keybd_event(0x44, 0, 2) 