import pyautogui, os, time, requests, sys
import numpy as np
from PIL import Image

sizemod = int(sys.argv[1])

while True:
    screenshot = pyautogui.screenshot()
    smallimg = screenshot.resize((round(screenshot.width/sizemod), round(screenshot.height/sizemod)), resample=Image.BILINEAR)

    # smallimg.save('result.png')

    pixels = list(smallimg.getdata())

    requests.post("https://screenshare.cintill.repl.co/getdata", data={"image": str([pixels, smallimg.mode, smallimg.size])})

    print("updated!")
