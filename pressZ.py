import time

import pyautogui

time.sleep(1)
for i in range(0, 100):
    pyautogui.press('A', pause=False)
    time.sleep(0.05)
