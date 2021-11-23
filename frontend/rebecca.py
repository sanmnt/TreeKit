'''
need to check:
    light:
        is lighting in the correct format
            what color :o
        is tu sufficient
        is the blinking too sudden
'''
import asyncio
import os
import time
import random

from dotenv import load_dotenv
from playsound import playsound

from treekit.lighting_client import LightingClient

load_dotenv()
client = LightingClient(400)
pixels = client.pixels

'''
GENERAL MORSE CODE RULES for my reference
    TU = time unit (toggle-able)
    dot = 1TU
    dash = 3TU
    between dot/dash = 1TU
    between letters = 3TU
    between words = 7TU
'''
tu = 0.5 # time unit (change if it's too long or short)

### LET THERE BE LIGHTS
async def off():
    # If the lights turning off is too harsh, change it in here
    pixels.fill((0, 0, 0))
    await client.send_frame()
    await asyncio.sleep(tu) # light off = between symbol

async def on(t):
    # If I'm doing lights wrong, change it in here
    pixels.fill((0, 255, 0))
    await client.send_frame()

    await asyncio.sleep(t)
    await off() #always needs to be turned off anyway

async def dot():
    await on(tu)

async def dash():
    await on(3 * tu)

async def endLetter():
    await asyncio.sleep(3 * tu) # all symbols turn off the lights

async def endWord():
    await asyncio.sleep(7 * tu) # all symbols turn off the lights

async def lightJP():
    # Lights "John Python" in Morse code
    # .---/---/..../-.//.--./-.--/-/..../---/-.

    # J .---
    await dot()
    await dash()
    await dash()
    await dash()
    await endLetter()

    # O ---
    await dash()
    await dash()
    await dash()
    await endLetter()

    # H ....
    await dot()
    await dot()
    await dot()
    await dot()
    await endLetter()

    # N -.
    await dash()
    await dot()
    await endLetter()

    await endWord()


    # P .--.
    await dot()
    await dash()
    await dash()
    await dot()
    await endLetter()

    # Y -.--
    await dash()
    await dot()
    await dash()
    await dash()
    await endLetter()

    # T -
    await dash()
    await endLetter()

    # H ....
    await dot()
    await dot()
    await dot()
    await dot()
    await endLetter()

    # O ---
    await dash()
    await dash()
    await dash()
    await endLetter()

    # N -.
    await dash()
    await dot()
    await endLetter()

async def jpTest():
    # Lights "JP" in Morse code
    # .---/.--.

    # J .---
    await dot()
    await dash()
    await dash()
    await dash()
    await endLetter()

    # P .--.
    await dot()
    await dash()
    await dash()
    await dot()
    await endLetter()

async def saria():
    # Lights first few measures of Saria's song
    # because it's stuck in my head.
    # using sheet music https://musescore.com/icelands_puffin/scores/848626 first 8 measures
    await dot()
    await dot()
    await on(2)

    await dot()
    await dot()
    await on(2)

    await dot()
    await dot()
    await dot()
    await dot()

    await on(2)
    await dot()
    await dot()


    await dot()
    await dot()
    # split

    await on(3) # or 4
    await off()
    await dot()

    await dot()
    await dot()
    await on(4) # or 6



### AN AUDIO EXPERIENCE
# download playsound (pip install playsound==1.2.2) to play .mp3
# song only plays while code executes
def chaos():
    pickme = ["music/fun.mp3", "music/ToadChristmas.mp3"]
    playsound(random.choice(pickme), block = False)

def funTimes():
    print("Dancing Queen")
    playsound("music/fun.mp3", block = False)

def festivity():
    print("Toad Christmas")
    playsound("music/ToadChristmas.mp3", block = False)

async def main():
    await client.connect(os.getenv('ADDRESS', 'localhost:8000'))

    funTimes()
    await lightJP()

if __name__ == '__main__':
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        asyncio.get_event_loop().run_until_complete(client.close())
        asyncio.get_event_loop().run_forever()
    finally:
        asyncio.get_event_loop().close()
