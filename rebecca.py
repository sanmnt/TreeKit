'''
need to check:
    light:
        is lighting in the correct format
            what color :o
        is tu sufficient
        is the blinking too sudden
    
    audio:
        what other songs/noises are good
        actually download/import the music
        run asynchronously?
'''

from playsound import playsound
import time
import random

### do I need these?
#import board
#import neopixel
#pixels = neopixel.NeoPixel(board.D18, 30)
pixels = [] # just so compiler doesn't yell at me

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
def off():
    # If the lights turning off is too harsh, change it in here
    pixels.fill((0, 0, 0))
    time.sleep(tu) # light off = between symbol

def on(t):
    # If I'm doing lights wrong, change it in here
    pixels.fill((0, 255, 0))
    ### or are we using this one
        #for i in range(strip.numPixels()):
        #  strip.setPixelColor(i, Color(0, 0, 0))
        #strip.show()
    time.sleep(t)
    off() #always needs to be turned off anyway

def dot():
    on(tu)

def dash():
    on(3 * tu)

def endLetter():
    time.sleep(3 * tu) # all symbols turn off the lights

def endWord():
    time.sleep(7 * tu) # all symbols turn off the lights

def lightJP():
    # Lights "John Python" in Morse code
    # .---/---/..../-.//.--./-.--/-/..../---/-.
    
    # J .---
    dot()
    dash()
    dash()
    dash()
    endLetter()

    # O ---
    dash()
    dash()
    dash()
    endLetter()

    # H ....
    dot()
    dot()
    dot()
    dot()
    endLetter()

    # N -.
    dash()
    dot()
    endLetter()

    endWord()


    # P .--.
    dot()
    dash()
    dash()
    dot()
    endLetter()

    # Y -.--
    dash()
    dot()
    dash()
    dash()
    endLetter()
    
    # T -
    dash()
    endLetter()
    
    # H ....
    dot()
    dot()
    dot()
    dot()
    endLetter()
    
    # O ---
    dash()
    dash()
    dash()
    endLetter()
    
    # N -.
    dash()
    dot()
    endLetter()

def jpTest():
    # Lights "JP" in Morse code
    # .---/.--.
    
    # J .---
    dot()
    dash()
    dash()
    dash()
    endLetter()

    # P .--.
    dot()
    dash()
    dash()
    dot()
    endLetter()    

def saria():
    # Lights first few measures of Saria's song
    # because it's stuck in my head.
    # using sheet music https://musescore.com/icelands_puffin/scores/848626 first 8 measures
    dot()
    dot()
    on(2)

    dot()
    dot()
    on(2)

    dot()
    dot()
    dot()
    dot()

    on(2)
    dot()
    dot()

    
    dot()
    dot()
    # split

    on(3) # or 4
    off()
    dot()
    
    dot()
    dot()
    on(4) # or 6



### AN AUDIO EXPERIENCE
### download playsound (pip install playsound==1.2.2) to play .mp3
def chaos():
    pickme = ["Toad sings", "Never gonna give you up"] # suggestions are welcome
    playsound(random.choice(pickme))

def funTimes():
    print("Dancing Queen")
    playsound("fun.mp3")

def calm(): # is this necessary
    print("Claire de Lune")

def festivity():
    print("Carol of the Bells")


chaos()