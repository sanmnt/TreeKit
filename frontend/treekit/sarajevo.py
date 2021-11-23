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

def tumble_up(pixels, sections, colors):
    for i in range(399, 399 - (80 *  sections), -80):
        for j, color in enumerate(colors):
            a = i - (j * 27)
            b = i - ((j + 1) * 27)

            if b < 0:
                b = 0

            if color == 'r':
                pixels[b:a:1] = (128, 0, 0)
            elif color == 'g':
                pixels[b:a:1] = (0, 128, 0)
            elif color == 'b':
                pixels[b:a:1] = (0, 0, 128)

def follow_up(pixels, timecode, color, start, end):
    duration = end - start
    num_lit = math.floor(((timecode - start) / duration) * 400)

    pixels[400 - num_lit:399] = color

def follow_down(pixels, timecode, color, start, end):
    duration = end - start
    num_lit = math.floor(((timecode - start) / duration) * 400)

    pixels[0:num_lit] = color

def fade_out(pixels, timecode, color, start, end):
    duration = end - start
    val = 1 - ((timecode - start) / duration)

    new_color = (math.floor(color[0] * val), math.floor(color[1] * val), math.floor(color[2] * val))
    pixels[:] = new_color
