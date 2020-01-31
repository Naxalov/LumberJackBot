# import time
#
# import pyautogui
#
# time.sleep(1)
# for i in range(0, 100):
#     pyautogui.press('A', pause=False)
#     time.sleep(0.05)
from pykeyboard import PyKeyboard

keyboard = PyKeyboard()


keyboard.tap_key(keyboard.right_key)


# keyboard.tap_key(keyboard.left_key)


