VIRTUAL_WIDTH = 1000
VIRTUAL_HEIGHT = 600
VIRTUAL_SCREEN_RECT = (VIRTUAL_HEIGHT, VIRTUAL_HEIGHT)

import pygame

def get_mouse_pos_virtual(screen):
    mx, my = pygame.mouse.get_pos()
    sw, sh = screen.get_size()
    vw, vh = VIRTUAL_SCREEN_RECT

    scale_x = vw / sw
    scale_y = vh / sh

    return int(mx * scale_x), int(my * scale_y)