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

mapping={ pygame.K_y: 74, pygame.K_s: 75, pygame.K_e: 76, pygame.K_4: 77,  
          pygame.K_x: 77, pygame.K_d: 78, pygame.K_r: 79, pygame.K_5: 80,   
          pygame.K_c: 80, pygame.K_f: 81, pygame.K_t: 82, pygame.K_6: 83,     
          pygame.K_v: 83, pygame.K_g: 84, pygame.K_z: 85, pygame.K_7: 86,       
          pygame.K_b: 86, pygame.K_h: 87, pygame.K_u: 88, pygame.K_8: 89,     
          pygame.K_n: 89, pygame.K_j: 90, pygame.K_i: 91, pygame.K_9: 92,    
          pygame.K_m: 92, pygame.K_k: 93, pygame.K_o: 94
        }

screen = pygame.display.set_mode((400, 400))
volume = 127

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            mapping.setdefault(event.key, 0)
            note = mapping.get(event.key)-12
            if note:
                midi_out.note_on(note, volume) 

        if event.type == pygame.KEYUP:
            mapping.setdefault(event.key, 0)
            note = mapping.get(event.key)-12
            if note:
                midi_out.note_off(note, volume) 

            if event.key == pygame.K_ESCAPE:
                exit()
