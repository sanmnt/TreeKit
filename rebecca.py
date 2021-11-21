'''
need to check:
    light:
        is lighting in the correct format
            what color :o
        is tu sufficient
        is the blinking too sudden
    
    audio:
        what other songs/noises are good
'''

from playsound import playsound
import time

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
tu = 0.5

### LET THERE BE LIGHTS
def on(t):
    # If I'm doing lights wrong, change it in here
    pixels.fill((0, 255, 0))
    ### or are we using this one
    #for i in range(strip.numPixels()):
    #  strip.setPixelColor(i, Color(0, 0, 0))
    #strip.show()
    time.sleep(t)

def off():
    # If the lights turning off is too harsh, change it in here
    pixels.fill((0, 255, 0))
    time.sleep(tu) # light off = between symbol

def dot():
    on(tu)
    off()

def dash():
    on(3 * tu)
    off()

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



### AN AUDIO EXPERIENCE
### download playsound (pip install playsound==1.2.2) to play .mp3
def chaos():
    pickme = []
    print()
    # randomly play one:
    #   toad sings
    #   rick roll?

def funTimes():
    playsound("fun.mp3")
    print("Dancing Queen")

def calm():
    print("Claire de Lune")

def festivity():
    print("Carol of the Bells")