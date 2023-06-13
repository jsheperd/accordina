#!/usr/bin/env python

import pygame
import pygame.midi
import sys
from goto import label, goto

#                init
# =======================================
GRAND_PIANO = 0
CHURCH_ORGAN = 19
WHISTLE = 78
ATMOSPHERE = 99
instrument = ATMOSPHERE
pygame.init()
pygame.midi.init()
print(pygame.midi.get_device_info(2))
midi_out = pygame.midi.Output(2)
midi_out.set_instrument(instrument)
music = True
# =======================================
def exit():
    global midi_out, music

    music = False
    pygame.midi.quit()
    del midi_out
    print("still ok")
    #pygame.quit()
    print("it is missing")
    sys.exit()

mapping={ 94: 74, 38: 75, 25: 76, 12: 77,  
          52: 77, 39: 78, 26: 79, 13: 80,   
          53: 80, 40: 81, 27: 82, 14: 83,     
          54: 83, 41: 84, 28: 85, 15: 86,       
          55: 86, 42: 87, 29: 88, 16: 89,     
          56: 89, 43: 90, 30: 91, 17: 92,    
          57: 92, 44: 93, 31: 94, 18: 95,
          58: 95, 45: 96, 32: 97, 19: 98,
          59: 98, 46: 99, 33: 100, 20: 101,
          60: 101, 47: 102, 34: 103, 21: 104,
          61: 104, 48: 105, 35: 106, 22: 107
        }



mapping={  100:  62,  4:   63,  26:  64,  32:  65,
           29:   65,  22:  66,  8:   67,  33:  68,
           27:   68,  7:   69,  21:  70,  34:  71,
           6:    71,  9:   72,  23:  73,  35:  74,
           25:   74,  10:  75,  28:  76,  36:  77,
           5:    77,  11:  78,  24:  79,  37:  80,
           17:   80,  13:  81,  12:  82,  38:  83,
           16:   83,  14:  84,  18:  85,  39:  86,
           54:   86,  15:  87,  19:  88,  45:  89,
           55:   89,  51:  90,  47:  91,  46:  92,
           56:   92,  52:  93,  48:  94,
}


        

screen = pygame.display.set_mode((400, 400))
volume = 120

def midi2human(note):
    pos = note%12
    val = ['c','c#','d','d#','e','f','f#','g','g#','a','a#','h'][pos]
    print("midi note:", note, val)


while music:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            mapping.setdefault(event.scancode, 0)
            note = mapping.get(event.scancode)
            #print(event)
            if note:
                midi2human(note)
                midi_out.note_on(note, volume) 

        if event.type == pygame.KEYUP:
            mapping.setdefault(event.scancode, 0)
            note = mapping.get(event.scancode)
            if note:
                midi_out.note_off(note, volume) 

            if event.key == 27:
                exit()
            if event.key == pygame.K_ESCAPE:
                exit()

