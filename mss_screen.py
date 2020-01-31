import mss
import mss.tools

# Use the 1st monitor
monitor = mss.mss().monitors[1]

# Capture a bbox using percent values
left =0# monitor["left"] + monitor["width"] * 5 // 100  # 5% from the left
top = 0# monitor["top"] + monitor["height"] * 5 // 100  # 5% from the top
right = left + 400  # 400px width
lower = top + 400  # 400px height
bbox = (left, top, right, lower)

# Grab the picture
# Using PIL would be something like:
# im = ImageGrab(bbox=bbox)
im = mss.mss().grab(bbox)  # type: ignore

# Save it!
mss.tools.to_png(im.rgb, im.size, output="screenshot.png")
