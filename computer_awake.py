import pyautogui
import time
from datetime import datetime
pyautogui.FAILSAFE = False

while(True):
    time.sleep(10)
    for i in range(0,200):
        pyautogui.moveTo(0,i*4)
    pyautogui.moveTo(1,1)
    for i in range(0,3):
        pyautogui.press("shift")
    print("Movement made at {}".format(datetime.now().time()))