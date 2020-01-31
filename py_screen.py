import pyscreenshot as ImageGrab

# fullscreen
# im = ImageGrab.grab()
# im.show()

# part of the screen
im = ImageGrab.grab(bbox=(0, 0, 400, 400))
im.save('1.png')
