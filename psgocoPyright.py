import pygame

from snakEPython import game_window, green, orange

#psGo(orange, 'Fixed-sys', 20)

#game_window.blit(game_over_surface, game_over_rect)

def psGo(color, font, size):
    psGo_font = pygame.font.SysFont(font, size)
    psGo_surface = psGo_font.render('psGo © Alright Copyright 2023', True, color)
    psGo_rect = psGo_surface.get_rect()
    game_window.blit(psGo_surface, psGo_rect)

psGo(green, 'consolas', 10)