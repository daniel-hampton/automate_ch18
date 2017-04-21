#! python3

import time
import pyautogui


time.sleep(5)
pyautogui.click()   # click to put drawing program into focus
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0)    # move right
    distance = distance - 5
    pyautogui.dragRel(0, distance)    # move down
    pyautogui.dragRel(-distance, 0)   # move left
    distance = distance - 5
    pyautogui.dragRel(0, -distance)   # move up
