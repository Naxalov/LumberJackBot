import os
import time

import mss

import mss.tools
import pyautogui
from PIL import ImageOps, Image, ImageDraw
import numpy as np
import pyscreenshot as ImageGrab

from pykeyboard import PyKeyboard

k = PyKeyboard()

time.sleep(2)
# print(pyautogui.displayMousePosition())

# Player (420,760)
playerCor = (420, 760)
playerColor = (161, 115, 62)
startCor = (480, 960)
# Top Left 420 670
topLeft = (420, 612)
topRight = (530, 612)
bunchColor = (161, 115, 62)
blueColor = (212, 247, 254)
# Top Right 540 670
# Start 480 960

# Mouse Left (395,960)
# mL = (395, 960)
# Mouse Right (560,960)
# mR = (560, 960)
pyautogui.press('space')
time.sleep(1)
image = ImageGrab.grab(bbox=(playerCor[0], playerCor[1], playerCor[0] + 1, playerCor[1] + 1))

# pixle = image.getpixel(playerCor)
pixle = image.getpixel((0, 0))
# print(pixle)
# image = image.crop((playerCor[0], playerCor[1], playerCor[0] + 100, playerCor[1] + 100))
# image.save("img{}.png".format(99))
topCor = topLeft
if pixle == playerColor:
    pyautogui.press('right')
    # topCor
i = 0
clr = blueColor
    # bbox = (10, 10, 510, 510)
# bbox=(10, 10, 510, 510)
# for i in range(0, 400):
# image = ImageGrab.grab()
for i in range(0, 405):
    # print(i)
    # image = ImageGrab.grab(bbox=(topCor[0], topCor[1], topCor[0] + 1, topCor[1] + 1))
    with mss.mss() as sct:
        sct_img = sct.grab((topCor[0], topCor[1], topCor[0] + 1, topCor[1] + 1))
        topLeftColor = sct_img.pixel(0, 0)
    time.sleep(0.1)

    # finish = image.getpixel(startCor)
    # if finish != (255, 255, 255):
    #     break
    # topLeftColor = image.getpixel((0, 0))
    # topLeftColor = image.getpixel(topCor)
    # image sav for debug
    # draw = ImageDraw.Draw(image)
    # draw.ellipse((topCor[0]-5, topCor[1]-5, topCor[0]+5, topCor[1]+5), outline='blue')
    # image.putpixel( (topCor[0],topCor[1]), (155, 155, 55))
    # draw.text((topCor[0], topCor[1]), "1111", fill="red")

    # image = image.crop((topCor[0] - 150, topCor[1] - 50, topCor[0] + 50, topCor[1] + 150))
    # image.save('image_{}.png'.format(i))
    # print(topLeftColor == bunchColor)
    if topLeftColor == clr:
        clr = blueColor

        k.tap_key(k.right_key)
        topCor = topRight

    else:
        clr = bunchColor
        k.tap_key(k.left_key)

        topCor = topLeft

    # print(clr)
# pyautogui.press('left')
