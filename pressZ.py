import time
import numpy as np
# import pyautogui
#
# time.sleep(1)
# for i in range(0, 100):
#     pyautogui.press('A', pause=False)
#     time.sleep(0.05)
from pykeyboard import PyKeyboard

keyboard = PyKeyboard()

# time.sleep(1)
# for i in range(0, 100):
#     keyboard.tap_key(keyboard.right_key)
#
# # keyboard.tap_key(keyboard.left_key)


import mss
import mss.tools


# The screen part to capture
monitor = {"top": 160, "left": 160, "width": 1, "height": 1}
output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

# Grab the data
sct_img = mss.mss().grab(monitor)

# Save to the picture file
mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
print(output)
