#!/usr/bin/python3

import pygame
import pygame.midi
import sys

#                init
# =======================================
GRAND_PIANO = 0
CHURCH_ORGAN = 19
instrument = CHURCH_ORGAN
pygame.init()
pygame.midi.init()
print(pygame.midi.get_device_info(2))
midi_out = pygame.midi.Output(2)
midi_out.set_instrument(instrument)
# =======================================
def exit():
    global midi_out, music

    music = 0
    del midi_out
    pygame.midi.quit()
    pygame.quit()
    sys.exit()

mapping={ 94: 74, 38: 75, 25: 76, 12: 77,  
          52: 77, 39: 78, 26: 79, 13: 80,   
          53: 80, 40: 81, 27: 82, 14: 83,     
          54: 83, 41: 84, 28: 85, 15: 86,       
          55: 86, 42: 87, 29: 88, 16: 89,     
          56: 89, 43: 90, 30: 91, 17: 92,    
          57: 92, 44: 93, 31: 94, 18: 95,
          58: 95, 45: 95, 32: 96, 19: 97
        }

screen = pygame.display.set_mode((400, 400))
volume = 12

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            mapping.setdefault(event.scancode, 0)
            note = mapping.get(event.scancode)-12
            print(event)
            if note:
                midi_out.note_on(note, volume) 

        if event.type == pygame.KEYUP:
            mapping.setdefault(event.scancode, 0)
            note = mapping.get(event.scancode)-12
            if note:
                midi_out.note_off(note, volume) 

            if event.key == pygame.K_ESCAPE:
                exit()
