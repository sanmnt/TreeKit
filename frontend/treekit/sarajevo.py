import math
from random import randint
from time import sleep

def intro(pixels, timecode):
    if 0 <= timecode < 33.75:
        a = abs(math.sin(math.pi * timecode / 15))
        b = abs(math.cos(math.pi * timecode / 15))

        pixels[::3] = (int(a * 230), int(a * 200), 0)
        pixels[1::3] = (int(b * 230), int(b * 200), 0)
    else:
        a = ((-.707 / 4.25) * (timecode - 33.75)) + .707

        pixels[::3] = (int(a * 230), int(a * 200), 0)
        pixels[1::3] = (int(a * 230), int(a * 200), 0)

def flash(pixels):
    pixels[:] = (255,255,255)

def reset(pixels):
    pixels[:] = (0, 0, 0)

def twinkle(pixels):
    for i in range(50):
        pixels[randint(0, 399)] = (128,128,128)
